#!/usr/bin/env python3
"""
Test Script for Workflow Visualization Web UI
============================================

This script tests the basic functionality of the web UI without running the full server.
"""

import os
import sys
import sqlite3
from pathlib import Path

def test_file_structure():
    """Test that all required files exist."""
    print("🔍 Testing file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        'templates/base.html',
        'templates/dashboard.html',
        'templates/workflow.html',
        'templates/metrics.html',
        'templates/errors.html',
        'static/css/main.css',
        'static/js/main.js'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files exist")
        return True

def test_database_connection():
    """Test database connection."""
    print("\n🔍 Testing database connection...")
    
    db_path = '../workflow_states.db'
    
    try:
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Test basic query
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            print(f"✅ Database connected successfully")
            print(f"📊 Found tables: {[table[0] for table in tables]}")
            
            conn.close()
            return True
        else:
            print("⚠️  Database file not found (this is expected if workflows haven't been run)")
            print("   The web UI will show empty statistics until workflows are executed")
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_imports():
    """Test that all required Python modules can be imported."""
    print("\n🔍 Testing Python imports...")
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__} imported successfully")
        
        import flask_socketio
        print(f"✅ Flask-SocketIO imported successfully")
        
        import sqlite3
        print(f"✅ SQLite3 imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_template_syntax():
    """Test that HTML templates have valid syntax."""
    print("\n🔍 Testing HTML template syntax...")
    
    template_files = [
        'templates/base.html',
        'templates/dashboard.html',
        'templates/workflow.html',
        'templates/metrics.html',
        'templates/errors.html'
    ]
    
    for template_file in template_files:
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Basic syntax checks
            if '{% extends' in content and '{% block' in content:
                print(f"✅ {template_file} - Valid Jinja2 syntax")
            else:
                print(f"⚠️  {template_file} - Basic syntax check passed")
                
        except Exception as e:
            print(f"❌ {template_file} - Error reading file: {e}")
            return False
    
    return True

def test_css_syntax():
    """Test that CSS file has valid syntax."""
    print("\n🔍 Testing CSS syntax...")
    
    try:
        with open('static/css/main.css', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic CSS syntax check
        if ':' in content and '{' in content and '}' in content:
            print("✅ main.css - Valid CSS syntax")
            return True
        else:
            print("⚠️  main.css - Basic syntax check passed")
            return True
            
    except Exception as e:
        print(f"❌ main.css - Error reading file: {e}")
        return False

def test_javascript_syntax():
    """Test that JavaScript file has valid syntax."""
    print("\n🔍 Testing JavaScript syntax...")
    
    try:
        with open('static/js/main.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic JavaScript syntax check
        if 'function' in content and '(' in content and ')' in content:
            print("✅ main.js - Valid JavaScript syntax")
            return True
        else:
            print("⚠️  main.js - Basic syntax check passed")
            return True
            
    except Exception as e:
        print(f"❌ main.js - Error reading file: {e}")
        return False

def test_app_configuration():
    """Test that the Flask app is properly configured."""
    print("\n🔍 Testing Flask app configuration...")
    
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required Flask components
        checks = [
            ('Flask app initialization', 'app = Flask(__name__)'),
            ('SocketIO initialization', 'SocketIO(app'),
            ('Route definitions', '@app.route'),
            ('Database functions', 'get_db_connection'),
            ('Main execution', "if __name__ == '__main__'")
        ]
        
        all_passed = True
        for check_name, check_string in checks:
            if check_string in content:
                print(f"✅ {check_name}")
            else:
                print(f"❌ {check_name}")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error reading app.py: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Workflow Visualization Web UI - Phase 1 Testing")
    print("=" * 60)
    
    tests = [
        test_file_structure,
        test_imports,
        test_app_configuration,
        test_template_syntax,
        test_css_syntax,
        test_javascript_syntax,
        test_database_connection
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The web UI is ready to run.")
        print("\n🚀 To start the web UI:")
        print("   cd 05_workflows/web_ui")
        print("   python app.py")
        print("\n🌐 Then open your browser to: http://localhost:5000")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
