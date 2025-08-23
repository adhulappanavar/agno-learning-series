# Example 2: Knowledge Agent with Storage

This is the second example in the Agno learning series. We'll build a **Level 2** agent that has knowledge and storage capabilities.

## What You'll Learn
- How to create agents with knowledge bases
- How to use vector storage for information retrieval
- How to enable agents to learn and remember information
- How to build agents that can answer questions about specific domains

## What We're Building
A knowledge agent that can:
- Load documents into a knowledge base using Agno's built-in system
- Demonstrate knowledge storage capabilities
- Show how to structure documents for the knowledge system
- Provide a foundation for more advanced knowledge retrieval

**Note**: This example focuses on knowledge loading and basic retrieval. For production use with large document collections, you may want to configure a vector database like ChromaDB for optimal performance.

## Key Differences from Example 1
- **Level 1**: Basic tools and instructions
- **Level 2**: Knowledge storage and retrieval capabilities
- **New Features**: Vector database integration, document storage, semantic search

## Files
- `knowledge_agent.py` - The main agent code with knowledge capabilities
- `sample_documents/` - Sample documents to populate the knowledge base
- `requirements.txt` - Dependencies including vector database
- `run_example.py` - Script to test the knowledge agent
- `setup.md` - Setup and usage guide

## Example Output

When you run `python knowledge_agent.py`, you'll see:

```
🤖 Creating Knowledge Agent...
==================================================
✅ Agent 'Company Knowledge Agent' created successfully!
📋 Role: Expert assistant with access to company policies and technical documentation
🛠️  Tools: 1 tools available
📝 Instructions: 5 instructions set
🗄️  Knowledge: Built-in knowledge system enabled

📚 Loading documents into knowledge base...
✅ Loaded: company_policy.txt
✅ Loaded: technical_guide.txt
📚 Knowledge base populated successfully!

🧪 Testing the knowledge agent:
==================================================

❓ Question 1: What are the core work hours for remote employees?
----------------------------------------
🤖 Answer: I couldn't find specific documentation about core work hours for remote employees in our company's knowledge base...

❓ Question 2: How should I handle lost equipment?
----------------------------------------
🤖 Answer: It seems that there might not be any specific documentation in the company knowledge base regarding the handling of lost equipment...

❓ Question 3: What are the best practices for API authentication?
----------------------------------------
🤖 Answer: Here are some best practices for API authentication:

1. **Use OAuth 2.0:** OAuth 2.0 is a widely adopted framework for token-based authentication...
2. **Implement API Keys:** While not the most secure, API keys can be used for identification...
3. **Use JSON Web Tokens (JWT):** JWTs are a compact way to securely transmit information...

🎉 Knowledge agent example completed!
```

## Next Steps
After this example, you'll learn about:
- Agents with memory and reasoning (Level 3)
- Multi-agent teams (Level 4)
- Complex workflows (Level 5)
