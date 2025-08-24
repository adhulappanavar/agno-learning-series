import React, { useState, useEffect, useCallback } from 'react';
import ReactFlow, { 
  MiniMap, 
  Controls, 
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Handle,
  Position
} from 'reactflow';
import 'reactflow/dist/style.css';
import './App.css';

// Custom node component with tooltip
const CustomNode = ({ data }) => {
  const [showTooltip, setShowTooltip] = useState(false);
  
  return (
    <div 
      className="custom-node"
      onMouseEnter={() => setShowTooltip(true)}
      onMouseLeave={() => setShowTooltip(false)}
    >
      <Handle type="target" position={Position.Top} />
      <div className="node-content">
        <div className="node-label">{data.label}</div>
        {showTooltip && (
          <div className="node-tooltip">
            <strong>{data.label}</strong>
            <p>{data.description}</p>
            <div className="tooltip-status">
              Status: <span className={`status-${data.status}`}>{data.status}</span>
            </div>
          </div>
        )}
      </div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
};

const nodeTypes = {
  custom: CustomNode,
};

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
      stages = ['Requirements Analysis', 'Financial Modeling', 'Risk Assessment', 'Compliance Check', 'Budget Approval', 'Execution', 'Audit & Reporting'];
      descriptions = {
        'Requirements Analysis': 'Analyze financial requirements, gather stakeholder input, define project scope and budget constraints',
        'Financial Modeling': 'Create financial projections, cash flow analysis, ROI calculations, and scenario planning',
        'Risk Assessment': 'Identify financial risks, market volatility analysis, stress testing, and risk mitigation strategies',
        'Compliance Check': 'Verify regulatory compliance, internal policy adherence, and legal requirements validation',
        'Budget Approval': 'Present to stakeholders, obtain executive approval, secure funding allocation',
        'Execution': 'Implement approved financial plan, monitor progress, adjust strategies as needed',
        'Audit & Reporting': 'Generate financial reports, conduct audits, document outcomes and lessons learned'
      };
    } else if (workflow.id.includes('data')) {
      stages = ['Data Discovery', 'Source Validation', 'ETL Processing', 'Quality Assurance', 'Transformation', 'Testing', 'Deployment'];
      descriptions = {
        'Data Discovery': 'Identify data sources, assess data quality, map data relationships and dependencies',
        'Source Validation': 'Verify data source authenticity, check data lineage, validate source system integrity',
        'ETL Processing': 'Extract data from sources, transform according to business rules, load into target systems',
        'Quality Assurance': 'Run data quality checks, identify anomalies, validate data completeness and accuracy',
        'Transformation': 'Apply business logic, data cleansing, aggregation, and business rule implementation',
        'Testing': 'Validate transformed data, run test scenarios, verify business logic correctness',
        'Deployment': 'Deploy to production, monitor performance, establish data governance and monitoring'
      };
    } else if (workflow.id.includes('business')) {
      stages = ['Market Research', 'Strategy Development', 'Stakeholder Alignment', 'Resource Planning', 'Implementation', 'Performance Monitoring', 'Optimization'];
      descriptions = {
        'Market Research': 'Analyze market conditions, competitive landscape, customer needs, and business opportunities',
        'Strategy Development': 'Define business objectives, develop strategic initiatives, create action plans and timelines',
        'Stakeholder Alignment': 'Engage key stakeholders, align on objectives, secure buy-in and commitment',
        'Resource Planning': 'Allocate resources, budget planning, team assignment, and timeline development',
        'Implementation': 'Execute strategic initiatives, manage change, coordinate cross-functional teams',
        'Performance Monitoring': 'Track KPIs, measure progress, identify bottlenecks and success metrics',
        'Optimization': 'Analyze results, identify improvements, implement lessons learned and best practices'
      };
    } else {
      // Generic workflow for unknown types
      stages = ['Initiation', 'Planning', 'Execution', 'Monitoring', 'Closure'];
      descriptions = {
        'Initiation': 'Define project scope, identify stakeholders, establish objectives and success criteria',
        'Planning': 'Develop detailed project plan, resource allocation, risk assessment, and timeline creation',
        'Execution': 'Implement project activities, manage resources, coordinate team efforts and deliverables',
        'Monitoring': 'Track progress, manage changes, control quality, and communicate status updates',
        'Closure': 'Complete deliverables, conduct lessons learned, document outcomes and archive project data'
      };
    }

    // Create nodes for each stage with better positioning
    const nodeWidth = 200;
    const nodeHeight = 80;
    const horizontalSpacing = 280;
    const verticalSpacing = 140;
    
    const newNodes = stages.map((stage, index) => {
      // Arrange nodes in a more compact grid layout
      const row = Math.floor(index / 3);
      const col = index % 3;
      
      // Determine node status
      let nodeStatus = 'pending';
      if (workflow.stage === stage.toLowerCase().replace(/\s+/g, '_')) {
        nodeStatus = 'current';
      } else if (workflow.stage === 'finalization' && index < stages.length - 1) {
        nodeStatus = 'completed';
      }
      
      return {
        id: stage.toLowerCase().replace(/\s+/g, '_'),
        type: 'custom', // Use the custom node type
        position: { 
          x: col * horizontalSpacing + 50, 
          y: row * verticalSpacing + 50 
        },
        data: { 
          label: stage,
          description: descriptions[stage],
          status: nodeStatus
        },
        style: {
          width: nodeWidth,
          height: nodeHeight,
        },
        // Set data attributes for CSS styling
        data: {
          ...stage,
          label: stage,
          description: descriptions[stage],
          status: nodeStatus
        }
      };
    });

    // Create edges connecting stages in logical flow
    const newEdges = [];
    for (let i = 0; i < stages.length - 1; i++) {
      newEdges.push({
        id: `e${i}`,
        source: stages[i].toLowerCase().replace(/\s+/g, '_'),
        target: stages[i + 1].toLowerCase().replace(/\s+/g, '_'),
        type: 'smoothstep',
        style: { 
          stroke: '#333', 
          strokeWidth: 2,
          strokeDasharray: workflow.stage === stages[i + 1].toLowerCase().replace(/\s+/g, '_') ? '0' : '5,5'
        },
        animated: workflow.stage === stages[i + 1].toLowerCase().replace(/\s+/g, '_'),
        label: `Stage ${i + 1} → ${i + 2}`
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
                          nodeTypes={nodeTypes}
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