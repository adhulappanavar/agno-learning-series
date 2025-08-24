"""
Example 5: Workflows (Level 5)
==============================

This example demonstrates a Level 5 Agno system with complex agentic workflows:
- Multi-step workflow orchestration
- State management across workflow stages
- Conditional branching and decision making
- Error handling and recovery
- Workflow persistence and resumption
- Integration with external systems and APIs
"""

import os
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
from agno.agent import Agent
from agno.workflow import Workflow
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.calculator import CalculatorTools
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

# Load environment variables
load_dotenv()

@dataclass
class WorkflowState:
    """Represents the current state of a workflow."""
    workflow_id: str
    current_stage: str
    stage_data: Dict[str, Any]
    completed_stages: List[str]
    failed_stages: List[str]
    workflow_data: Dict[str, Any]
    created_at: str
    updated_at: str
    status: str  # 'running', 'completed', 'failed', 'paused'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorkflowState':
        """Create from dictionary."""
        return cls(**data)

class WorkflowStateManager:
    """Manages workflow state persistence and retrieval."""
    
    def __init__(self, db_file: str = "workflow_states.db"):
        self.db_file = db_file
        self.init_database()
    
    def init_database(self):
        """Initialize the SQLite database for workflow states."""
        import sqlite3
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workflow_states (
                workflow_id TEXT PRIMARY KEY,
                current_stage TEXT,
                stage_data TEXT,
                completed_stages TEXT,
                failed_stages TEXT,
                workflow_data TEXT,
                created_at TEXT,
                updated_at TEXT,
                status TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_state(self, state: WorkflowState):
        """Save workflow state to database."""
        import sqlite3
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO workflow_states 
            (workflow_id, current_stage, stage_data, completed_stages, 
             failed_stages, workflow_data, created_at, updated_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            state.workflow_id,
            state.current_stage,
            json.dumps(state.stage_data),
            json.dumps(state.completed_stages),
            json.dumps(state.failed_stages),
            json.dumps(state.workflow_data),
            state.created_at,
            state.updated_at,
            state.status
        ))
        
        conn.commit()
        conn.close()
    
    def load_state(self, workflow_id: str) -> Optional[WorkflowState]:
        """Load workflow state from database."""
        import sqlite3
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT current_stage, stage_data, completed_stages, failed_stages,
                   workflow_data, created_at, updated_at, status
            FROM workflow_states WHERE workflow_id = ?
        ''', (workflow_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return WorkflowState(
                workflow_id=workflow_id,
                current_stage=row[0],
                stage_data=json.loads(row[1]),
                completed_stages=json.loads(row[2]),
                failed_stages=json.loads(row[3]),
                workflow_data=json.loads(row[4]),
                created_at=row[5],
                updated_at=row[6],
                status=row[7]
            )
        return None
    
    def list_workflows(self) -> List[str]:
        """List all workflow IDs."""
        import sqlite3
        
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('SELECT workflow_id FROM workflow_states')
        workflow_ids = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        return workflow_ids

def create_workflow_agent():
    """Create a specialized agent for workflow orchestration."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="workflow_memories", db_file="memory_workflow.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Workflow Orchestrator",
        role="A specialized agent that orchestrates complex multi-step workflows with state management",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a workflow orchestration specialist with expertise in process management",
            "Analyze workflow requirements and break them down into manageable stages",
            "Identify dependencies between workflow stages and critical path items",
            "Handle error conditions and provide recovery strategies",
            "Manage workflow state and ensure data consistency across stages",
            "Provide clear status updates and progress tracking",
            "Use markdown formatting for workflow documentation and status reports"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="workflow_orchestrator",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_data_processing_agent():
    """Create an agent specialized in data processing workflows."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="data_memories", db_file="memory_data.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Data Processor",
        role="A data processing specialist that handles data transformation, validation, and analysis workflows",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a data processing specialist with expertise in ETL workflows",
            "Design data transformation pipelines and validation rules",
            "Handle data quality issues and provide data cleansing strategies",
            "Implement data analysis workflows and reporting",
            "Ensure data security and compliance throughout processing",
            "Optimize data processing performance and resource usage",
            "Use markdown formatting for data workflow documentation"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="data_processor",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_approval_agent():
    """Create an agent specialized in approval and decision workflows."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="approval_memories", db_file="memory_approval.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Approval Manager",
        role="An approval specialist that manages multi-level approval workflows and decision gates",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are an approval workflow specialist with expertise in decision management",
            "Design approval hierarchies and decision gate workflows",
            "Handle escalation procedures and exception management",
            "Ensure compliance with approval policies and regulations",
            "Track approval status and provide audit trails",
            "Manage approval notifications and reminders",
            "Use markdown formatting for approval workflow documentation"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="approval_manager",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

class ComplexWorkflow:
    """A complex workflow with multiple stages, state management, and error handling."""
    
    def __init__(self, workflow_id: str, state_manager: WorkflowStateManager):
        self.workflow_id = workflow_id
        self.state_manager = state_manager
        self.workflow_orchestrator = create_workflow_agent()
        self.data_processor = create_data_processing_agent()
        self.approval_manager = create_approval_agent()
        
        # Initialize or load workflow state
        self.state = self._initialize_state()
    
    def _initialize_state(self) -> WorkflowState:
        """Initialize or load existing workflow state."""
        existing_state = self.state_manager.load_state(self.workflow_id)
        
        if existing_state:
            print(f"🔄 Resuming existing workflow: {self.workflow_id}")
            return existing_state
        
        # Create new workflow state
        new_state = WorkflowState(
            workflow_id=self.workflow_id,
            current_stage="initialization",
            stage_data={},
            completed_stages=[],
            failed_stages=[],
            workflow_data={},
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            status="running"
        )
        
        self.state_manager.save_state(new_state)
        print(f"🚀 Creating new workflow: {self.workflow_id}")
        return new_state
    
    def _update_state(self, stage: str, stage_data: Dict[str, Any], status: str = "running"):
        """Update workflow state."""
        self.state.current_stage = stage
        self.state.stage_data = stage_data
        self.state.updated_at = datetime.now().isoformat()
        self.state.status = status
        
        if status == "completed":
            self.state.completed_stages.append(stage)
        elif status == "failed":
            self.state.failed_stages.append(stage)
        
        self.state_manager.save_state(self.state)
    
    def _log_stage(self, stage: str, message: str, data: Dict[str, Any] = None):
        """Log workflow stage information."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n🔄 [{timestamp}] {stage.upper()}: {message}")
        
        if data:
            print(f"📊 Stage Data: {json.dumps(data, indent=2)}")
    
    def run_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the complete workflow."""
        
        print(f"🚀 Starting Complex Workflow: {self.workflow_id}")
        print("=" * 60)
        
        try:
            # Stage 1: Workflow Analysis and Planning
            result = self._execute_planning_stage(workflow_input)
            if not result["success"]:
                return self._handle_workflow_failure("planning", result["error"])
            
            # Stage 2: Data Processing and Validation
            result = self._execute_data_processing_stage(workflow_input)
            if not result["success"]:
                return self._handle_workflow_failure("data_processing", result["error"])
            
            # Stage 3: Business Logic Execution
            result = self._execute_business_logic_stage(workflow_input)
            if not result["success"]:
                return self._handle_workflow_failure("business_logic", result["error"])
            
            # Stage 4: Approval and Decision Making
            result = self._execute_approval_stage(workflow_input)
            if not result["success"]:
                return self._handle_workflow_failure("approval", result["error"])
            
            # Stage 5: Finalization and Reporting
            result = self._execute_finalization_stage(workflow_input)
            if not result["success"]:
                return self._handle_workflow_failure("finalization", result["error"])
            
            # Workflow completed successfully
            self._update_state("finalization", result["data"], "completed")
            
            print("\n🎉 Workflow completed successfully!")
            print("=" * 60)
            
            return {
                "success": True,
                "workflow_id": self.workflow_id,
                "status": "completed",
                "completed_stages": self.state.completed_stages,
                "final_result": result["data"],
                "workflow_summary": self._generate_workflow_summary()
            }
            
        except Exception as e:
            error_msg = f"Unexpected error in workflow: {str(e)}"
            print(f"\n❌ {error_msg}")
            return self._handle_workflow_failure("unexpected", error_msg)
    
    def _execute_planning_stage(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the workflow planning stage."""
        stage = "planning"
        self._log_stage(stage, "Starting workflow analysis and planning")
        
        try:
            # Get workflow orchestration guidance
            planning_prompt = f"""
            Analyze the following workflow requirements and create a detailed execution plan:
            
            Workflow Input: {json.dumps(workflow_input, indent=2)}
            
            Please provide:
            1. Workflow stage breakdown
            2. Dependencies between stages
            3. Resource requirements
            4. Risk assessment
            5. Success criteria
            """
            
            response = self.workflow_orchestrator.run(planning_prompt)
            
            planning_data = {
                "plan": response.content,
                "input_analysis": workflow_input,
                "planning_timestamp": datetime.now().isoformat()
            }
            
            self._update_state(stage, planning_data, "completed")
            self._log_stage(stage, "Planning completed successfully", planning_data)
            
            return {"success": True, "data": planning_data}
            
        except Exception as e:
            error_msg = f"Planning stage failed: {str(e)}"
            self._log_stage(stage, f"ERROR: {error_msg}")
            return {"success": False, "error": error_msg}
    
    def _execute_data_processing_stage(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the data processing stage."""
        stage = "data_processing"
        self._log_stage(stage, "Starting data processing and validation")
        
        try:
            # Simulate data processing workflow
            data_prompt = f"""
            Design a data processing workflow for the following requirements:
            
            Workflow Input: {json.dumps(workflow_input, indent=2)}
            
            Please provide:
            1. Data transformation pipeline design
            2. Validation rules and quality checks
            3. Error handling strategies
            4. Performance optimization recommendations
            5. Data security considerations
            """
            
            response = self.data_processor.run(data_prompt)
            
            # Simulate processing time
            time.sleep(1)
            
            processing_data = {
                "pipeline_design": response.content,
                "validation_rules": ["data_format", "data_range", "data_completeness"],
                "processing_timestamp": datetime.now().isoformat(),
                "records_processed": len(workflow_input.get("data", []))
            }
            
            self._update_state(stage, processing_data, "completed")
            self._log_stage(stage, "Data processing completed successfully", processing_data)
            
            return {"success": True, "data": processing_data}
            
        except Exception as e:
            error_msg = f"Data processing stage failed: {str(e)}"
            self._log_stage(stage, f"ERROR: {error_msg}")
            return {"success": False, "error": error_msg}
    
    def _execute_business_logic_stage(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the business logic stage."""
        stage = "business_logic"
        self._log_stage(stage, "Starting business logic execution")
        
        try:
            # Execute business logic based on workflow type
            workflow_type = workflow_input.get("type", "standard")
            
            if workflow_type == "financial":
                business_logic = self._execute_financial_workflow(workflow_input)
            elif workflow_type == "approval":
                business_logic = self._execute_approval_workflow(workflow_input)
            else:
                business_logic = self._execute_standard_workflow(workflow_input)
            
            business_data = {
                "business_logic": business_logic,
                "workflow_type": workflow_type,
                "execution_timestamp": datetime.now().isoformat(),
                "business_rules_applied": len(business_logic.get("rules", []))
            }
            
            self._update_state(stage, business_data, "completed")
            self._log_stage(stage, "Business logic executed successfully", business_data)
            
            return {"success": True, "data": business_data}
            
        except Exception as e:
            error_msg = f"Business logic stage failed: {str(e)}"
            self._log_stage(stage, f"ERROR: {error_msg}")
            return {"success": False, "error": error_msg}
    
    def _execute_approval_stage(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the approval and decision making stage."""
        stage = "approval"
        self._log_stage(stage, "Starting approval and decision making")
        
        try:
            # Get approval workflow guidance
            approval_prompt = f"""
            Design an approval workflow for the following requirements:
            
            Workflow Input: {json.dumps(workflow_input, indent=2)}
            
            Please provide:
            1. Approval hierarchy design
            2. Decision gate criteria
            3. Escalation procedures
            4. Compliance requirements
            5. Audit trail design
            """
            
            response = self.approval_manager.run(approval_prompt)
            
            # Simulate approval process
            time.sleep(1)
            
            approval_data = {
                "approval_design": response.content,
                "approval_levels": ["Level 1", "Level 2", "Level 3"],
                "approval_timestamp": datetime.now().isoformat(),
                "approval_status": "approved"
            }
            
            self._update_state(stage, approval_data, "completed")
            self._log_stage(stage, "Approval completed successfully", approval_data)
            
            return {"success": True, "data": approval_data}
            
        except Exception as e:
            error_msg = f"Approval stage failed: {str(e)}"
            self._log_stage(stage, f"ERROR: {error_msg}")
            return {"success": False, "error": error_msg}
    
    def _execute_finalization_stage(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the finalization and reporting stage."""
        stage = "finalization"
        self._log_stage(stage, "Starting finalization and reporting")
        
        try:
            # Generate final workflow report
            finalization_data = {
                "workflow_summary": f"Workflow {self.workflow_id} completed successfully",
                "total_stages": len(self.state.completed_stages),
                "completion_timestamp": datetime.now().isoformat(),
                "performance_metrics": {
                    "total_duration": "5 minutes",
                    "stages_completed": len(self.state.completed_stages),
                    "success_rate": "100%"
                }
            }
            
            self._update_state(stage, finalization_data, "completed")
            self._log_stage(stage, "Finalization completed successfully", finalization_data)
            
            return {"success": True, "data": finalization_data}
            
        except Exception as e:
            error_msg = f"Finalization stage failed: {str(e)}"
            self._log_stage(stage, f"ERROR: {error_msg}")
            return {"success": False, "error": error_msg}
    
    def _execute_financial_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute financial-specific business logic."""
        return {
            "type": "financial",
            "rules": ["amount_validation", "budget_check", "approval_threshold"],
            "calculations": ["total_amount", "tax_calculation", "final_amount"],
            "compliance": ["SOX", "GAAP", "Internal Controls"]
        }
    
    def _execute_approval_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute approval-specific business logic."""
        return {
            "type": "approval",
            "rules": ["role_based_access", "delegation_rules", "escalation_criteria"],
            "workflow": ["submit", "review", "approve", "notify"],
            "compliance": ["audit_trail", "documentation", "timeline_tracking"]
        }
    
    def _execute_standard_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute standard business logic."""
        return {
            "type": "standard",
            "rules": ["business_validation", "data_integrity", "process_compliance"],
            "workflow": ["input_validation", "processing", "output_generation"],
            "quality": ["error_handling", "logging", "monitoring"]
        }
    
    def _handle_workflow_failure(self, stage: str, error: str) -> Dict[str, Any]:
        """Handle workflow failures and provide recovery options."""
        self._update_state(stage, {"error": error}, "failed")
        
        print(f"\n❌ Workflow failed at stage: {stage}")
        print(f"🔍 Error: {error}")
        print("\n🔄 Recovery Options:")
        print("1. Retry the failed stage")
        print("2. Skip to the next stage")
        print("3. Pause workflow for manual intervention")
        print("4. Rollback to previous successful stage")
        
        return {
            "success": False,
            "workflow_id": self.workflow_id,
            "status": "failed",
            "failed_stage": stage,
            "error": error,
            "recovery_options": ["retry", "skip", "pause", "rollback"]
        }
    
    def _generate_workflow_summary(self) -> str:
        """Generate a summary of the completed workflow."""
        return f"""
        # Workflow Summary
        
        **Workflow ID**: {self.workflow_id}
        **Status**: {self.state.status}
        **Created**: {self.state.created_at}
        **Completed**: {self.state.updated_at}
        
        **Stages Completed**: {len(self.state.completed_stages)}
        - {', '.join(self.state.completed_stages)}
        
        **Performance**: All stages completed successfully
        **Total Duration**: {self._calculate_duration()}
        
        **Key Achievements**:
        - Comprehensive workflow planning and analysis
        - Data processing and validation completed
        - Business logic executed successfully
        - Approval workflow completed
        - Finalization and reporting generated
        """
    
    def _calculate_duration(self) -> str:
        """Calculate the total duration of the workflow."""
        try:
            start_time = datetime.fromisoformat(self.state.created_at)
            end_time = datetime.fromisoformat(self.state.updated_at)
            duration = end_time - start_time
            return str(duration).split('.')[0]  # Remove microseconds
        except:
            return "Unknown"

def demonstrate_complex_workflows():
    """Demonstrate complex workflow capabilities."""
    
    print("🚀 Complex Workflows (Level 5) Demonstration")
    print("=" * 60)
    print("This example shows advanced workflow orchestration with state management.\n")
    
    # Initialize state manager
    state_manager = WorkflowStateManager()
    
    # Example 1: Financial Approval Workflow
    print("💰 Example 1: Financial Approval Workflow")
    print("-" * 40)
    
    financial_input = {
        "type": "financial",
        "amount": 50000,
        "department": "Engineering",
        "purpose": "Software licenses and tools",
        "data": ["license1", "license2", "tool1"],
        "approvers": ["manager", "director", "finance"]
    }
    
    financial_workflow = ComplexWorkflow("financial_001", state_manager)
    result = financial_workflow.run_workflow(financial_input)
    
    print(f"\n📊 Financial Workflow Result: {result['status']}")
    
    # Example 2: Data Processing Workflow
    print("\n📊 Example 2: Data Processing Workflow")
    print("-" * 40)
    
    data_input = {
        "type": "data_processing",
        "source": "customer_database",
        "target": "analytics_warehouse",
        "transformations": ["clean", "validate", "enrich"],
        "data": ["customer1", "customer2", "customer3"],
        "quality_threshold": 0.95
    }
    
    data_workflow = ComplexWorkflow("data_001", state_manager)
    result = data_workflow.run_workflow(data_input)
    
    print(f"\n📊 Data Workflow Result: {result['status']}")
    
    # Example 3: Standard Business Workflow
    print("\n🏢 Example 3: Standard Business Workflow")
    print("-" * 40)
    
    business_input = {
        "type": "standard",
        "process": "employee_onboarding",
        "department": "HR",
        "data": ["employee_info", "documents", "access_requests"],
        "approvals_required": ["hr_manager", "it_manager"]
    }
    
    business_workflow = ComplexWorkflow("business_001", state_manager)
    result = business_workflow.run_workflow(business_input)
    
    print(f"\n📊 Business Workflow Result: {result['status']}")
    
    # Show workflow states
    print("\n📋 Workflow States Summary")
    print("=" * 40)
    
    workflow_ids = state_manager.list_workflows()
    for workflow_id in workflow_ids:
        state = state_manager.load_state(workflow_id)
        if state:
            print(f"🆔 {workflow_id}: {state.status} (Stage: {state.current_stage})")
    
    print("\n🎉 Complex workflows demonstration completed!")
    print("\n💡 Key Features Demonstrated:")
    print("   - Multi-stage workflow orchestration")
    print("   - State persistence and recovery")
    print("   - Error handling and recovery options")
    print("   - Specialized agents for different workflow types")
    print("   - Conditional branching and decision making")
    print("\n💡 Try running 'workflow_test.py' to see more workflow scenarios!")

def main():
    """Main function to run the complex workflows demonstration."""
    demonstrate_complex_workflows()

if __name__ == "__main__":
    main()
