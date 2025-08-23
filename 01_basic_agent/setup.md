# Setup Guide for Example 1

## Prerequisites
- Python 3.8+ installed
- OpenAI API key

## Quick Start

### 1. Install Dependencies
```bash
cd 01_basic_agent
pip install -r requirements.txt
```

### 2. Set Up Your API Key
Create a `.env` file in this directory:
```bash
cp env_example.txt .env
```

Then edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Run the Example
```bash
# Run the basic demonstration
python basic_agent.py

# Or start an interactive chat session
python run_example.py
```

## What You'll See

### Running `basic_agent.py`:
- Agent creation process
- Example questions and answers
- Tool usage demonstration

### Running `run_example.py`:
- Interactive chat interface
- Ask your own questions
- See which tools the agent uses

## Understanding the Code

### Key Components:
1. **Agent Creation**: `Agent()` class with name, role, model, and tools
2. **Tools**: `ReasoningTools` and `CalculatorTools` for problem-solving
3. **Instructions**: Clear guidelines for how the agent should behave
4. **Model**: OpenAI's GPT-4o for reasoning capabilities

### Agent Configuration:
- `markdown=True`: Enables formatted output
- `show_tool_calls=True`: Shows which tools are being used
- `add_instructions=True`: Enhances reasoning capabilities
- `agent.run()`: Method to get responses from the agent

## Next Steps
After understanding this example, move to:
- `02_knowledge_agent/` - Agents with knowledge and storage
- `03_memory_agent/` - Agents with memory and reasoning
- `04_team_agents/` - Multi-agent teams
- `05_workflows/` - Complex agentic workflows

## Troubleshooting

### Common Issues:
1. **API Key Error**: Make sure your `.env` file has the correct API key
2. **Import Errors**: Ensure you've installed all requirements
3. **Rate Limits**: OpenAI has usage limits - check your account

### Getting Help:
- Check the [Agno documentation](https://docs.agno.com)
- Visit the [community forum](https://community.agno.com)
- Join the [Discord server](https://discord.gg/agno)
