#!/usr/bin/env python3
"""
Interactive script to test the basic agent.
Run this to chat with your agent!
"""

import os
from dotenv import load_dotenv
from basic_agent import create_basic_agent

def interactive_chat():
    """
    Start an interactive chat session with the agent.
    """
    print("🤖 Welcome to Agno Basic Agent!")
    print("=" * 40)
    print("Type 'quit' or 'exit' to end the session")
    print("Type 'help' to see available commands")
    print()
    
    # Create the agent
    agent = create_basic_agent()
    print(f"✅ Agent '{agent.name}' is ready!")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye! Thanks for trying Agno!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print("\n📚 Available Commands:")
                print("  - Type any question to get an answer")
                print("  - 'help' - Show this help message")
                print("  - 'quit' or 'exit' - End the session")
                print("  - 'tools' - Show available tools")
                print()
                continue
            
            # Check for tools command
            if user_input.lower() == 'tools':
                print(f"\n🛠️  Available Tools ({len(agent.tools)}):")
                for i, tool in enumerate(agent.tools, 1):
                    print(f"  {i}. {tool.__class__.__name__}")
                print()
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            print("🤖 Thinking...")
            
            # Get response from agent
            response = agent.run(user_input)
            
            print(f"🤖 Agent: {response.content}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for trying Agno!")
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
