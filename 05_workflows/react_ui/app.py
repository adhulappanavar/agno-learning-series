#!/usr/bin/env python3
"""
Simple Flask backend for React UI
Just serves workflow data in JSON format
"""

from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

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
            SELECT id, stage, status, created_at, updated_at, stage_data
            FROM workflow_states
            ORDER BY created_at DESC
        """)
        
        workflows = []
        for row in cursor.fetchall():
            workflow = {
                'id': row[0],
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

@app.route('/api/workflows', methods=['GET'])
def workflows():
    """API endpoint to get all workflows"""
    workflows_data = get_workflows()
    return jsonify({
        'workflows': workflows_data,
        'count': len(workflows_data)
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'React UI backend is running'})

if __name__ == '__main__':
    print("🚀 Starting Simple React UI Backend...")
    print("📊 API: http://localhost:5002/api/workflows")
    print("🔌 CORS: Enabled for React frontend")
    
    app.run(host='0.0.0.0', port=5002, debug=True)
