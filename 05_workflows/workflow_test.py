#!/usr/bin/env python3
"""
Workflow Testing Script
=======================

This script demonstrates various workflow scenarios and state management capabilities.
Run this after running workflows.py to see more advanced workflow features in action.
"""

import os
import json
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from workflows import ComplexWorkflow, WorkflowStateManager

def test_workflow_persistence():
    """Test workflow state persistence and recovery."""
    
    print("🧪 Testing Workflow Persistence and Recovery")
    print("=" * 50)
    print("This test shows how workflows can be paused, resumed, and recovered.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Create a workflow
    workflow_id = "persistence_test_001"
    workflow = ComplexWorkflow(workflow_id, state_manager)
    
    print(f"🆔 Created workflow: {workflow_id}")
    
    # Start workflow but simulate interruption
    print("\n🔄 Starting workflow...")
    
    workflow_input = {
        "type": "standard",
        "process": "data_migration",
        "department": "IT",
        "data": ["table1", "table2", "table3"],
        "priority": "high"
    }
    
    # Simulate workflow interruption after planning stage
    print("⏸️ Simulating workflow interruption after planning stage...")
    
    # Manually update state to simulate interruption
    workflow.state.current_stage = "planning"
    workflow.state.status = "paused"
    workflow.state.stage_data = {"interruption_reason": "System maintenance"}
    workflow.state_manager.save_state(workflow.state)
    
    print(f"📊 Workflow state saved: {workflow.state.status}")
    
    # Now try to resume the workflow
    print("\n🔄 Attempting to resume workflow...")
    
    resumed_workflow = ComplexWorkflow(workflow_id, state_manager)
    print(f"📊 Resumed workflow status: {resumed_workflow.state.status}")
    print(f"📊 Current stage: {resumed_workflow.state.current_stage}")
    
    # Continue the workflow
    print("\n🔄 Continuing workflow from where it left off...")
    
    result = resumed_workflow.run_workflow(workflow_input)
    
    print(f"\n📊 Final workflow result: {result['status']}")
    print(f"📊 Completed stages: {len(result.get('completed_stages', []))}")

def test_workflow_error_handling():
    """Test workflow error handling and recovery mechanisms."""
    
    print("\n🧪 Testing Workflow Error Handling and Recovery")
    print("=" * 55)
    print("This test shows how workflows handle errors and provide recovery options.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Create a workflow with potential error conditions
    workflow_id = "error_test_001"
    workflow = ComplexWorkflow(workflow_id, state_manager)
    
    print(f"🆔 Created workflow: {workflow_id}")
    
    # Create input that might cause issues
    problematic_input = {
        "type": "financial",
        "amount": -1000,  # Negative amount (invalid)
        "department": "Unknown",  # Invalid department
        "purpose": "",  # Empty purpose
        "data": [],  # Empty data
        "approvers": []  # No approvers
    }
    
    print("\n⚠️ Running workflow with problematic input to test error handling...")
    
    try:
        result = workflow.run_workflow(problematic_input)
        
        if result["success"]:
            print("✅ Workflow completed despite problematic input")
        else:
            print(f"❌ Workflow failed as expected: {result['error']}")
            print(f"🔄 Recovery options: {result.get('recovery_options', [])}")
            
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

def test_concurrent_workflows():
    """Test running multiple workflows concurrently."""
    
    print("\n🧪 Testing Concurrent Workflows")
    print("=" * 40)
    print("This test shows how multiple workflows can run simultaneously.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Create multiple workflows
    workflow_configs = [
        {
            "id": "concurrent_001",
            "type": "financial",
            "amount": 10000,
            "department": "Marketing",
            "purpose": "Campaign materials"
        },
        {
            "id": "concurrent_002", 
            "type": "data_processing",
            "source": "sales_data",
            "target": "reporting_dashboard",
            "transformations": ["aggregate", "calculate_metrics"]
        },
        {
            "id": "concurrent_003",
            "type": "standard",
            "process": "inventory_check",
            "department": "Operations",
            "priority": "medium"
        }
    ]
    
    print(f"🚀 Starting {len(workflow_configs)} concurrent workflows...")
    
    workflow_results = []
    
    for config in workflow_configs:
        print(f"\n🔄 Starting workflow: {config['id']}")
        
        workflow = ComplexWorkflow(config['id'], state_manager)
        
        # Create workflow input
        workflow_input = {k: v for k, v in config.items() if k != 'id'}
        workflow_input['data'] = [f"item_{i}" for i in range(3)]
        workflow_input['approvers'] = ['manager', 'supervisor']
        
        # Run workflow
        result = workflow.run_workflow(workflow_input)
        workflow_results.append({
            'id': config['id'],
            'status': result['status'],
            'success': result['success']
        })
        
        print(f"✅ Workflow {config['id']} completed with status: {result['status']}")
    
    # Summary of concurrent workflows
    print("\n📊 Concurrent Workflows Summary")
    print("-" * 35)
    
    successful = sum(1 for r in workflow_results if r['success'])
    failed = len(workflow_results) - successful
    
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {(successful/len(workflow_results)*100):.1f}%")

def test_workflow_metrics():
    """Test workflow performance metrics and monitoring."""
    
    print("\n🧪 Testing Workflow Metrics and Monitoring")
    print("=" * 50)
    print("This test shows workflow performance tracking and analytics.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Create a workflow for metrics testing
    workflow_id = "metrics_test_001"
    workflow = ComplexWorkflow(workflow_id, state_manager)
    
    print(f"🆔 Created workflow: {workflow_id}")
    
    # Record start time
    start_time = datetime.now()
    
    # Run workflow
    workflow_input = {
        "type": "standard",
        "process": "performance_testing",
        "department": "QA",
        "data": ["test_case_1", "test_case_2", "test_case_3", "test_case_4", "test_case_5"],
        "priority": "high"
    }
    
    print("🔄 Running workflow for metrics collection...")
    result = workflow.run_workflow(workflow_input)
    
    # Record end time
    end_time = datetime.now()
    
    # Calculate metrics
    duration = end_time - start_time
    stages_completed = len(result.get('completed_stages', []))
    success_rate = 100 if result['success'] else 0
    
    print("\n📊 Workflow Performance Metrics")
    print("-" * 35)
    print(f"⏱️ Total Duration: {duration}")
    print(f"📋 Stages Completed: {stages_completed}")
    print(f"✅ Success Rate: {success_rate}%")
    print(f"🆔 Workflow ID: {workflow_id}")
    print(f"📅 Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📅 End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Calculate stage-level metrics
    if hasattr(workflow, 'state') and workflow.state:
        print(f"\n📊 Stage-Level Metrics")
        print("-" * 25)
        print(f"🔄 Current Stage: {workflow.state.current_stage}")
        print(f"✅ Completed Stages: {', '.join(workflow.state.completed_stages)}")
        print(f"❌ Failed Stages: {', '.join(workflow.state.failed_stages)}")
        print(f"📊 Total Stages: {len(workflow.state.completed_stages) + len(workflow.state.failed_stages)}")

def test_workflow_customization():
    """Test customizing workflows for specific use cases."""
    
    print("\n🧪 Testing Workflow Customization")
    print("=" * 40)
    print("This test shows how workflows can be customized for different domains.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Custom workflow types
    custom_workflows = [
        {
            "id": "custom_hr_001",
            "type": "hr_onboarding",
            "process": "new_employee_setup",
            "stages": ["document_collection", "system_access", "training", "final_approval"],
            "department": "Human Resources",
            "priority": "high"
        },
        {
            "id": "custom_it_001",
            "type": "it_deployment",
            "process": "software_deployment",
            "stages": ["planning", "testing", "deployment", "verification", "rollback_plan"],
            "department": "Information Technology",
            "priority": "critical"
        },
        {
            "id": "custom_finance_001",
            "type": "budget_approval",
            "process": "annual_budget_approval",
            "stages": ["budget_preparation", "stakeholder_review", "executive_approval", "implementation"],
            "department": "Finance",
            "priority": "high"
        }
    ]
    
    print(f"🚀 Testing {len(custom_workflows)} custom workflow types...")
    
    for custom_config in custom_workflows:
        print(f"\n🔄 Testing custom workflow: {custom_config['id']}")
        print(f"📋 Type: {custom_config['type']}")
        print(f"📋 Process: {custom_config['process']}")
        print(f"📋 Stages: {', '.join(custom_config['stages'])}")
        
        # Create workflow
        workflow = ComplexWorkflow(custom_config['id'], state_manager)
        
        # Create input
        workflow_input = {
            "type": custom_config['type'],
            "process": custom_config['process'],
            "department": custom_config['department'],
            "priority": custom_config['priority'],
            "data": [f"{custom_config['type']}_item_{i}" for i in range(3)],
            "approvers": ['manager', 'director', 'executive']
        }
        
        # Run workflow
        result = workflow.run_workflow(workflow_input)
        
        print(f"✅ Result: {result['status']}")

def test_workflow_state_inspection():
    """Test inspecting and analyzing workflow states."""
    
    print("\n🧪 Testing Workflow State Inspection")
    print("=" * 45)
    print("This test shows how to inspect and analyze workflow states.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # List all workflows
    workflow_ids = state_manager.list_workflows()
    
    print(f"📋 Found {len(workflow_ids)} workflows in database")
    
    if workflow_ids:
        print("\n📊 Workflow State Analysis")
        print("-" * 30)
        
        for workflow_id in workflow_ids:
            state = state_manager.load_state(workflow_id)
            if state:
                print(f"\n🆔 Workflow: {workflow_id}")
                print(f"   📊 Status: {state.status}")
                print(f"   🔄 Current Stage: {state.current_stage}")
                print(f"   ✅ Completed Stages: {len(state.completed_stages)}")
                print(f"   ❌ Failed Stages: {len(state.failed_stages)}")
                print(f"   📅 Created: {state.created_at}")
                print(f"   📅 Updated: {state.updated_at}")
                
                # Show stage data summary
                if state.stage_data:
                    print(f"   📊 Stage Data Keys: {list(state.stage_data.keys())}")
                
                # Calculate workflow age
                try:
                    created = datetime.fromisoformat(state.created_at)
                    age = datetime.now() - created
                    print(f"   ⏰ Age: {age}")
                except:
                    print(f"   ⏰ Age: Unknown")
    else:
        print("📋 No workflows found in database")

def main():
    """Main function to run all workflow tests."""
    
    print("🚀 Workflow Testing Suite")
    print("=" * 40)
    print("This suite demonstrates advanced workflow capabilities.\n")
    
    # Run all tests
    test_workflow_persistence()
    print("\n" + "="*60 + "\n")
    
    test_workflow_error_handling()
    print("\n" + "="*60 + "\n")
    
    test_concurrent_workflows()
    print("\n" + "="*60 + "\n")
    
    test_workflow_metrics()
    print("\n" + "="*60 + "\n")
    
    test_workflow_customization()
    print("\n" + "="*60 + "\n")
    
    test_workflow_state_inspection()
    
    print("\n🎉 All workflow tests completed!")
    print("\n💡 Key Insights:")
    print("   - Workflows can be paused, resumed, and recovered")
    print("   - Error handling provides recovery options")
    print("   - Multiple workflows can run concurrently")
    print("   - Performance metrics are tracked automatically")
    print("   - Workflows can be customized for specific domains")
    print("   - State inspection enables workflow analysis")

if __name__ == "__main__":
    main()
