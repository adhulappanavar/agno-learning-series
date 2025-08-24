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
            SELECT workflow_id, workflow_type, status, current_stage, created_at, updated_at
            FROM workflow_states 
            ORDER BY updated_at DESC 
            LIMIT 5
        """)
        recent_workflows = []
        for row in cursor.fetchall():
            recent_workflows.append({
                'id': row['workflow_id'],
                'type': row['workflow_type'],
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
            SELECT workflow_id, workflow_type, status, current_stage, 
                   stage_data, created_at, updated_at
            FROM workflow_states 
            ORDER BY updated_at DESC
        """)
        
        workflows = []
        for row in cursor.fetchall():
            workflows.append({
                'id': row['workflow_id'],
                'type': row['workflow_type'],
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

if __name__ == '__main__':
    print("🚀 Starting Workflow Visualization Web UI...")
    print("📊 Dashboard: http://localhost:5000")
    print("🔄 Workflows: http://localhost:5000/workflow")
    print("📈 Metrics: http://localhost:5000/metrics")
    print("🚨 Errors: http://localhost:5000/errors")
    print("🔌 WebSocket: Real-time updates enabled")
    
    # Run the application
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
