import React, { useState, useEffect, useCallback } from 'react';
import ReactFlow, { 
  MiniMap, 
  Controls, 
  Background,
  useNodesState,
  useEdgesState,
  addEdge
} from 'reactflow';
import 'reactflow/dist/style.css';
import './App.css';

function App() {
  const [workflows, setWorkflows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedWorkflow, setSelectedWorkflow] = useState(null);
  const [showDiagram, setShowDiagram] = useState(false);
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  useEffect(() => {
    fetchWorkflows();
  }, []);

  const fetchWorkflows = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/workflows');
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setWorkflows(data.workflows || []);
      setError(null);
    } catch (err) {
      console.error('Error fetching workflows:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    try {
      return new Date(dateString).toLocaleString();
    } catch {
      return dateString;
    }
  };

  const getStatusColor = (status) => {
    switch (status?.toLowerCase()) {
      case 'completed':
        return 'text-success';
      case 'running':
        return 'text-warning';
      case 'failed':
        return 'text-danger';
      case 'pending':
        return 'text-info';
      default:
        return 'text-muted';
    }
  };

  const getStatusBadgeClass = (status) => {
    switch (status?.toLowerCase()) {
      case 'completed':
        return 'bg-success';
      case 'running':
        return 'bg-warning';
      case 'failed':
        return 'bg-danger';
      case 'pending':
        return 'bg-info';
      default:
        return 'bg-secondary';
    }
  };

  const selectWorkflow = (workflow) => {
    setSelectedWorkflow(workflow);
    setShowDiagram(false);
    generateWorkflowDiagram(workflow);
  };

  const generateWorkflowDiagram = (workflow) => {
    // Define workflow stages based on workflow type
    let stages = [];
    let descriptions = {};
    
    if (workflow.id.includes('financial')) {
      stages = ['Planning', 'Data Processing', 'Business Logic', 'Approval', 'Finalization'];
      descriptions = {
        'Planning': 'Analyze financial requirements and create strategic plans',
        'Data Processing': 'Process financial data and validate inputs',
        'Business Logic': 'Apply financial rules and calculations',
        'Approval': 'Review and approve financial decisions',
        'Finalization': 'Execute approved plans and generate reports'
      };
    } else if (workflow.id.includes('data')) {
      stages = ['Planning', 'Data Processing', 'Business Logic', 'Approval', 'Finalization'];
      descriptions = {
        'Planning': 'Design data processing workflow and requirements',
        'Data Processing': 'Extract, transform, and validate data',
        'Business Logic': 'Apply business rules and data integrity checks',
        'Approval': 'Review data quality and processing results',
        'Finalization': 'Generate processed data and quality metrics'
      };
    } else {
      stages = ['Planning', 'Data Processing', 'Business Logic', 'Approval', 'Finalization'];
      descriptions = {
        'Planning': 'Analyze business requirements and create execution plan',
        'Data Processing': 'Process business data and validate inputs',
        'Business Logic': 'Apply business rules and compliance checks',
        'Approval': 'Review and approve business decisions',
        'Finalization': 'Execute approved plans and generate documentation'
      };
    }

    // Create nodes for each stage
    const newNodes = stages.map((stage, index) => ({
      id: stage.toLowerCase().replace(' ', '_'),
      type: 'default',
      position: { x: 250, y: index * 120 },
      data: { 
        label: stage,
        description: descriptions[stage],
        status: workflow.stage === stage.toLowerCase() ? 'current' : 
                workflow.stage === 'finalization' && index < stages.length - 1 ? 'completed' : 'pending'
      },
      style: {
        background: workflow.stage === stage.toLowerCase() ? '#17a2b8' : 
                   workflow.stage === 'finalization' && index < stages.length - 1 ? '#28a745' : '#6c757d',
        color: 'white',
        border: '2px solid #333',
        borderRadius: '8px',
        padding: '10px',
        width: 200,
        textAlign: 'center'
      }
    }));

    // Create edges connecting stages
    const newEdges = [];
    for (let i = 0; i < stages.length - 1; i++) {
      newEdges.push({
        id: `e${i}`,
        source: stages[i].toLowerCase().replace(' ', '_'),
        target: stages[i + 1].toLowerCase().replace(' ', '_'),
        type: 'smoothstep',
        style: { stroke: '#333', strokeWidth: 2 },
        animated: workflow.stage === stages[i + 1].toLowerCase()
      });
    }

    setNodes(newNodes);
    setEdges(newEdges);
  };

  const runWorkflow = async (workflowId) => {
    try {
      // Simulate workflow execution
      setSelectedWorkflow(prev => ({ ...prev, status: 'running' }));
      
      // Update workflow status in the backend (you can implement this)
      console.log(`Starting workflow: ${workflowId}`);
      
      // Simulate progress
      setTimeout(() => {
        setSelectedWorkflow(prev => ({ ...prev, status: 'completed' }));
        alert(`Workflow ${workflowId} execution completed!`);
      }, 3000);
      
    } catch (error) {
      console.error('Error running workflow:', error);
      alert('Error running workflow. Please try again.');
    }
  };

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges],
  );

  if (loading) {
    return (
      <div className="App">
        <div className="container mt-4">
          <div className="text-center">
            <div className="spinner-border" role="status">
              <span className="visually-hidden">Loading...</span>
            </div>
            <p className="mt-2">Loading workflows...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="App">
        <div className="container mt-4">
          <div className="alert alert-danger" role="alert">
            <h4 className="alert-heading">Error Loading Workflows</h4>
            <p>{error}</p>
            <hr />
            <button 
              className="btn btn-primary" 
              onClick={fetchWorkflows}
            >
              Try Again
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <div className="container-fluid mt-4">
        <div className="row">
          {/* Workflows List */}
          <div className="col-md-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
              <h3>Workflows</h3>
              <button 
                className="btn btn-outline-primary btn-sm" 
                onClick={fetchWorkflows}
              >
                <i className="fas fa-sync-alt me-1"></i>
                Refresh
              </button>
            </div>
            
            <div className="workflow-list">
              {workflows.map((workflow, index) => (
                <div 
                  key={workflow.id || index}
                  className={`workflow-card ${selectedWorkflow?.id === workflow.id ? 'selected' : ''}`}
                  onClick={() => selectWorkflow(workflow)}
                >
                  <div className="card mb-3">
                    <div className="card-body">
                      <h6 className="card-title">
                        <code className="text-primary">{workflow.id}</code>
                      </h6>
                      <div className="mb-2">
                        <span className={`badge ${getStatusBadgeClass(workflow.status)}`}>
                          {workflow.status}
                        </span>
                      </div>
                      <div className="mb-2">
                        <small className="text-muted">
                          Stage: {workflow.stage}
                        </small>
                      </div>
                      <div className="d-flex justify-content-between">
                        <button 
                          className="btn btn-sm btn-outline-primary"
                          onClick={(e) => {
                            e.stopPropagation();
                            setShowDiagram(true);
                          }}
                        >
                          <i className="fas fa-sitemap me-1"></i>
                          Diagram
                        </button>
                        <button 
                          className="btn btn-sm btn-outline-success"
                          onClick={(e) => {
                            e.stopPropagation();
                            runWorkflow(workflow.id);
                          }}
                        >
                          <i className="fas fa-play me-1"></i>
                          Run
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Workflow Details and Diagram */}
          <div className="col-md-8">
            {selectedWorkflow ? (
              <div>
                <div className="d-flex justify-content-between align-items-center mb-4">
                  <h3>Workflow: {selectedWorkflow.id}</h3>
                  <div>
                    <button 
                      className="btn btn-outline-secondary me-2"
                      onClick={() => setShowDiagram(!showDiagram)}
                    >
                      <i className="fas fa-sitemap me-1"></i>
                      {showDiagram ? 'Hide' : 'Show'} Diagram
                    </button>
                    <button 
                      className="btn btn-success"
                      onClick={() => runWorkflow(selectedWorkflow.id)}
                    >
                      <i className="fas fa-play me-1"></i>
                      Run Workflow
                    </button>
                  </div>
                </div>

                {/* Workflow Info */}
                <div className="card mb-4">
                  <div className="card-body">
                    <div className="row">
                      <div className="col-md-6">
                        <p><strong>Status:</strong> 
                          <span className={`badge ${getStatusBadgeClass(selectedWorkflow.status)} ms-2`}>
                            {selectedWorkflow.status}
                          </span>
                        </p>
                        <p><strong>Current Stage:</strong> {selectedWorkflow.stage}</p>
                        <p><strong>Created:</strong> {formatDate(selectedWorkflow.created_at)}</p>
                      </div>
                      <div className="col-md-6">
                        <p><strong>Updated:</strong> {formatDate(selectedWorkflow.updated_at)}</p>
                        <p><strong>Stage Data:</strong></p>
                        <pre className="bg-light p-2 rounded">
                          {JSON.stringify(JSON.parse(selectedWorkflow.stage_data || '{}'), null, 2)}
                        </pre>
                      </div>
                    </div>
                  </div>
                </div>

                {/* React Flow Diagram */}
                {showDiagram && (
                  <div className="card">
                    <div className="card-body">
                      <h5 className="card-title">Workflow Flow Diagram</h5>
                      <div style={{ height: '600px', width: '100%' }}>
                        <ReactFlow
                          nodes={nodes}
                          edges={edges}
                          onNodesChange={onNodesChange}
                          onEdgesChange={onEdgesChange}
                          onConnect={onConnect}
                          fitView
                        >
                          <Controls />
                          <MiniMap />
                          <Background color="#aaa" gap={16} />
                        </ReactFlow>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <div className="text-center mt-5">
                <i className="fas fa-sitemap fa-3x text-muted mb-3"></i>
                <h4 className="text-muted">Select a Workflow</h4>
                <p className="text-muted">Choose a workflow from the list to view details and diagram</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
