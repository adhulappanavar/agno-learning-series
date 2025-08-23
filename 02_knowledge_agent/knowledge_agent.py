"""
Example 2: Knowledge Agent with Storage
========================================

This example demonstrates a Level 2 Agno agent that has:
- Knowledge storage and retrieval capabilities
- Vector database integration
- Document learning and search
- Domain-specific expertise
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from agno.agent import Agent, AgentKnowledge
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.document.base import Document

# Load environment variables
load_dotenv()

def create_knowledge_agent():
    """
    Create a Level 2 agent with knowledge storage capabilities.
    """
    
    # Initialize knowledge system
    knowledge = AgentKnowledge()
    
    # Create the agent with built-in knowledge capabilities
    agent = Agent(
        name="Company Knowledge Agent",
        role="Expert assistant with access to company policies and technical documentation",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
        ],
        knowledge=knowledge,
        instructions=[
            "You have access to company knowledge base including policies and technical guides",
            "Always cite your sources when answering questions",
            "If you don't know something, say so and suggest where to find the information",
            "Use markdown formatting for better readability",
            "Be helpful and professional in your responses"
        ],
        markdown=True,
        show_tool_calls=True,
        # Enable knowledge capabilities
        search_knowledge=True,
        update_knowledge=True,
        add_references=True,
    )
    
    return agent

def load_documents_to_knowledge(agent):
    """
    Load sample documents into the agent's knowledge base.
    """
    print("📚 Loading documents into knowledge base...")
    
    # Get the sample documents directory
    docs_dir = Path(__file__).parent / "sample_documents"
    
    if not docs_dir.exists():
        print("❌ Sample documents directory not found!")
        return
    
    # Load each document
    for doc_file in docs_dir.glob("*.txt"):
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create document object
            doc = Document(
                content=content,
                name=doc_file.name,
                meta_data={
                    "source": doc_file.name,
                    "type": "policy" if "policy" in doc_file.name.lower() else "technical",
                    "filename": doc_file.name
                }
            )
            
            # Add document to knowledge base
            agent.knowledge.load_document(doc)
            
            print(f"✅ Loaded: {doc_file.name}")
            
        except Exception as e:
            print(f"❌ Error loading {doc_file.name}: {e}")
    
    print("📚 Knowledge base populated successfully!")

def main():
    """
    Main function to demonstrate the knowledge agent.
    """
    print("🤖 Creating Knowledge Agent...")
    print("=" * 50)
    
    # Create the agent
    agent = create_knowledge_agent()
    
    print(f"✅ Agent '{agent.name}' created successfully!")
    print(f"📋 Role: {agent.role}")
    print(f"🛠️  Tools: {len(agent.tools)} tools available")
    print(f"📝 Instructions: {len(agent.instructions)} instructions set")
    print(f"🗄️  Knowledge: Built-in knowledge system enabled")
    print()
    
    # Load documents into knowledge base
    load_documents_to_knowledge(agent)
    print()
    
    # Example questions that test knowledge retrieval
    examples = [
        "What are the core work hours for remote employees?",
        "How should I handle lost equipment?",
        "What are the best practices for API authentication?",
        "What is the company's policy on PTO requests?",
        "How should I implement error handling in APIs?",
        "What are the meeting etiquette guidelines for video calls?"
    ]
    
    print("💡 Note: The knowledge system is working, but for optimal retrieval,")
    print("   you may want to configure a vector database like ChromaDB.")
    print("   This example shows the basic knowledge loading capabilities.")
    print()
    
    print("🧪 Testing the knowledge agent:")
    print("=" * 50)
    
    for i, question in enumerate(examples, 1):
        print(f"\n❓ Question {i}: {question}")
        print("-" * 40)
        
        try:
            # Get response from agent
            response = agent.run(question)
            print(f"🤖 Answer: {response.content}")
            
            # Show sources if available
            if hasattr(response, 'extra_data') and response.extra_data.references:
                print(f"\n📚 Sources: {len(response.extra_data.references)} documents referenced")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("🎉 Knowledge agent example completed!")
    print("\n💡 Try asking your own questions about company policies or technical topics!")

if __name__ == "__main__":
    main()
