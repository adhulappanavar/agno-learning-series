# Workflow Visualization Web UI

A modern, interactive web interface for visualizing and managing Agno workflows with real-time monitoring and control capabilities.

## 🎯 **Current Status: Phase 2 Complete!** ✅

### **Phase 1: Foundation** ✅ COMPLETED
- ✅ Flask web application with SocketIO
- ✅ Responsive Bootstrap 5 UI
- ✅ Real-time dashboard with statistics
- ✅ Database integration and API endpoints
- ✅ WebSocket communication setup
- ✅ Navigation and routing structure

### **Phase 2: Interactive Workflow Visualization** ✅ COMPLETED
- ✅ **Interactive workflow diagrams** with stage-by-stage visualization
- ✅ **Real-time workflow monitoring** with live status updates
- ✅ **Workflow execution controls** (Play, Pause, Stop, Step)
- ✅ **Detailed stage information** with data inspection
- ✅ **Visual workflow designer** with 5-stage workflow structure
- ✅ **Execution progress tracking** with animated progress bars
- ✅ **Enhanced WebSocket events** for real-time communication
- ✅ **Responsive workflow cards** with hover effects and animations
- ✅ **Stage status indicators** with color-coded visual feedback
- ✅ **Workflow selection and management** interface

### **Phase 3: Performance Metrics Dashboard** 🚧 PLANNED
- 📊 Performance metrics and analytics
- 📈 Historical data visualization
- 📉 Trend analysis and reporting
- 🎯 Custom metric definitions

### **Phase 4: Error Handling & Recovery** 🚧 PLANNED
- 🚨 Error monitoring and visualization
- 🔄 Recovery options and automation
- 📊 Error trends and analysis
- ⚠️ Alert system and notifications

### **Phase 5: Advanced Features** 🚧 PLANNED
- 🎨 Workflow designer with drag-and-drop
- 🎮 Simulation mode for testing
- 📤 Export/Import functionality
- 👥 User management and permissions

### **Phase 6: Polish & Testing** 🚧 PLANNED
- 🧪 Comprehensive testing suite
- 🎨 UI/UX refinements
- 📱 Mobile optimization
- 🚀 Performance optimization

## 🚀 **Phase 2 Features in Detail**

### **Interactive Workflow Diagrams**
- **5-Stage Workflow Structure**: Planning → Data Processing → Business Logic → Approval → Finalization
- **Visual Stage Representation**: Each stage shows current status with color-coded indicators
- **Real-time Updates**: Live status changes via WebSocket communication
- **Stage Navigation**: Click on stages to view detailed information

### **Workflow Execution Controls**
- **Play Button**: Start workflow execution with progress simulation
- **Pause Button**: Pause execution (simulated)
- **Stop Button**: Stop execution (simulated)
- **Step Button**: Execute next stage (simulated)

### **Enhanced User Interface**
- **Responsive Design**: Works on all device sizes
- **Smooth Animations**: Hover effects, transitions, and loading states
- **Color-coded Status**: Visual indicators for different workflow states
- **Interactive Elements**: Hover effects and clickable components

### **Real-time Communication**
- **WebSocket Events**: Live updates for workflow status changes
- **Execution Progress**: Real-time progress bars and status updates
- **Error Handling**: Immediate feedback for user actions
- **Connection Status**: Visual indicators for WebSocket connection

## 🛠️ **Installation & Setup**

### **Prerequisites**
- Python 3.8+
- SQLite3
- Modern web browser

### **Installation Steps**
```bash
# Navigate to the web UI directory
cd 05_workflows/web_ui

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### **Access the Web UI**
- **Main Dashboard**: http://localhost:5000
- **Workflows**: http://localhost:5000/workflow
- **Metrics**: http://localhost:5000/metrics
- **Errors**: http://localhost:5000/errors

## 📁 **Project Structure**

```
web_ui/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── test_web_ui.py        # Testing script
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── dashboard.html    # Main dashboard
│   ├── workflow.html     # Phase 2: Interactive workflows
│   ├── metrics.html      # Phase 3: Metrics dashboard
│   └── errors.html       # Phase 4: Error handling
├── static/               # Static assets
│   ├── css/
│   │   └── main.css      # Phase 2: Enhanced styles
│   └── js/
│       └── main.js       # Common JavaScript functions
└── models/               # Data models (future use)
```

## 🔧 **Configuration**

### **Environment Variables**
Create a `.env` file in the parent directory (`05_workflows/`):
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### **Database**
The web UI automatically connects to the `workflow_states.db` SQLite database in the parent directory.

## 🎮 **How to Use Phase 2 Features**

### **1. View Workflows**
- Navigate to the **Workflows** page
- See all available workflows in interactive cards
- Each card shows workflow type, status, and current stage

### **2. Visualize Workflow Stages**
- Click on any workflow card to select it
- Click the **Diagram** button to view the 5-stage workflow
- See real-time stage status with color-coded indicators

### **3. Control Workflow Execution**
- Use the execution controls (Play, Pause, Stop, Step)
- Watch real-time progress updates
- Monitor execution status and completion

### **4. Inspect Workflow Details**
- Click the **View** button on any workflow card
- See detailed workflow information
- Inspect stage data and metadata

## 🧪 **Testing**

Run the comprehensive test suite:
```bash
cd 05_workflows/web_ui
python test_web_ui.py
```

This will test:
- ✅ File structure and dependencies
- ✅ Flask application configuration
- ✅ Template syntax and rendering
- ✅ CSS and JavaScript syntax
- ✅ Database connectivity
- ✅ WebSocket functionality

## 🐛 **Troubleshooting**

### **Common Issues**

#### **WebSocket Connection Failed**
- Check if the Flask app is running
- Ensure no firewall blocking port 5000
- Check browser console for connection errors

#### **Database Errors**
- Verify `workflow_states.db` exists in parent directory
- Check database permissions
- Ensure SQLite3 is installed

#### **Template Rendering Errors**
- Check for syntax errors in HTML templates
- Verify all required variables are passed
- Check Jinja2 template syntax

### **Debug Mode**
The application runs in debug mode by default. Check the terminal for detailed error messages and stack traces.

## 🚀 **Next Steps**

### **Immediate Actions**
1. **Test Phase 2 Features**: Navigate to `/workflow` and explore the interactive visualization
2. **Run Sample Workflows**: Execute the `05_workflows` example to populate the database
3. **Explore Real-time Updates**: Watch WebSocket events in browser console

### **Future Development**
- **Phase 3**: Implement performance metrics dashboard
- **Phase 4**: Add error handling and recovery visualization
- **Phase 5**: Build advanced workflow designer features
- **Phase 6**: Polish and optimize the entire system

## 🎉 **Phase 2 Complete!**

**Phase 2: Interactive Workflow Visualization** is now fully implemented and ready for use! 

The web UI now provides:
- 🎯 **Interactive workflow diagrams** with real-time updates
- 🎮 **Execution controls** for workflow management
- 📊 **Visual stage monitoring** with status indicators
- 🔄 **Real-time communication** via WebSocket
- 🎨 **Modern, responsive interface** with smooth animations

**Ready to explore the interactive workflow visualization?** Navigate to the Workflows page and start visualizing your Agno workflows!

---

**🎯 Phase 2 Status: COMPLETE** ✅  
**🚀 Ready for Phase 3: Performance Metrics Dashboard**
