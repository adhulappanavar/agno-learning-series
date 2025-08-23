# Setup Guide for Example 3: Memory Agent

## Prerequisites
- Python 3.8+ installed
- OpenAI API key
- Understanding of Examples 1 & 2 (Basic Agent & Knowledge Agent)

## Quick Start

### 1. Install Dependencies
```bash
cd 03_memory_agent
pip install -r requirements.txt
```

### 2. Set Up Your API Key
Create a `.env` file in this directory:
```bash
cp ../01_basic_agent/env_example.txt .env
```

Then edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Run the Examples
```bash
# Run the memory demonstration
python memory_agent.py

# Test memory persistence across sessions
python memory_test.py

# Or start an interactive chat session
python run_example.py
```

## What You'll See

### Running `memory_agent.py`:
- Agent creation with memory and reasoning capabilities
- Three-part conversation demonstrating memory retention
- Session caching and context maintenance
- Advanced reasoning tool usage

### Running `memory_test.py`:
- Memory persistence test across sessions
- Verification that agent remembers previous conversations
- New information addition and recall testing

### Running `run_example.py`:
- Interactive chat with memory-enabled agent
- Session management and memory commands
- Real-time conversation with persistent context

## Understanding the Code

### Key Components:
1. **Memory System**: `enable_agentic_memory=True`, `enable_user_memories=True`
2. **Session Management**: `session_name`, `cache_session=True`
3. **Reasoning Tools**: `reasoning=True`, `reasoning_min_steps`, `reasoning_max_steps`
4. **History Integration**: `add_history_to_messages`, `num_history_responses`

### New Concepts from Previous Examples:
- **Level 3 Capabilities**: Memory, reasoning, and session persistence
- **Session Management**: Named sessions for context preservation
- **Memory References**: Automatic recall of previous conversations
- **Reasoning Workflows**: Step-by-step problem solving

### Agent Configuration:
- `enable_agentic_memory=True`: Enables agent memory system
- `enable_session_summaries=True`: Creates session summaries
- `add_memory_references=True`: References previous memories
- `reasoning=True`: Enables advanced reasoning capabilities

## Memory System Features

### What Gets Remembered:
- User preferences and personal information
- Project details and technical discussions
- Advice given and decisions made
- Conversation context and flow

### Session Persistence:
- Sessions are cached locally
- Memory persists across program restarts
- Multiple sessions can be maintained
- Context is automatically loaded

### Reasoning Capabilities:
- Step-by-step problem analysis
- Multi-step reasoning workflows
- Context-aware decision making
- Learning from conversation history

## Next Steps
After understanding this example, move to:
- `04_team_agents/` - Multi-agent teams (Level 4)
- `05_workflows/` - Complex agentic workflows (Level 5)

## Troubleshooting

### Common Issues:
1. **Memory Not Working**: Ensure all memory flags are set to `True`
2. **Session Issues**: Check that `session_name` is consistent
3. **API Key Errors**: Verify your OpenAI API key is correct
4. **Performance Issues**: Memory operations may add latency

### Performance Tips:
- Memory operations are cached for efficiency
- Session summaries reduce memory overhead
- Reasonable `reasoning_max_steps` prevents infinite loops
- Use specific session names for better organization

### Getting Help:
- Check the [Agno documentation](https://docs.agno.com)
- Visit the [community forum](https://community.agno.com)
- Join the [Discord server](https://discord.gg/agno)
