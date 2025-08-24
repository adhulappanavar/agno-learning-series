#!/usr/bin/env python3
"""
Workflow Visualization Web UI
============================

Flask-based web application for visualizing workflows, metrics, and error handling.
Phase 1: Foundation - Basic Flask app setup with routing and navigation.
"""

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
import os
import sqlite3
from datetime import datetime
import json

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'workflow-viz-secret-key-2024'
app.config['DEBUG'] = True

# Initialize SocketIO for real-time updates
socketio = SocketIO(app, cors_allowed_origins="*")

# Database configuration
DATABASE_PATH = '../workflow_states.db'

def get_db_connection():
    """Create a database connection."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.OperationalError:
        # If database doesn't exist, return None
        return None

def get_workflow_stats():
    """Get basic workflow statistics from database."""
    conn = get_db_connection()
    if conn is None:
        return {
            'total_workflows': 0,
            'active_workflows': 0,
            'completed_workflows': 0,
            'failed_workflows': 0,
            'recent_workflows': []
        }
    
    try:
        cursor = conn.cursor()
        
        # Get total workflows
        cursor.execute("SELECT COUNT(*) FROM workflow_states")
        total_workflows = cursor.fetchone()[0]
        
        # Get active workflows (not completed)
        cursor.execute("SELECT COUNT(*) FROM workflow_states WHERE status != 'completed'")
        active_workflows = cursor.fetchone()[0]
        
        # Get completed workflows
        cursor.execute("SELECT COUNT(*) FROM workflow_states WHERE status = 'completed'")
        completed_workflows = cursor.fetchone()[0]
        
        # Get failed workflows
        cursor.execute("SELECT COUNT(*) FROM workflow_states WHERE status = 'failed'")
        failed_workflows = cursor.fetchone()[0]
        
        # Get recent workflows
        cursor.execute("""
            SELECT workflow_id, status, current_stage, created_at, updated_at
            FROM workflow_states 
            ORDER BY updated_at DESC 
            LIMIT 5
        """)
        recent_workflows = []
        for row in cursor.fetchall():
            recent_workflows.append({
                'id': row['workflow_id'],
                'type': 'Workflow',  # Default type since it's not in schema
                'status': row['status'],
                'stage': row['current_stage'],
                'created': row['created_at'],
                'updated': row['updated_at']
            })
        
        return {
            'total_workflows': total_workflows,
            'active_workflows': active_workflows,
            'completed_workflows': completed_workflows,
            'failed_workflows': failed_workflows,
            'recent_workflows': recent_workflows
        }
        
    except Exception as e:
        print(f"Database error: {e}")
        return {
            'total_workflows': 0,
            'active_workflows': 0,
            'completed_workflows': 0,
            'failed_workflows': 0,
            'recent_workflows': []
        }
    finally:
        conn.close()

# Route definitions
@app.route('/')
def dashboard():
    """Main dashboard page."""
    stats = get_workflow_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/workflow')
def workflow():
    """Workflow visualization page."""
    return render_template('workflow.html')

@app.route('/metrics')
def metrics():
    """Metrics dashboard page."""
    return render_template('metrics.html')

@app.route('/errors')
def errors():
    """Error handling dashboard page."""
    return render_template('errors.html')

@app.route('/api/stats')
def api_stats():
    """API endpoint for workflow statistics."""
    stats = get_workflow_stats()
    return jsonify(stats)

@app.route('/api/workflows')
def api_workflows():
    """API endpoint for workflow data."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'workflows': []})
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT workflow_id, status, current_stage, 
                   stage_data, created_at, updated_at
            FROM workflow_states 
            ORDER BY updated_at DESC
        """)
        
        workflows = []
        for row in cursor.fetchall():
            workflows.append({
                'id': row['workflow_id'],
                'type': 'Workflow',  # Default type since it's not in schema
                'status': row['status'],
                'stage': row['current_stage'],
                'stage_data': row['stage_data'],
                'created': row['created_at'],
                'updated': row['updated_at']
            })
        
        return jsonify({'workflows': workflows})
        
    except Exception as e:
        return jsonify({'error': str(e), 'workflows': []})
    finally:
        conn.close()

# SocketIO events for real-time updates
@socketio.on('connect')
def handle_connect():
    """Handle client connection."""
    print('Client connected')
    emit('status', {'data': 'Connected to Workflow Visualization Server'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection."""
    print('Client disconnected')

@socketio.on('request_update')
def handle_update_request():
    """Handle update requests from clients."""
    stats = get_workflow_stats()
    emit('stats_update', stats)

@socketio.on('get_workflow_details')
def handle_workflow_details(data):
    """Get detailed information about a specific workflow."""
    workflow_id = data.get('workflow_id')
    if not workflow_id:
        emit('error', {'message': 'Workflow ID required'})
        return
    
    conn = get_db_connection()
    if conn is None:
        emit('error', {'message': 'Database connection failed'})
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT workflow_id, current_stage, stage_data, completed_stages, 
                   failed_stages, workflow_data, created_at, updated_at, status
            FROM workflow_states 
            WHERE workflow_id = ?
        """, (workflow_id,))
        
        row = cursor.fetchone()
        if row:
            workflow_details = {
                'id': row['workflow_id'],
                'current_stage': row['current_stage'],
                'stage_data': row['stage_data'],
                'completed_stages': row['completed_stages'],
                'failed_stages': row['failed_stages'],
                'workflow_data': row['workflow_data'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'status': row['status']
            }
            emit('workflow_details', workflow_details)
        else:
            emit('error', {'message': 'Workflow not found'})
            
    except Exception as e:
        emit('error', {'message': f'Database error: {str(e)}'})
    finally:
        conn.close()

@socketio.on('execute_workflow')
def handle_workflow_execution(data):
    """Handle workflow execution commands."""
    workflow_id = data.get('workflow_id')
    action = data.get('action')  # 'play', 'pause', 'stop', 'step'
    
    if not workflow_id or not action:
        emit('error', {'message': 'Workflow ID and action required'})
        return
    
    # For Phase 2, we'll simulate workflow execution
    # In a real implementation, this would control actual workflow execution
    execution_status = {
        'workflow_id': workflow_id,
        'action': action,
        'status': 'executing',
        'timestamp': datetime.now().isoformat(),
        'message': f'Workflow {action} command received'
    }
    
    emit('execution_update', execution_status)
    
    # Simulate execution progress
    if action == 'play':
        socketio.emit('workflow_progress', {
            'workflow_id': workflow_id,
            'stage': 'executing',
            'progress': 50,
            'message': 'Workflow execution in progress'
        })

@socketio.on('get_workflow_stages')
def handle_workflow_stages(data):
    """Get detailed stage information for a workflow."""
    workflow_id = data.get('workflow_id')
    if not workflow_id:
        emit('error', {'message': 'Workflow ID required'})
        return
    
    # Define the standard 5-stage workflow structure
    workflow_stages = [
        {
            'stage_id': 'planning',
            'name': 'Planning',
            'description': 'Workflow analysis, timeline planning, resource allocation',
            'status': 'pending',
            'order': 1
        },
        {
            'stage_id': 'data_processing',
            'name': 'Data Processing',
            'description': 'Data extraction, validation, quality checks',
            'status': 'pending',
            'order': 2
        },
        {
            'stage_id': 'business_logic',
            'name': 'Business Logic',
            'description': 'Business validation, data integrity, compliance',
            'status': 'pending',
            'order': 3
        },
        {
            'stage_id': 'approval',
            'name': 'Approval',
            'description': 'Manager approval chain and decision gates',
            'status': 'pending',
            'order': 4
        },
        {
            'stage_id': 'finalization',
            'name': 'Finalization',
            'description': 'Final report, performance metrics, completion',
            'status': 'pending',
            'order': 5
        }
    ]
    
    # Get actual workflow data to determine stage status
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT current_stage, completed_stages, failed_stages, status
                FROM workflow_states 
                WHERE workflow_id = ?
            """, (workflow_id,))
            
            row = cursor.fetchone()
            if row:
                current_stage = row['current_stage']
                completed_stages = row['completed_stages'] or '[]'
                failed_stages = row['failed_stages'] or '[]'
                workflow_status = row['status']
                
                # Parse completed and failed stages
                try:
                    completed = eval(completed_stages) if completed_stages else []
                    failed = eval(failed_stages) if failed_stages else []
                except:
                    completed = []
                    failed = []
                
                # Update stage statuses
                for stage in workflow_stages:
                    if stage['stage_id'] in completed:
                        stage['status'] = 'completed'
                    elif stage['stage_id'] in failed:
                        stage['status'] = 'failed'
                    elif stage['stage_id'] == current_stage:
                        stage['status'] = 'running'
                    else:
                        stage['status'] = 'pending'
                
                # Add workflow metadata
                workflow_info = {
                    'workflow_id': workflow_id,
                    'stages': workflow_stages,
                    'current_stage': current_stage,
                    'overall_status': workflow_status,
                    'completed_count': len(completed),
                    'failed_count': len(failed),
                    'total_stages': len(workflow_stages)
                }
                
                emit('workflow_stages', workflow_info)
            else:
                emit('error', {'message': 'Workflow not found'})
                
        except Exception as e:
            emit('error', {'message': f'Database error: {str(e)}'})
        finally:
            conn.close()
    else:
        # Return default stages if database not available
        workflow_info = {
            'workflow_id': workflow_id,
            'stages': workflow_stages,
            'current_stage': 'planning',
            'overall_status': 'unknown',
            'completed_count': 0,
            'failed_count': 0,
            'total_stages': len(workflow_stages)
        }
        emit('workflow_stages', workflow_info)

if __name__ == '__main__':
    print("🚀 Starting Workflow Visualization Web UI...")
    print("📊 Dashboard: http://localhost:5000")
    print("🔄 Workflows: http://localhost:5000/workflow")
    print("📈 Metrics: http://localhost:5000/metrics")
    print("🚨 Errors: http://localhost:5000/errors")
    print("🔌 WebSocket: Real-time updates enabled")
    
    # Run the application
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
