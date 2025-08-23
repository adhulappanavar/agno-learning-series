#!/usr/bin/env python3
"""
Interactive script to test the memory agent.
Run this to have a conversation with your memory-enabled agent!
"""

import os
from dotenv import load_dotenv
from memory_agent import create_memory_agent

def interactive_chat():
    """
    Start an interactive chat session with the memory agent.
    """
    print("🧠 Welcome to Agno Memory Agent!")
    print("=" * 40)
    print("This agent remembers our conversations and uses reasoning tools.")
    print("Type 'quit' or 'exit' to end the session")
    print("Type 'help' to see available commands")
    print("Type 'session' to see current session info")
    print("Type 'memory' to see memory capabilities")
    print()
    
    # Get session name from user
    session_name = input("Enter a session name (or press Enter for default): ").strip()
    if not session_name:
        session_name = "interactive_session"
    
    print(f"📚 Starting session: '{session_name}'")
    print()
    
    # Create the agent with the specified session
    agent = create_memory_agent(session_name)
    print(f"✅ Agent '{agent.name}' is ready!")
    print(f"🧠 Memory enabled: {agent.enable_agentic_memory}")
    print(f"💭 Reasoning enabled: {agent.reasoning}")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye! Your conversation has been saved to memory.")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print("\n📚 Available Commands:")
                print("  - Type any question to get an answer")
                print("  - 'help' - Show this help message")
                print("  - 'quit' or 'exit' - End the session")
                print("  - 'session' - Show current session info")
                print("  - 'memory' - Show memory capabilities")
                print("  - 'tools' - Show available tools")
                print("  - 'summary' - Get conversation summary")
                print()
                continue
            
            # Check for session command
            if user_input.lower() == 'session':
                print(f"\n📚 Session Information:")
                print(f"  Session Name: {agent.session_name}")
                print(f"  Session ID: {agent.session_id}")
                print(f"  Cache Enabled: {agent.cache_session}")
                print(f"  History Responses: {agent.num_history_responses}")
                print(f"  History Sessions: {agent.num_history_sessions}")
                print()
                continue
            
            # Check for memory command
            if user_input.lower() == 'memory':
                print(f"\n🧠 Memory Capabilities:")
                print(f"  Agentic Memory: {agent.enable_agentic_memory}")
                print(f"  User Memories: {agent.enable_user_memories}")
                print(f"  Session Summaries: {agent.enable_session_summaries}")
                print(f"  Memory References: {agent.add_memory_references}")
                print(f"  Session Summary References: {agent.add_session_summary_references}")
                print()
                continue
            
            # Check for tools command
            if user_input.lower() == 'tools':
                print(f"\n🛠️  Available Tools ({len(agent.tools)}):")
                for i, tool in enumerate(agent.tools, 1):
                    print(f"  {i}. {tool.__class__.__name__}")
                print()
                continue
            
            # Check for summary command
            if user_input.lower() == 'summary':
                print("\n📝 Getting conversation summary...")
                try:
                    # Try to get a summary of our conversation
                    summary_response = agent.run("Can you give me a brief summary of our conversation so far?")
                    print(f"🤖 Summary: {summary_response.content}")
                except Exception as e:
                    print(f"❌ Error getting summary: {e}")
                print()
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            print("🤖 Thinking...")
            
            # Get response from agent
            response = agent.run(user_input)
            
            print(f"🤖 Assistant: {response.content}")
            
            # Show memory references if available
            if hasattr(response, 'extra_data') and response.extra_data.references:
                print(f"\n📚 Memory References: {len(response.extra_data.references)} found")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Your conversation has been saved to memory.")
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
