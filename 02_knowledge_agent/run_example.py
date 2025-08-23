#!/usr/bin/env python3
"""
Interactive script to test the knowledge agent.
Run this to chat with your knowledge-enabled agent!
"""

import os
from dotenv import load_dotenv
from knowledge_agent import create_knowledge_agent, load_documents_to_knowledge

def interactive_chat():
    """
    Start an interactive chat session with the knowledge agent.
    """
    print("🤖 Welcome to Agno Knowledge Agent!")
    print("=" * 45)
    print("This agent has access to company policies and technical documentation.")
    print("Type 'quit' or 'exit' to end the session")
    print("Type 'help' to see available commands")
    print("Type 'reload' to reload the knowledge base")
    print()
    
    # Create the agent
    agent = create_knowledge_agent()
    print(f"✅ Agent '{agent.name}' is ready!")
    print()
    
    # Load documents into knowledge base
    load_documents_to_knowledge(agent)
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye! Thanks for trying the Knowledge Agent!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print("\n📚 Available Commands:")
                print("  - Type any question to get an answer")
                print("  - 'help' - Show this help message")
                print("  - 'quit' or 'exit' - End the session")
                print("  - 'reload' - Reload the knowledge base")
                print("  - 'tools' - Show available tools")
                print("  - 'knowledge' - Show knowledge base info")
                print()
                continue
            
            # Check for reload command
            if user_input.lower() == 'reload':
                print("🔄 Reloading knowledge base...")
                load_documents_to_knowledge(agent)
                print()
                continue
            
            # Check for tools command
            if user_input.lower() == 'tools':
                print(f"\n🛠️  Available Tools ({len(agent.tools)}):")
                for i, tool in enumerate(agent.tools, 1):
                    print(f"  {i}. {tool.__class__.__name__}")
                print()
                continue
            
            # Check for knowledge command
            if user_input.lower() == 'knowledge':
                try:
                    # Show info about the knowledge base
                    print(f"\n🗄️  Knowledge Base Info:")
                    print(f"  Knowledge System: Built-in Agno knowledge")
                    print(f"  Search Enabled: {agent.search_knowledge}")
                    print(f"  Update Enabled: {agent.update_knowledge}")
                    print("  Sample documents loaded:")
                    
                    docs_dir = os.path.join(os.path.dirname(__file__), "sample_documents")
                    if os.path.exists(docs_dir):
                        for file in os.listdir(docs_dir):
                            if file.endswith('.txt'):
                                print(f"    - {file}")
                    print()
                except Exception as e:
                    print(f"❌ Error getting knowledge info: {e}")
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            print("🤖 Searching knowledge base...")
            
            # Get response from agent
            response = agent.run(user_input)
            
            print(f"🤖 Agent: {response.content}")
            
            # Show sources if available
            if hasattr(response, 'extra_data') and response.extra_data.references:
                print(f"\n📚 Sources: {len(response.extra_data.references)} documents referenced")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for trying the Knowledge Agent!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Make sure you have set your OpenAI API key in the .env file")
            print()

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment!")
        print("💡 Please create a .env file with your OpenAI API key:")
        print("   OPENAI_API_KEY=your_api_key_here")
        print()
        print("🔗 Get your API key from: https://platform.openai.com/api-keys")
        exit(1)
    
    # Start interactive chat
    interactive_chat()
