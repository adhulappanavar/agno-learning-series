/**
 * Main JavaScript for Workflow Visualization Web UI
 * Phase 1: Foundation - Common functionality and utilities
 */

// Global variables
let socket = null;
let autoRefreshInterval = null;
let currentPage = 'dashboard';

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Workflow Visualization Web UI - Phase 1 Initialized');
    
    // Initialize common functionality
    initializeCommonFeatures();
    
    // Initialize page-specific features
    initializePageFeatures();
    
    // Initialize WebSocket connection
    initializeWebSocket();
});

/**
 * Initialize common features across all pages
 */
function initializeCommonFeatures() {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading states to buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('btn-loading')) {
                this.classList.add('btn-loading');
                this.disabled = true;
                
                // Remove loading state after a delay
                setTimeout(() => {
                    this.classList.remove('btn-loading');
                    this.disabled = false;
                }, 2000);
            }
        });
    });
    
    // Add card hover effects
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize notifications
    initializeNotifications();
}

/**
 * Initialize page-specific features
 */
function initializePageFeatures() {
    const path = window.location.pathname;
    
    if (path === '/' || path === '/dashboard') {
        currentPage = 'dashboard';
        initializeDashboard();
    } else if (path === '/workflow') {
        currentPage = 'workflow';
        initializeWorkflow();
    } else if (path === '/metrics') {
        currentPage = 'metrics';
        initializeMetrics();
    } else if (path === '/errors') {
        currentPage = 'errors';
        initializeErrors();
    }
}

/**
 * Initialize WebSocket connection
 */
function initializeWebSocket() {
    try {
        socket = io();
        
        socket.on('connect', function() {
            console.log('🔌 WebSocket connected');
            updateConnectionStatus('Connected', 'success');
            
            // Request initial data
            socket.emit('request_update');
        });
        
        socket.on('disconnect', function() {
            console.log('🔌 WebSocket disconnected');
            updateConnectionStatus('Disconnected', 'danger');
        });
        
        socket.on('connect_error', function(error) {
            console.error('🔌 WebSocket connection error:', error);
            updateConnectionStatus('Connection Error', 'warning');
        });
        
        socket.on('stats_update', function(data) {
            console.log('📊 Received stats update:', data);
            handleStatsUpdate(data);
        });
        
        socket.on('workflow_update', function(data) {
            console.log('🔄 Received workflow update:', data);
            handleWorkflowUpdate(data);
        });
        
        socket.on('error_update', function(data) {
            console.log('🚨 Received error update:', data);
            handleErrorUpdate(data);
        });
        
    } catch (error) {
        console.error('❌ Failed to initialize WebSocket:', error);
        updateConnectionStatus('WebSocket Unavailable', 'warning');
    }
}

/**
 * Update connection status indicator
 */
function updateConnectionStatus(text, type) {
    const indicator = document.getElementById('status-indicator');
    const statusText = document.getElementById('status-text');
    
    if (indicator && statusText) {
        statusText.textContent = text;
        indicator.className = `fas fa-circle text-${type} me-1`;
        
        // Update WebSocket status if available
        const wsStatus = document.getElementById('ws-status');
        if (wsStatus) {
            wsStatus.textContent = text;
            wsStatus.className = `badge bg-${type} ms-2`;
        }
    }
}

/**
 * Handle statistics updates
 */
function handleStatsUpdate(data) {
    if (currentPage === 'dashboard') {
        updateDashboardStats(data);
    }
    
    // Update any global stats displays
    updateGlobalStats(data);
}

/**
 * Handle workflow updates
 */
function handleWorkflowUpdate(data) {
    if (currentPage === 'workflow') {
        updateWorkflowDisplay(data);
    }
    
    // Update any global workflow displays
    updateGlobalWorkflows(data);
}

/**
 * Handle error updates
 */
function handleErrorUpdate(data) {
    if (currentPage === 'errors') {
        updateErrorDisplay(data);
    }
    
    // Update any global error displays
    updateGlobalErrors(data);
}

/**
 * Update global statistics
 */
function updateGlobalStats(stats) {
    // Update any global stat displays that might exist
    const totalWorkflows = document.getElementById('total-workflows');
    const activeWorkflows = document.getElementById('active-workflows');
    const completedWorkflows = document.getElementById('completed-workflows');
    const failedWorkflows = document.getElementById('failed-workflows');
    
    if (totalWorkflows) totalWorkflows.textContent = stats.total_workflows || 0;
    if (activeWorkflows) activeWorkflows.textContent = stats.active_workflows || 0;
    if (completedWorkflows) completedWorkflows.textContent = stats.completed_workflows || 0;
    if (failedWorkflows) failedWorkflows.textContent = stats.failed_workflows || 0;
}

/**
 * Update global workflow displays
 */
function updateGlobalWorkflows(workflows) {
    // This will be implemented in Phase 2
    console.log('Global workflow update:', workflows);
}

/**
 * Update global error displays
 */
function updateGlobalErrors(errors) {
    // This will be implemented in Phase 4
    console.log('Global error update:', errors);
}

/**
 * Initialize tooltips
 */
function initializeTooltips() {
    // Initialize Bootstrap tooltips if available
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

/**
 * Initialize notification system
 */
function initializeNotifications() {
    // Create notification container if it doesn't exist
    if (!document.getElementById('notification-container')) {
        const container = document.createElement('div');
        container.id = 'notification-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            max-width: 400px;
        `;
        document.body.appendChild(container);
    }
}

/**
 * Show notification
 */
function showNotification(message, type = 'info', duration = 5000) {
    const container = document.getElementById('notification-container');
    if (!container) return;
    
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    container.appendChild(notification);
    
    // Auto-remove after duration
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, duration);
    
    // Add click to dismiss
    notification.addEventListener('click', function() {
        this.remove();
    });
}

/**
 * Initialize dashboard page
 */
function initializeDashboard() {
    console.log('📊 Dashboard initialized');
    
    // Start auto-refresh
    startAutoRefresh();
    
    // Update last update timestamp
    updateLastUpdate();
    
    // Load initial data
    loadDashboardData();
}

/**
 * Initialize workflow page
 */
function initializeWorkflow() {
    console.log('🔄 Workflow page initialized');
    
    // This will be implemented in Phase 2
    showNotification('Workflow visualization will be available in Phase 2', 'info');
}

/**
 * Initialize metrics page
 */
function initializeMetrics() {
    console.log('📈 Metrics page initialized');
    
    // This will be implemented in Phase 3
    showNotification('Metrics dashboard will be available in Phase 3', 'info');
}

/**
 * Initialize errors page
 */
function initializeErrors() {
    console.log('🚨 Errors page initialized');
    
    // This will be implemented in Phase 4
    showNotification('Error handling dashboard will be available in Phase 4', 'info');
}

/**
 * Start auto-refresh for dashboard
 */
function startAutoRefresh() {
    if (autoRefreshInterval) {
        clearInterval(autoRefreshInterval);
    }
    
    autoRefreshInterval = setInterval(() => {
        if (currentPage === 'dashboard') {
            refreshDashboardData();
        }
    }, 30000); // 30 seconds
}

/**
 * Load dashboard data
 */
function loadDashboardData() {
    fetch('/api/stats')
        .then(response => response.json())
        .then(data => {
            updateDashboardStats(data);
            showNotification('Dashboard data loaded successfully', 'success');
        })
        .catch(error => {
            console.error('Error loading dashboard data:', error);
            showNotification('Failed to load dashboard data', 'danger');
        });
}

/**
 * Refresh dashboard data
 */
function refreshDashboardData() {
    fetch('/api/stats')
        .then(response => response.json())
        .then(data => {
            updateDashboardStats(data);
            updateLastUpdate();
        })
        .catch(error => {
            console.error('Error refreshing dashboard data:', error);
        });
}

/**
 * Update dashboard statistics
 */
function updateDashboardStats(stats) {
    // Update statistics cards
    const totalWorkflows = document.getElementById('total-workflows');
    const activeWorkflows = document.getElementById('active-workflows');
    const completedWorkflows = document.getElementById('completed-workflows');
    const failedWorkflows = document.getElementById('failed-workflows');
    
    if (totalWorkflows) totalWorkflows.textContent = stats.total_workflows || 0;
    if (activeWorkflows) activeWorkflows.textContent = stats.active_workflows || 0;
    if (completedWorkflows) completedWorkflows.textContent = stats.completed_workflows || 0;
    if (failedWorkflows) failedWorkflows.textContent = stats.failed_workflows || 0;
    
    // Update recent workflows table if it exists
    if (stats.recent_workflows && stats.recent_workflows.length > 0) {
        updateRecentWorkflowsTable(stats.recent_workflows);
    }
}

/**
 * Update recent workflows table
 */
function updateRecentWorkflowsTable(workflows) {
    const tbody = document.querySelector('#recent-workflows-table tbody');
    if (!tbody) return;
    
    tbody.innerHTML = '';
    
    workflows.forEach(workflow => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><code>${workflow.id.substring(0, 8)}...</code></td>
            <td><span class="badge bg-primary">${workflow.type}</span></td>
            <td>${getStatusBadge(workflow.status)}</td>
            <td>${workflow.stage}</td>
            <td>${workflow.created}</td>
            <td>${workflow.updated}</td>
            <td>
                <button class="btn btn-sm btn-outline-primary" onclick="viewWorkflow('${workflow.id}')">
                    <i class="fas fa-eye"></i>
                </button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

/**
 * Get status badge HTML
 */
function getStatusBadge(status) {
    if (status === 'completed') {
        return '<span class="badge bg-success">Completed</span>';
    } else if (status === 'failed') {
        return '<span class="badge bg-danger">Failed</span>';
    } else if (status === 'running') {
        return '<span class="badge bg-info">Running</span>';
    } else {
        return `<span class="badge bg-secondary">${status}</span>`;
    }
}

/**
 * Update last update timestamp
 */
function updateLastUpdate() {
    const lastUpdate = document.getElementById('last-update');
    if (lastUpdate) {
        const now = new Date();
        lastUpdate.textContent = now.toLocaleString();
    }
}

/**
 * View workflow details
 */
function viewWorkflow(workflowId) {
    console.log('Viewing workflow:', workflowId);
    showNotification(`Viewing workflow: ${workflowId}\n\nThis feature will be implemented in Phase 2.`, 'info');
}

/**
 * Refresh data (global function)
 */
function refreshData() {
    if (currentPage === 'dashboard') {
        refreshDashboardData();
    } else if (currentPage === 'workflow') {
        // Will be implemented in Phase 2
        showNotification('Workflow refresh will be available in Phase 2', 'info');
    } else if (currentPage === 'metrics') {
        // Will be implemented in Phase 3
        showNotification('Metrics refresh will be available in Phase 3', 'info');
    } else if (currentPage === 'errors') {
        // Will be implemented in Phase 4
        showNotification('Error refresh will be available in Phase 4', 'info');
    }
}

/**
 * Cleanup on page unload
 */
window.addEventListener('beforeunload', function() {
    if (autoRefreshInterval) {
        clearInterval(autoRefreshInterval);
    }
    if (socket) {
        socket.disconnect();
    }
});

/**
 * Export functions for use in templates
 */
window.refreshData = refreshData;
window.viewWorkflow = viewWorkflow;
window.updateLastUpdate = updateLastUpdate;
