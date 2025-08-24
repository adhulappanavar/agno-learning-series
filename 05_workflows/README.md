# Example 5: Workflows (Level 5) - Complex agentic workflows with state management

This example demonstrates **Level 5** of the Agno framework: **Agentic Workflows** - complex multi-step workflows with state management, persistence, and error handling.

## 🎯 What You'll Learn

- **Workflow Orchestration**: Create complex multi-step workflows
- **State Management**: Persist workflow state across sessions
- **Error Handling**: Graceful failure and recovery
- **Agent Coordination**: Multiple agents working together in sequence
- **Real-time Monitoring**: Track workflow progress and status

## 🚀 Features

### **Core Workflow System**
- **Custom Workflow State**: Persistent state management using SQLite
- **Multi-stage Execution**: Business logic → Approval → Finalization
- **Error Recovery**: Automatic retry and fallback mechanisms
- **Progress Tracking**: Real-time status updates and monitoring

### **Agent Capabilities**
- **Business Logic Agent**: Analyzes business requirements and creates plans
- **Approval Agent**: Reviews and approves business decisions
- **Finalization Agent**: Executes approved plans and generates reports

### **State Persistence**
- **SQLite Database**: `workflow_states.db` stores all workflow data
- **Session Recovery**: Workflows can be resumed after interruptions
- **Audit Trail**: Complete history of workflow execution

## 📁 Project Structure

```
05_workflows/
├── main.py                 # Main workflow execution script
├── workflow_manager.py     # Workflow orchestration and state management
├── agents/                 # Workflow agents
│   ├── business_agent.py   # Business logic analysis
│   ├── approval_agent.py   # Decision approval
│   └── finalization_agent.py # Plan execution
├── workflow_states.db      # SQLite database for state persistence
├── react_ui/              # Simple React web interface
│   ├── app.py             # Flask backend API
│   ├── src/               # React frontend components
│   └── package.json       # Node.js dependencies
└── README.md              # This file
```

## 🛠️ Setup & Installation

### **1. Install Dependencies**
```bash
pip install agno openai python-dotenv
```

### **2. Environment Configuration**
Create a `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### **3. Run the Workflow**
```bash
python main.py
```

## 🌐 Web Interface

### **Simple React UI**
We've created a clean, simple React-based web interface to visualize workflows:

#### **Start the Backend**
```bash
cd react_ui
python app.py
```
- **Port**: 5001
- **API**: http://localhost:5001/api/workflows

#### **Start the Frontend**
```bash
cd react_ui
npm start
```
- **Port**: 3000
- **URL**: http://localhost:3000

### **Features**
- **Clean Table Display**: Simple workflow table with status badges
- **Real-time Data**: Fetches workflow data from Python backend
- **Status Indicators**: Color-coded status badges for different states
- **Responsive Design**: Works on desktop and mobile devices

## 🔄 Workflow Execution

### **Workflow Stages**

1. **Business Logic** (`business_logic`)
   - Analyzes business requirements
   - Creates strategic plans
   - Generates business insights

2. **Approval** (`approval`)
   - Reviews business plans
   - Makes approval decisions
   - Provides feedback and suggestions

3. **Finalization** (`finalization`)
   - Executes approved plans
   - Generates final reports
   - Completes workflow

### **Status Tracking**
- **Pending**: Workflow created, waiting to start
- **Running**: Currently executing a stage
- **Completed**: All stages finished successfully
- **Failed**: Error occurred, needs attention

## 📊 Database Schema

The `workflow_states.db` contains:

```sql
CREATE TABLE workflow_states (
    id TEXT PRIMARY KEY,
    stage TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stage_data TEXT
);
```

## 🎮 Usage Examples

### **Basic Workflow Execution**
```python
from workflow_manager import WorkflowManager

# Create workflow manager
manager = WorkflowManager()

# Execute workflow
workflow_id = manager.execute_workflow("business_analysis")
print(f"Workflow {workflow_id} started")
```

### **Monitor Workflow Status**
```python
# Check workflow status
status = manager.get_workflow_status(workflow_id)
print(f"Status: {status}")

# Get workflow details
details = manager.get_workflow_details(workflow_id)
print(f"Current stage: {details['stage']}")
```

## 🔍 Monitoring & Debugging

### **Real-time Status**
- Monitor workflow progress in real-time
- View current stage and status
- Track execution time and performance

### **Error Handling**
- Automatic retry mechanisms
- Detailed error logging
- Graceful failure recovery

### **Web Interface**
- View all workflows in a clean table
- Monitor status changes
- Refresh data in real-time

## 🚀 Next Steps

This example demonstrates the foundation for building complex agentic workflows. You can extend it by:

1. **Adding More Stages**: Implement additional workflow stages
2. **Enhanced Error Handling**: Add more sophisticated retry logic
3. **Workflow Templates**: Create reusable workflow patterns
4. **Advanced Monitoring**: Add performance metrics and analytics
5. **Integration**: Connect with external systems and APIs

## 📚 Key Concepts

- **Workflow Orchestration**: Coordinating multiple agents in sequence
- **State Persistence**: Maintaining workflow state across sessions
- **Error Recovery**: Handling failures gracefully
- **Real-time Monitoring**: Tracking progress and performance
- **Agent Coordination**: Managing agent interactions and data flow

## 🎯 Success Criteria

✅ **Workflow Creation**: Successfully create multi-stage workflows  
✅ **State Persistence**: Maintain state across sessions  
✅ **Error Handling**: Gracefully handle and recover from failures  
✅ **Real-time Monitoring**: Track progress and status updates  
✅ **Web Interface**: View workflows in a clean, simple table format  

---

**Level 5 Complete!** 🎉 You've now mastered complex agentic workflows with state management, persistence, and real-time monitoring. This represents the highest level of sophistication in the Agno framework!
