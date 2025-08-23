# Setup Guide for Team Agents Example

This guide will help you set up and run the Team Agents (Level 4) example.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Basic understanding of Python

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the `04_team_agents` directory:

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 3. Verify Installation

Check that all packages are installed correctly:

```bash
python -c "import agno; print('Agno version:', agno.__version__)"
```

## Running the Example

### Basic Team Demonstration

```bash
python team_agents.py
```

This will:
- Create a team of 4 specialized agents
- Demonstrate team collaboration on a project scenario
- Show how agents work together to solve complex problems

### Extended Team Testing

```bash
python team_test.py
```

This comprehensive test suite will:
- Test individual agent capabilities
- Demonstrate team problem-solving
- Show agent memory and learning
- Test cross-agent consultation

## What You'll See

### Team Structure
- **Project Manager**: Coordinates team efforts and manages timelines
- **Developer**: Handles technical implementation and architecture
- **Designer**: Focuses on user experience and interface design
- **QA Tester**: Ensures quality and testing strategies

### Key Features Demonstrated
- **Multi-agent collaboration** on complex problems
- **Specialized expertise** from each agent
- **Team coordination** and communication
- **Memory persistence** across conversations
- **Interdisciplinary problem-solving**

## Customization

### Adding New Agents

You can create new agents by following the pattern in the code:

```python
def create_new_agent():
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="new_memories", db_file="memory_new.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="New Agent Name",
        role="Description of the agent's role",
        model=OpenAIChat(id="gpt-4o"),
        tools=[...],
        instructions=[...],
        memory=memory,
        user_id="new_agent",
        # ... other configurations
    )
    
    return agent
```

### Modifying Team Instructions

Update the team instructions in `create_team()` function to change how agents collaborate:

```python
team = Team(
    name="Your Team Name",
    agents=[...],
    instructions=[
        "Your custom team instructions here",
        "Define how agents should work together",
        "Set collaboration protocols"
    ]
)
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed correctly
2. **API Key Issues**: Verify your `.env` file contains the correct OpenAI API key
3. **Memory Database Errors**: Check file permissions in the directory
4. **Team Collaboration Errors**: Some team features may fall back to individual responses

### Performance Tips

- **Memory Management**: Each agent has its own memory database for optimal performance
- **Team Size**: Keep teams manageable (4-6 agents) for best collaboration
- **Session Management**: Use consistent session names for better memory retention

## Next Steps

After mastering this example, explore:
- **Example 5**: Workflows (Level 5) - Complex agentic workflows
- **Custom Team Configurations**: Build teams for specific domains
- **Advanced Collaboration**: Implement custom team protocols and workflows

## Resources

- [Agno Documentation](https://github.com/agno-agi/agno)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Team Collaboration Best Practices](https://github.com/agno-agi/agno/tree/main/cookbook/teams)
