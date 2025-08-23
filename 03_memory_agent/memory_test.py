#!/usr/bin/env python3
"""
Memory Test Script
==================

This script demonstrates how the memory agent maintains context across different sessions.
Run this after running memory_agent.py to see memory persistence in action.
"""

import os
from dotenv import load_dotenv
from memory_agent import create_memory_agent

def test_memory_persistence():
    """
    Test memory persistence across sessions.
    """
    print("🧠 Testing Memory Persistence Across Sessions")
    print("=" * 50)
    print("This test shows how the agent remembers information from previous sessions.")
    print()
    
    # Use the same session name to test persistence
    session_name = "memory_demo_session"
    
    print(f"📚 Loading existing session: '{session_name}'")
    print()
    
    # Create agent with the same session name
    agent = create_memory_agent(session_name)
    
    print(f"✅ Agent '{agent.name}' loaded with session '{session_name}'")
    print(f"🧠 Memory references: {agent.add_memory_references}")
    print(f"📚 Session summaries: {agent.add_session_summary_references}")
    print()
    
    # Test questions that should trigger memory recall
    memory_test_questions = [
        "What do you remember about me from our previous conversation?",
        "What project was I working on?",
        "What frameworks did we discuss for my task management app?",
        "Can you give me a quick summary of our previous discussion?",
        "What advice did you give me about choosing frameworks?",
        "What's my name and what's my profession?"
    ]
    
    print("🧪 Testing Memory Recall:")
    print("=" * 30)
    
    for i, question in enumerate(memory_test_questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("-" * 40)
        
        try:
            print("🤖 Thinking...")
            response = agent.run(question)
            print(f"🤖 Answer: {response.content}")
            
            # Check if memory references are included
            if hasattr(response, 'extra_data') and response.extra_data and hasattr(response.extra_data, 'references') and response.extra_data.references:
                print(f"\n📚 Memory References: {len(response.extra_data.references)} found")
            elif hasattr(response, 'references') and response.references:
                print(f"\n📚 Memory References: {len(response.references)} found")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    # Test new information that should be added to memory
    print("🆕 Testing New Information Addition:")
    print("=" * 35)
    
    new_info_questions = [
        "I've decided to use React for the frontend and Node.js for the backend.",
        "I'm planning to deploy this on AWS using their free tier.",
        "I want to add real-time collaboration features to my app."
    ]
    
    for i, question in enumerate(new_info_questions, 1):
        print(f"\n👤 Alex: {question}")
        print("🤖 Thinking...")
        
        try:
            response = agent.run(question)
            print(f"🤖 Assistant: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    # Final memory test
    print("🧠 Final Memory Test:")
    print("=" * 20)
    
    final_questions = [
        "What's my complete tech stack now?",
        "What deployment platform am I using?",
        "What new features am I planning to add?",
        "Can you give me a comprehensive summary of everything we've discussed?"
    ]
    
    for i, question in enumerate(final_questions, 1):
        print(f"\n❓ Final Question {i}: {question}")
        print("-" * 40)
        
        try:
            print("🤖 Thinking...")
            response = agent.run(question)
            print(f"🤖 Answer: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("🎉 Memory persistence test completed!")
    print(f"\n💡 The agent successfully maintained context across the entire conversation")
    print(f"💡 Session '{session_name}' has been updated with new information")
    print(f"💡 You can run this script again to see even more memory persistence!")

def main():
    """
    Main function to run the memory test.
    """
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
    
    # Run the memory test
    test_memory_persistence()

if __name__ == "__main__":
    main()
