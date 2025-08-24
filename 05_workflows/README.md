# Example 5: Workflows (Level 5)

This is the fifth and final example in the Agno learning series. We'll build a **Level 5** system with complex agentic workflows, state management, and advanced orchestration capabilities.

## What You'll Learn

- How to create multi-stage workflows with state management
- How to implement workflow persistence and recovery
- How to handle errors and provide recovery mechanisms
- How to run multiple workflows concurrently
- How to customize workflows for different domains
- How to monitor workflow performance and metrics
- How to implement conditional branching and decision making

## What We're Building

A sophisticated workflow orchestration system that can:

- **Orchestrate Complex Processes**: Multi-stage workflows with dependencies
- **Manage State Persistence**: Save and restore workflow states across sessions
- **Handle Errors Gracefully**: Provide recovery options and error handling
- **Execute Concurrently**: Run multiple workflows simultaneously
- **Track Performance**: Monitor metrics and performance indicators
- **Customize for Domains**: Adapt workflows for different business needs

## Key Differences from Previous Examples

- **Level 1**: Basic tools and instructions
- **Level 2**: Knowledge storage and retrieval
- **Level 3**: Memory, reasoning, and session persistence
- **Level 4**: Multi-agent collaboration and team coordination
- **Level 5**: **Complex agentic workflows with state management**
- **New Features**: Workflow orchestration, state persistence, error recovery, concurrent execution

## Files

- `workflows.py` - The main workflows code with complex workflow orchestration
- `workflow_test.py` - Comprehensive testing suite for workflow capabilities
- `requirements.txt` - Dependencies
- `setup.md` - Setup and usage guide

## Example Output

When you run `python workflows.py`, you'll see:

```
🚀 Complex Workflows (Level 5) Demonstration
============================================================
This example shows advanced workflow orchestration with state management.

💰 Example 1: Financial Approval Workflow
----------------------------------------
🚀 Creating new workflow: financial_001

🔄 [2024-01-15 10:30:15] PLANNING: Starting workflow analysis and planning
🤖 Workflow Orchestrator is thinking...
🤖 Workflow Orchestrator: Here is a comprehensive workflow execution plan...

📊 Stage Data: {
  "plan": "Detailed execution plan...",
  "input_analysis": {...},
  "planning_timestamp": "2024-01-15T10:30:15.123456"
}

🔄 [2024-01-15 10:30:16] DATA_PROCESSING: Starting data processing and validation
🤖 Data Processor is thinking...
🤖 Data Processor: Here is a comprehensive data processing workflow design...

📊 Stage Data: {
  "pipeline_design": "Data transformation pipeline...",
  "validation_rules": ["data_format", "data_range", "data_completeness"],
  "processing_timestamp": "2024-01-15T10:30:17.123456",
  "records_processed": 3
}

🔄 [2024-01-15 10:30:18] BUSINESS_LOGIC: Starting business logic execution
🔄 [2024-01-15 10:30:19] APPROVAL: Starting approval and decision making
🤖 Approval Manager is thinking...
🤖 Approval Manager: Here is a comprehensive approval workflow design...

🔄 [2024-01-15 10:30:20] FINALIZATION: Starting finalization and reporting

🎉 Workflow completed successfully!
============================================================

📊 Financial Workflow Result: completed
```

## Key Features Demonstrated

### 🚀 **Workflow Orchestration**
- **Multi-Stage Execution**: 5-stage workflow with clear progression
- **State Management**: Persistent workflow states with SQLite database
- **Conditional Logic**: Different business logic based on workflow type
- **Error Handling**: Comprehensive error handling with recovery options

### 🧠 **Specialized Agents**
- **Workflow Orchestrator**: Plans and coordinates workflow execution
- **Data Processor**: Handles data transformation and validation
- **Approval Manager**: Manages approval workflows and decision gates

### 📊 **State Management**
- **Persistent Storage**: Workflow states saved to SQLite database
- **Resume Capability**: Workflows can be paused and resumed
- **State Recovery**: Failed workflows can be recovered and restarted
- **Progress Tracking**: Monitor workflow progress and completion

### 🔄 **Error Handling & Recovery**
- **Stage-Level Error Handling**: Each stage has its own error handling
- **Recovery Options**: Multiple recovery strategies (retry, skip, pause, rollback)
- **Error Logging**: Comprehensive error logging and reporting
- **Graceful Degradation**: Handle failures without losing progress

## Workflow Types

### 💰 **Financial Approval Workflow**
- **Purpose**: Handle financial requests and approvals
- **Stages**: Budget validation, approval hierarchy, compliance checks
- **Output**: Approved/rejected financial requests with audit trail

### 📊 **Data Processing Workflow**
- **Purpose**: Transform and validate data
- **Stages**: Data extraction, transformation, validation, loading
- **Output**: Processed data with quality metrics

### 🏢 **Standard Business Workflow**
- **Purpose**: Handle general business processes
- **Stages**: Input validation, processing, output generation
- **Output**: Completed business processes with documentation

## Running the Examples

### Basic Workflows Demonstration
```bash
python workflows.py
```

### Extended Workflow Testing
```bash
python workflow_test.py
```

## Workflow Testing Suite

The `workflow_test.py` script demonstrates:

1. **Workflow Persistence**: Pause, resume, and recover workflows
2. **Error Handling**: Test error conditions and recovery mechanisms
3. **Concurrent Execution**: Run multiple workflows simultaneously
4. **Performance Metrics**: Track workflow performance and timing
5. **Customization**: Test domain-specific workflow types
6. **State Inspection**: Analyze workflow states and progress

## Advanced Capabilities

### 🔄 **Concurrent Workflow Execution**
- **Multiple Workflows**: Run several workflows simultaneously
- **Resource Management**: Efficient resource allocation across workflows
- **Performance Monitoring**: Track concurrent execution metrics
- **Scalability**: Handle increasing workflow loads

### 📈 **Performance Monitoring**
- **Execution Metrics**: Track workflow duration and stage completion
- **Success Rates**: Monitor workflow success and failure rates
- **Resource Usage**: Track resource consumption and performance
- **Real-time Monitoring**: Live workflow status and progress

### 🎯 **Workflow Customization**
- **Domain-Specific Workflows**: Adapt workflows for different industries
- **Custom Stages**: Add new workflow stages and logic
- **Business Rules**: Implement domain-specific business rules
- **Compliance**: Ensure workflows meet regulatory requirements

## Customization Options

### Adding New Workflow Types
- Create new workflow classes extending `ComplexWorkflow`
- Implement domain-specific business logic
- Add custom validation and processing rules
- Integrate with external systems and APIs

### Modifying Workflow Stages
- Update workflow execution logic
- Add new stages and dependencies
- Implement custom error handling
- Add stage-specific monitoring and metrics

### Custom State Management
- Extend workflow state classes
- Add custom state fields and data
- Implement custom persistence strategies
- Add state validation and integrity checks

## Performance Considerations

- **State Persistence**: SQLite for development, production databases for scale
- **Concurrent Execution**: Limit based on system resources and API limits
- **Error Recovery**: Implement appropriate retry strategies and timeouts
- **Monitoring**: Set up alerts for workflow failures and performance issues

## Best Practices

### Workflow Design
- **Clear Stage Definition**: Define clear inputs, outputs, and dependencies
- **Error Handling**: Implement comprehensive error handling at each stage
- **State Management**: Ensure state consistency across workflow stages
- **Monitoring**: Track workflow progress and performance metrics

### Performance Optimization
- **Resource Management**: Efficiently allocate resources across workflows
- **Caching**: Cache frequently accessed data and states
- **Parallelization**: Execute independent stages in parallel
- **Batch Processing**: Group similar operations for efficiency

### Error Recovery
- **Retry Strategies**: Implement appropriate retry logic for transient failures
- **Rollback Mechanisms**: Provide rollback capabilities for failed workflows
- **Manual Intervention**: Allow manual intervention for complex failures
- **Audit Trails**: Maintain comprehensive audit trails for compliance

## Next Steps

After mastering this example, you'll have completed the full Agno learning series:

- **Level 1**: Basic tools and instructions ✅
- **Level 2**: Knowledge storage and retrieval ✅
- **Level 3**: Memory, reasoning, and session persistence ✅
- **Level 4**: Multi-agent collaboration and team coordination ✅
- **Level 5**: Complex agentic workflows with state management ✅

## 🔧 Troubleshooting

### Common Issues

1. **Workflow Failures**: Check error logs and recovery options
2. **State Persistence Issues**: Verify database permissions and connectivity
3. **Performance Issues**: Monitor resource usage and concurrent execution
4. **API Rate Limits**: Manage OpenAI API usage across multiple workflows

### Solutions

- **Check Error Logs**: Review detailed error messages and recovery options
- **Verify Database**: Ensure SQLite database is accessible and writable
- **Monitor Resources**: Track system resources and API usage
- **Implement Retries**: Add retry logic for transient failures

## Resources

- [Agno Documentation](https://github.com/agno-agi/agno)
- [Workflow Best Practices](https://github.com/agno-agi/agno/tree/main/cookbook/workflows)
- [State Management Patterns](https://github.com/agno-agi/agno/tree/main/cookbook/patterns)
- [Multi-Agent Systems](https://github.com/agno-agi/agno/tree/main/cookbook/agent_levels)

---

**🎉 Congratulations! You've completed the full Agno learning series!** 

From basic tools to complex workflows, you now have a comprehensive understanding of building intelligent, multi-agent systems with Agno. Ready to build your own production-ready AI applications? 🚀
