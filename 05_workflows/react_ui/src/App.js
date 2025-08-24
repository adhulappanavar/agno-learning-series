import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [workflows, setWorkflows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

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
      <div className="container mt-4">
        <div className="row">
          <div className="col-12">
            <div className="d-flex justify-content-between align-items-center mb-4">
              <h1>Agno Workflows</h1>
              <div>
                <button 
                  className="btn btn-outline-primary me-2" 
                  onClick={fetchWorkflows}
                >
                  <i className="fas fa-sync-alt me-1"></i>
                  Refresh
                </button>
                <span className="badge bg-secondary">
                  {workflows.length} workflows
                </span>
              </div>
            </div>

            {workflows.length === 0 ? (
              <div className="alert alert-info" role="alert">
                <h4 className="alert-heading">No Workflows Found</h4>
                <p>No workflow data is currently available in the database.</p>
                <hr />
                <p className="mb-0">
                  Make sure you have run some workflows first, then click Refresh.
                </p>
              </div>
            ) : (
              <div className="table-responsive">
                <table className="table table-striped table-hover">
                  <thead className="table-dark">
                    <tr>
                      <th>ID</th>
                      <th>Stage</th>
                      <th>Status</th>
                      <th>Created</th>
                      <th>Updated</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {workflows.map((workflow, index) => (
                      <tr key={workflow.id || index}>
                        <td>
                          <code className="text-primary">
                            {workflow.id ? workflow.id.substring(0, 12) + '...' : 'N/A'}
                          </code>
                        </td>
                        <td>
                          <span className="badge bg-info">
                            {workflow.stage || 'Unknown'}
                          </span>
                        </td>
                        <td>
                          <span className={`badge ${getStatusColor(workflow.status).replace('text-', 'bg-')}`}>
                            {workflow.status || 'Unknown'}
                          </span>
                        </td>
                        <td>
                          <small className="text-muted">
                            {formatDate(workflow.created_at)}
                          </small>
                        </td>
                        <td>
                          <small className="text-muted">
                            {formatDate(workflow.updated_at)}
                          </small>
                        </td>
                        <td>
                          <button 
                            className="btn btn-sm btn-outline-primary me-1"
                            onClick={() => alert(`Workflow ID: ${workflow.id}`)}
                            title="View Details"
                          >
                            <i className="fas fa-eye"></i>
                          </button>
                          <button 
                            className="btn btn-sm btn-outline-secondary"
                            onClick={() => alert(`Stage Data: ${workflow.stage_data}`)}
                            title="View Stage Data"
                          >
                            <i className="fas fa-code"></i>
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
