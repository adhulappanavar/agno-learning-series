#!/usr/bin/env python3
"""
Enhanced Flask backend for React UI with WebSocket support
Serves workflow data and provides real-time execution monitoring
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import sqlite3
import os
import json
import subprocess
import threading
import time
import sys
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'agno-workflow-secret-key'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

def get_workflows():
    """Get all workflows from the database"""
    try:
        db_path = "../workflow_states.db"
        if not os.path.exists(db_path):
            return []
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all workflows
        cursor.execute("""
            SELECT workflow_id, current_stage, status, created_at, updated_at, stage_data
            FROM workflow_states
            ORDER BY created_at DESC
        """)
        
        workflows = []
        for row in cursor.fetchall():
            workflow = {
                'id': row[0], # Maps workflow_id to 'id' for the frontend
                'stage': row[1],
                'status': row[2],
                'created_at': row[3],
                'updated_at': row[4],
                'stage_data': row[5] if row[5] else '{}'
            }
            workflows.append(workflow)
        
        conn.close()
        return workflows
        
    except Exception as e:
        print(f"Error getting workflows: {e}")
        return []

def execute_workflow(workflow_id, socket_id):
    """Execute a workflow and stream output via WebSocket"""
    try:
        # Emit start message
        socketio.emit('workflow_started', {
            'workflow_id': workflow_id,
            'message': f'🚀 Starting workflow execution for {workflow_id}',
            'timestamp': datetime.now().isoformat(),
            'type': 'info'
        }, room=socket_id)
        
        # Change to the parent directory where the main workflow script is
        workflow_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(workflow_dir)
        
        # Emit directory change message
        socketio.emit('workflow_output', {
            'workflow_id': workflow_id,
            'message': f'📁 Working directory: {workflow_dir}',
            'timestamp': datetime.now().isoformat(),
            'type': 'info'
        }, room=socket_id)
        
        # Execute the main workflow script
        cmd = [sys.executable, 'main.py']
        
        socketio.emit('workflow_output', {
            'workflow_id': workflow_id,
            'message': f'🔧 Executing: {" ".join(cmd)}',
            'timestamp': datetime.now().isoformat(),
            'type': 'command'
        }, room=socket_id)
        
        # Start the process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # Stream output in real-time
        for line in iter(process.stdout.readline, ''):
            if line:
                line = line.strip()
                if line:  # Skip empty lines
                    # Determine message type based on content
                    msg_type = 'output'
                    if 'error' in line.lower() or 'exception' in line.lower():
                        msg_type = 'error'
                    elif 'success' in line.lower() or 'completed' in line.lower():
                        msg_type = 'success'
                    elif 'warning' in line.lower():
                        msg_type = 'warning'
                    elif line.startswith('🔧') or line.startswith('📊') or line.startswith('✅'):
                        msg_type = 'info'
                    
                    socketio.emit('workflow_output', {
                        'workflow_id': workflow_id,
                        'message': line,
                        'timestamp': datetime.now().isoformat(),
                        'type': msg_type
                    }, room=socket_id)
        
        # Wait for process to complete
        return_code = process.wait()
        
        # Emit completion message
        if return_code == 0:
            socketio.emit('workflow_completed', {
                'workflow_id': workflow_id,
                'message': f'✅ Workflow {workflow_id} completed successfully',
                'timestamp': datetime.now().isoformat(),
                'type': 'success',
                'return_code': return_code
            }, room=socket_id)
        else:
            socketio.emit('workflow_failed', {
                'workflow_id': workflow_id,
                'message': f'❌ Workflow {workflow_id} failed with return code {return_code}',
                'timestamp': datetime.now().isoformat(),
                'type': 'error',
                'return_code': return_code
            }, room=socket_id)
            
    except Exception as e:
        error_msg = f'💥 Error executing workflow {workflow_id}: {str(e)}'
        socketio.emit('workflow_error', {
            'workflow_id': workflow_id,
            'message': error_msg,
            'timestamp': datetime.now().isoformat(),
            'type': 'error',
            'error': str(e)
        }, room=socket_id)

@app.route('/api/workflows', methods=['GET'])
def workflows():
    """API endpoint to get all workflows"""
    workflows_data = get_workflows()
    return jsonify({
        'workflows': workflows_data,
        'count': len(workflows_data)
    })

@app.route('/api/workflows/<workflow_id>/run', methods=['POST'])
def run_workflow(workflow_id):
    """API endpoint to run a specific workflow"""
    try:
        # Get the socket ID from the request
        socket_id = request.json.get('socket_id')
        if not socket_id:
            return jsonify({'error': 'Socket ID required'}), 400
        
        # Start workflow execution in a separate thread
        thread = threading.Thread(
            target=execute_workflow,
            args=(workflow_id, socket_id)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'message': f'Workflow {workflow_id} execution started',
            'workflow_id': workflow_id,
            'status': 'started'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Enhanced React UI backend is running'})

@socketio.on('connect')
def handle_connect():
    """Handle WebSocket connection"""
    print(f'Client connected: {request.sid}')
    emit('connected', {'message': 'Connected to workflow backend', 'socket_id': request.sid})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection"""
    print(f'Client disconnected: {request.sid}')

@socketio.on('join_workflow')
def handle_join_workflow(data):
    """Handle joining a specific workflow room"""
    workflow_id = data.get('workflow_id')
    if workflow_id:
        socketio.emit('workflow_joined', {
            'workflow_id': workflow_id,
            'message': f'Joined workflow {workflow_id} monitoring'
        }, room=request.sid)

if __name__ == '__main__':
    print("🚀 Starting Enhanced React UI Backend with WebSocket Support...")
    print("📊 API: http://localhost:5002/api/workflows")
    print("🔌 CORS: Enabled for React frontend")
    print("📡 WebSocket: Enabled for real-time workflow monitoring")
    
    socketio.run(app, host='0.0.0.0', port=5002, debug=True)
