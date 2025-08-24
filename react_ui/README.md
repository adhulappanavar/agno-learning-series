# Simple React UI for Agno Workflows

A clean, simple React-based web interface to display Agno workflows in a table format.

## Features

- **Simple Table Display**: Shows all workflows in a clean, organized table
- **Real-time Data**: Fetches workflow data from the Python backend
- **Status Indicators**: Color-coded status badges for different workflow states
- **Responsive Design**: Works on desktop and mobile devices
- **Easy to Use**: Just click refresh to get the latest workflow data

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the Python Backend
```bash
python app.py
```
This starts the Flask backend on port 5001.

### 3. Start the React Frontend
```bash
npm start
```
This starts the React app on port 3000.

### 4. Open in Browser
Navigate to: http://localhost:3000

## What You'll See

- **Workflow ID**: Truncated workflow identifier
- **Stage**: Current workflow stage (e.g., "business_logic", "approval")
- **Status**: Workflow status with color coding
- **Created**: When the workflow was created
- **Updated**: When the workflow was last updated
- **Actions**: View details and stage data

## API Endpoints

- **GET /api/workflows**: Returns all workflows from the database
- **GET /api/health**: Health check endpoint

## Database Schema

The app reads from the `workflow_states.db` SQLite database with this structure:
- `id`: Workflow identifier
- `stage`: Current workflow stage
- `status`: Workflow status
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `stage_data`: JSON data for the current stage

## Next Steps

This is just the first step - a simple table view. Future enhancements could include:
- Workflow execution controls
- Real-time updates
- Detailed workflow visualization
- Performance metrics
- Error handling visualization
