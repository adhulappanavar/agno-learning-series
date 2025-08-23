# Agno Learning Series

A comprehensive learning path for building AI agents with the [Agno framework](https://github.com/agno-agi/agno).

## 🎯 What You'll Learn

This series teaches you how to build increasingly sophisticated AI agents, from basic tools to complex multi-agent systems:

- **Level 1**: Basic agents with tools and instructions
- **Level 2**: Agents with knowledge storage and retrieval
- **Level 3**: Agents with memory and reasoning across sessions
- **Level 4**: Multi-agent teams and collaboration
- **Level 5**: Complex agentic workflows with state management

## 📁 Project Structure

```
agno/
├── 01_basic_agent/          # Level 1: Basic tools and instructions
├── 02_knowledge_agent/      # Level 2: Knowledge storage and retrieval
├── 03_memory_agent/         # Level 3: Memory and reasoning
├── 04_team_agents/          # Level 4: Multi-agent teams (coming soon)
├── 05_workflows/            # Level 5: Complex workflows (coming soon)
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key
- Basic Python knowledge

### Quick Start
1. **Clone this repository**:
   ```bash
   git clone <your-repo-url>
   cd agno
   ```

2. **Start with Example 1**:
   ```bash
   cd 01_basic_agent
   cp env_example.txt .env
   # Edit .env with your OpenAI API key
   pip install -r requirements.txt
   python basic_agent.py
   ```

3. **Progress through the examples** in order to build your understanding

## 📚 Learning Path

### Example 1: Basic Agent
Learn the fundamentals of Agno agents:
- Creating agents with tools
- Setting instructions and behavior
- Basic agent interaction patterns

**Files**: `basic_agent.py`, `run_example.py`, `setup.md`
**Sample Output**: Included in README showing calculation and reasoning examples

### Example 2: Knowledge Agent
Build agents that can learn and remember:
- Document loading and storage
- Knowledge base management
- Information retrieval capabilities

**Files**: `knowledge_agent.py`, `run_example.py`, `sample_documents/`
**Sample Output**: Included in README showing knowledge loading and Q&A examples

### Example 3: Memory Agent
Create agents with persistent memory:
- Session management and persistence
- Memory across conversations
- Advanced reasoning workflows

**Files**: `memory_agent.py`, `memory_test.py`, `run_example.py`
**Sample Output**: Included in README showing memory and reasoning capabilities

### Example 4: Team Agents (Coming Soon)
Learn multi-agent collaboration:
- Agent teams and coordination
- Task distribution and delegation
- Team-based problem solving

### Example 5: Workflows (Coming Soon)
Build complex agentic systems:
- State management and workflows
- Multi-step processes
- Production-ready agent systems

## 🔑 Configuration

Each example requires an OpenAI API key. Create a `.env` file in each example directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Never commit your `.env` files! They're already excluded by `.gitignore`.

**Note**: You'll need to create a `.env` file in each example directory (`01_basic_agent/`, `02_knowledge_agent/`, `03_memory_agent/`) with your OpenAI API key.

## 🛠️ Development

### Adding New Examples
1. Create a new directory: `04_team_agents/`
2. Follow the established pattern:
   - `README.md` - Learning objectives
   - `requirements.txt` - Dependencies
   - `main_agent.py` - Core agent code
   - `run_example.py` - Interactive testing
   - `setup.md` - Setup guide

### Testing
Each example includes:
- **Main script**: Demonstrates core functionality
- **Interactive script**: Allows custom testing
- **Setup guide**: Complete configuration instructions

## 📖 Resources

- [Agno Documentation](https://docs.agno.com)
- [Agno GitHub Repository](https://github.com/agno-agi/agno)
- [Community Forum](https://community.agno.com)
- [Discord Server](https://discord.gg/agno)

## 🤝 Contributing

This is a learning resource - feel free to:
- Improve examples
- Add new learning paths
- Fix bugs or clarify instructions
- Share your own examples

## 📄 License

This project is for educational purposes. The Agno framework is licensed under MPL-2.0.

## 🆘 Getting Help

- **Example Issues**: Check the `setup.md` in each example directory
- **Agno Questions**: Visit the [community forum](https://community.agno.com)
- **General Help**: Join the [Discord server](https://discord.gg/agno)

---

**Happy Learning! 🚀**

Build amazing AI agents with Agno!
