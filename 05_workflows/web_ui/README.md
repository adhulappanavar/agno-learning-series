# Workflow Visualization Web UI

A modern, interactive web-based interface for visualizing workflows, metrics, and error handling in the Agno framework.

## 🚀 Phase 1: Foundation Complete

This is the foundation implementation of the web UI, providing the basic structure and navigation for the complete workflow visualization system.

## ✨ Features Implemented (Phase 1)

### 🏗️ **Core Infrastructure**
- **Flask Web Application**: Modern Python web framework
- **Real-time Updates**: WebSocket support with Socket.IO
- **Database Integration**: SQLite database connectivity
- **Responsive Design**: Bootstrap 5 + custom CSS
- **Modern UI/UX**: Interactive elements and animations

### 📊 **Dashboard**
- **Statistics Cards**: Total, active, completed, and failed workflows
- **Recent Workflows Table**: Latest workflow executions
- **Quick Actions**: Navigation to different sections
- **System Status**: Database and WebSocket connection status
- **Auto-refresh**: Automatic data updates every 30 seconds

### 🧭 **Navigation**
- **Main Dashboard**: Overview and statistics
- **Workflows**: Workflow visualization (Phase 2)
- **Metrics**: Performance metrics (Phase 3)
- **Errors**: Error handling dashboard (Phase 4)

### 🔌 **Real-time Features**
- **WebSocket Connection**: Live status updates
- **Connection Monitoring**: Real-time connection status
- **Data Synchronization**: Automatic data refresh
- **Event Handling**: Real-time workflow updates

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Modern web browser

### 1. Install Dependencies
```bash
cd 05_workflows/web_ui
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the Web UI
Open your browser and navigate to:
- **Main Dashboard**: http://localhost:5000
- **Workflows**: http://localhost:5000/workflow
- **Metrics**: http://localhost:5000/metrics
- **Errors**: http://localhost:5000/errors

## 📁 Project Structure

```
web_ui/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base layout template
│   ├── dashboard.html   # Main dashboard
│   ├── workflow.html    # Workflow visualization
│   ├── metrics.html     # Metrics dashboard
│   └── errors.html      # Error handling dashboard
├── static/              # Static assets
│   ├── css/            # Stylesheets
│   │   └── main.css    # Main CSS file
│   ├── js/             # JavaScript files
│   │   └── main.js     # Main JavaScript file
│   └── img/            # Images and icons
└── models/              # Data models (future use)
```

## 🔧 Configuration

### Environment Variables
The application uses the following configuration:

- **Database Path**: `../workflow_states.db` (relative to app.py)
- **Port**: 5000 (configurable in app.py)
- **Host**: 0.0.0.0 (accessible from any IP)
- **Debug Mode**: Enabled for development

### Database Connection
The web UI automatically connects to the workflow database created by the workflow system. If no database exists, it will show empty statistics.

## 🎯 What's Coming Next

### Phase 2: Interactive Workflow Visualization
- **Interactive Diagrams**: Clickable workflow stages
- **Real-time Monitoring**: Live stage execution updates
- **Execution Controls**: Play/pause/step through workflows
- **Stage Details**: Detailed stage information and data
- **Visual Designer**: Drag-and-drop workflow creation

### Phase 3: Performance Metrics Dashboard
- **Execution Charts**: Real-time performance visualization
- **Success Rate Analysis**: Workflow success/failure tracking
- **Resource Monitoring**: CPU, memory, and database metrics
- **Historical Trends**: Performance over time analysis
- **Custom Reporting**: Configurable dashboards and exports

### Phase 4: Error Handling & Recovery
- **Error Monitoring**: Real-time error detection
- **Recovery Options**: Visual recovery strategies
- **Error Trends**: Pattern analysis and prediction
- **Alert System**: Configurable notifications
- **Prevention Tools**: Proactive error prevention

## 🚀 Development

### Running in Development Mode
```bash
python app.py
```

The application runs with debug mode enabled, providing:
- Auto-reload on code changes
- Detailed error messages
- Development-friendly logging

### Code Organization
- **app.py**: Main application logic and routes
- **templates/**: HTML templates with Jinja2
- **static/css/**: Custom CSS styling
- **static/js/**: JavaScript functionality
- **models/**: Data models (future implementation)

### Adding New Features
1. **Backend**: Add routes and logic in `app.py`
2. **Frontend**: Create templates in `templates/`
3. **Styling**: Add CSS in `static/css/main.css`
4. **Functionality**: Add JavaScript in `static/js/main.js`

## 🔍 Troubleshooting

### Common Issues

#### 1. Database Connection Error
```
Database error: no such table: workflow_states
```
**Solution**: Run the workflow system first to create the database, or check the database path in `app.py`.

#### 2. Port Already in Use
```
Address already in use
```
**Solution**: Change the port in `app.py` or stop other services using port 5000.

#### 3. WebSocket Connection Failed
**Solution**: Check if the application is running and accessible at the correct URL.

#### 4. Dependencies Not Found
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`.

### Debug Mode
The application runs in debug mode by default, providing:
- Detailed error messages
- Auto-reload on changes
- Development console output

## 📱 Browser Compatibility

- **Chrome**: 90+ (Recommended)
- **Firefox**: 88+
- **Safari**: 14+
- **Edge**: 90+

## 🔒 Security Notes

- **Development Mode**: Currently runs in debug mode
- **Database Access**: Direct SQLite access (consider connection pooling for production)
- **WebSocket**: CORS enabled for development
- **Authentication**: No authentication implemented (add for production use)

## 🚀 Production Deployment

For production deployment, consider:

1. **WSGI Server**: Use Gunicorn or uWSGI
2. **Reverse Proxy**: Nginx or Apache
3. **Environment Variables**: Configure via environment
4. **Database**: Use production database (PostgreSQL, MySQL)
5. **Authentication**: Implement user authentication
6. **HTTPS**: Enable SSL/TLS encryption
7. **Monitoring**: Add application monitoring and logging

## 🤝 Contributing

To contribute to the web UI:

1. **Fork the repository**
2. **Create a feature branch**
3. **Implement your changes**
4. **Test thoroughly**
5. **Submit a pull request**

## 📄 License

This project is part of the Agno Learning Series and follows the same license terms.

## 🆘 Support

For issues and questions:

1. **Check the troubleshooting section**
2. **Review the code and documentation**
3. **Create an issue in the repository**
4. **Contact the development team**

---

**🎉 Phase 1 Complete!** The foundation is ready for the advanced features coming in future phases.
