# Setup Guide for Example 2: Knowledge Agent

## Prerequisites
- Python 3.8+ installed
- OpenAI API key
- Understanding of Example 1 (Basic Agent)

## Quick Start

### 1. Install Dependencies
```bash
cd 02_knowledge_agent
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

### 3. Run the Example
```bash
# Run the knowledge demonstration
python knowledge_agent.py

# Or start an interactive chat session
python run_example.py
```

## What You'll See

### Running `knowledge_agent.py`:
- Agent creation with ChromaDB storage
- Document loading into knowledge base
- Example questions and answers using stored knowledge
- Source citations from documents

### Running `run_example.py`:
- Interactive chat with knowledge-enabled agent
- Ask questions about company policies or technical topics
- See which documents are referenced
- Reload knowledge base with 'reload' command

## Understanding the Code

### Key Components:
1. **Built-in Knowledge System**: Agno's integrated knowledge capabilities
2. **Knowledge Loading**: `agent.add_to_knowledge()` method
3. **Document Processing**: Automatic text chunking and embedding
4. **Semantic Search**: Built-in similarity search for relevant information

### New Concepts from Example 1:
- **Level 2 Capabilities**: Knowledge storage and retrieval
- **Vector Database**: ChromaDB for efficient similarity search
- **Document Metadata**: Structured information about stored content
- **Source Citations**: References to original documents

### Agent Configuration:
- `search_knowledge=True`: Enables knowledge base functionality
- `update_knowledge=True`: Allows adding new information
- `add_references=True`: Provides source citations
- `add_to_knowledge()`: Method to populate knowledge base
- Automatic retrieval: Agent searches knowledge when answering questions

## Sample Documents

The example includes two sample documents:
1. **Company Policy**: Remote work guidelines and procedures
2. **Technical Guide**: API development best practices

These demonstrate how the agent can handle different types of content and provide domain-specific expertise.

## Next Steps
After understanding this example, move to:
- `03_memory_agent/` - Agents with memory and reasoning (Level 3)
- `04_team_agents/` - Multi-agent teams (Level 4)
- `05_workflows/` - Complex agentic workflows (Level 5)

## Troubleshooting

### Common Issues:
1. **Memory Issues**: Large documents may require more RAM
2. **API Key Errors**: Verify your OpenAI API key is correct
3. **Import Errors**: Ensure all requirements are installed
4. **Knowledge Loading**: Ensure documents are properly formatted

### Performance Tips:
- Knowledge is stored in memory during the session
- First run may be slower due to document processing
- Subsequent runs are faster due to cached knowledge
- Large documents are automatically chunked for efficiency

### Getting Help:
- Check the [Agno documentation](https://docs.agno.com)
- Visit the [community forum](https://community.agno.com)
- Join the [Discord server](https://discord.gg/agno)
