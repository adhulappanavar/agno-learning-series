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
🤖 Assistant: Nice to meet you, Alex! I understand you're a software developer working with Python and JavaScript...

👤 Alex: I'm planning to build a web application for task management.
🤖 Thinking...
🤖 Assistant: That sounds like an exciting project! A task management web application is a great way to apply your Python and JavaScript skills...

👤 Alex: What should I consider when choosing between different frameworks?
🤖 Thinking...
🤖 Assistant: When choosing frameworks for your task management app, consider these factors...

🗣️  Second Conversation - Testing Memory:
----------------------------------------

👤 Alex: What's my name and what do I do?
🤖 Thinking...
🤖 Assistant: Your name is Alex, and you're a software developer who works with Python and JavaScript...

👤 Alex: What project am I working on?
🤖 Thinking...
🤖 Assistant: You're working on building a web application for task management...

🎉 Memory agent demonstration completed!
💡 The agent has maintained context across 10 questions
💡 Session 'memory_demo_session' has been cached for future use
```

## Next Steps
After this example, you'll learn about:
- Multi-agent teams (Level 4)
- Complex workflows (Level 5)
