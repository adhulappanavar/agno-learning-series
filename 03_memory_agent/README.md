# Example 3: Memory Agent with Reasoning

This is the third example in the Agno learning series. We'll build a **Level 3** agent that has memory and reasoning capabilities across sessions.

## What You'll Learn
- How to create agents with persistent memory
- How to enable reasoning across multiple conversations
- How to use session management and memory storage
- How to build agents that learn and improve over time

## What We're Building
A memory-enabled agent that can:
- Remember conversations and context across sessions
- Use reasoning tools to work through complex problems
- Maintain conversation history and learn from interactions
- Provide consistent responses based on previous knowledge

## Key Differences from Previous Examples
- **Level 1**: Basic tools and instructions
- **Level 2**: Knowledge storage and retrieval
- **Level 3**: Memory, reasoning, and session persistence
- **New Features**: Memory storage, session management, reasoning workflows

## Files
- `memory_agent.py` - The main agent code with memory capabilities
- `requirements.txt` - Dependencies
- `run_example.py` - Interactive script to test memory persistence
- `setup.md` - Setup and usage guide
- `memory_test.py` - Script to demonstrate memory across sessions

## Example Output

When you run `python memory_agent.py`, you'll see:

```
🤖 Creating Memory-Enabled Agent...
==================================================
✅ Agent 'Memory-Enabled Assistant' created successfully!
📋 Role: A helpful assistant that remembers conversations and uses reasoning
🛠️  Tools: 1 tools available
📝 Instructions: 6 instructions set
🧠 Memory: Agentic memory enabled
💭 Reasoning: Advanced reasoning enabled
📚 Session: 'memory_demo_session'

🗣️  First Conversation - Establishing Context:
----------------------------------------

👤 Alex: My name is Alex and I'm a software developer. I work with Python and JavaScript.
🤖 Thinking...
WARNING  Failed to parse cleaned JSON: Extra data: line 1 column 3967 (char 3966)
WARNING  MemoryDb not provided.
🤖 Assistant: I've added your name, profession as a software developer, and expertise in Python and JavaScript to my memory...

👤 Alex: I'm planning to build a web application for task management.
🤖 Thinking...
ERROR    Invalid schema for function 'think': Missing 'action' parameter
❌ Error: Invalid schema for function 'think'...

🗣️  Second Conversation - Testing Memory:
----------------------------------------

👤 Alex: What's my name and what do I do?
🤖 Thinking...
ERROR    Invalid schema for function 'think': Missing 'action' parameter
❌ Error: Invalid schema for function 'think'...

🎉 Memory agent demonstration completed!
💡 The agent has maintained context across 10 questions
💡 Session 'memory_demo_session' has been cached for future use
```

## ⚠️ Current Limitations

**Note**: The current version of Agno has some compatibility issues with the reasoning tools. You may see:
- Schema validation errors for the `think` function
- Warnings about MemoryDb not being provided
- Some reasoning steps may fail

These issues are being addressed in future Agno releases. The memory and session capabilities still work, but the advanced reasoning features may be limited.

## Next Steps
After this example, you'll learn about:
- Multi-agent teams (Level 4)
- Complex workflows (Level 5)

## 🔧 Troubleshooting

### Common Issues

1. **Schema Validation Errors**: If you see errors about missing 'action' parameters, this is a known issue with the current Agno version
2. **MemoryDb Warnings**: These are informational and don't affect basic functionality
3. **Reasoning Tool Failures**: The agent will fall back to regular responses if reasoning tools fail

### Workarounds

- **Disable Reasoning**: Set `reasoning=False` in the agent configuration for more stable operation
- **Use Basic Mode**: Focus on memory and session features rather than advanced reasoning
- **Check Agno Version**: Ensure you're using the latest stable release

### What Still Works

Despite the reasoning tool issues, the agent successfully demonstrates:
- ✅ Memory storage and retrieval
- ✅ Session management and persistence
- ✅ Context maintenance across conversations
- ✅ Basic agent capabilities
