# Setup Guide for Workflows Example

This guide will help you set up and run the Workflows (Level 5) example.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Basic understanding of Python
- Familiarity with previous Agno examples (Levels 1-4)

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the `05_workflows` directory:

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 3. Verify Installation

Check that all packages are installed correctly:

```bash
python -c "import agno; print('Agno version:', agno.__version__)"
```

## Running the Example

### Basic Workflows Demonstration

```bash
python workflows.py
```

This will:
- Create complex workflows with multiple stages
- Demonstrate state management and persistence
- Show error handling and recovery mechanisms
- Run three different workflow types (financial, data processing, business)

### Extended Workflow Testing

```bash
python workflow_test.py
```

This comprehensive test suite will:
- Test workflow persistence and recovery
- Demonstrate error handling and recovery
- Show concurrent workflow execution
- Test performance metrics and monitoring
- Demonstrate workflow customization
- Show state inspection and analysis

## What You'll See

### Workflow Structure
- **5-Stage Workflow**: Planning → Data Processing → Business Logic → Approval → Finalization
- **State Management**: Persistent workflow states with SQLite database
- **Error Handling**: Comprehensive error handling with recovery options
- **Specialized Agents**: Workflow Orchestrator, Data Processor, Approval Manager

### Key Features Demonstrated
- **Multi-stage orchestration** with conditional branching
- **State persistence** across workflow stages
- **Error handling and recovery** mechanisms
- **Concurrent workflow execution** capabilities
- **Performance monitoring** and metrics collection
- **Workflow customization** for different domains

## Workflow Types

### 1. Financial Approval Workflow
- **Purpose**: Handle financial requests and approvals
- **Stages**: Budget validation, approval hierarchy, compliance checks
- **Output**: Approved/rejected financial requests with audit trail

### 2. Data Processing Workflow
- **Purpose**: Transform and validate data
- **Stages**: Data extraction, transformation, validation, loading
- **Output**: Processed data with quality metrics

### 3. Standard Business Workflow
- **Purpose**: Handle general business processes
- **Stages**: Input validation, processing, output generation
- **Output**: Completed business processes with documentation

## Customization

### Adding New Workflow Types

You can create new workflow types by extending the `ComplexWorkflow` class:

```python
def _execute_custom_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
    """Execute custom-specific business logic."""
    return {
        "type": "custom",
        "rules": ["custom_validation", "custom_processing"],
        "workflow": ["custom_stage1", "custom_stage2"],
        "compliance": ["custom_standards", "custom_requirements"]
    }
```

### Modifying Workflow Stages

Update the workflow execution logic in the `run_workflow` method:

```python
def run_workflow(self, workflow_input: Dict[str, Any]) -> Dict[str, Any]:
    # Add your custom stages here
    result = self._execute_custom_stage(workflow_input)
    if not result["success"]:
        return self._handle_workflow_failure("custom_stage", result["error"])
    
    # Continue with existing stages...
```

### Custom State Management

Extend the `WorkflowState` class for additional state information:

```python
@dataclass
class CustomWorkflowState(WorkflowState):
    custom_field: str
    additional_data: Dict[str, Any]
```

## Advanced Features

### Workflow Persistence
- **Automatic State Saving**: Workflow state is automatically saved after each stage
- **Resume Capability**: Workflows can be resumed from where they left off
- **State Recovery**: Failed workflows can be recovered and restarted

### Error Handling
- **Stage-Level Error Handling**: Each stage has its own error handling
- **Recovery Options**: Multiple recovery strategies (retry, skip, pause, rollback)
- **Error Logging**: Comprehensive error logging and reporting

### Performance Monitoring
- **Execution Metrics**: Track workflow duration and stage completion
- **Success Rates**: Monitor workflow success and failure rates
- **Resource Usage**: Track resource consumption and performance

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed correctly
2. **API Key Issues**: Verify your `.env` file contains the correct OpenAI API key
3. **Database Errors**: Check file permissions for SQLite database creation
4. **Workflow Failures**: Check error logs and recovery options

### Performance Tips

- **State Management**: Use appropriate database for production workloads
- **Concurrent Execution**: Limit concurrent workflows based on system resources
- **Error Recovery**: Implement appropriate retry strategies for failed stages
- **Monitoring**: Set up alerts for workflow failures and performance issues

## Next Steps

After mastering this example, explore:
- **Production Deployment**: Deploy workflows in production environments
- **Integration**: Connect workflows with external systems and APIs
- **Scaling**: Implement workflow orchestration at scale
- **Monitoring**: Set up comprehensive workflow monitoring and alerting

## Resources

- [Agno Documentation](https://github.com/agno-agi/agno)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Workflow Best Practices](https://github.com/agno-agi/agno/tree/main/cookbook/workflows)
- [State Management Patterns](https://github.com/agno-agi/agno/tree/main/cookbook/patterns)
