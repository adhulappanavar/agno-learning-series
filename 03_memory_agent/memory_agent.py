"""
Example 3: Memory Agent with Reasoning
======================================

This example demonstrates a Level 3 Agno agent that has:
- Memory capabilities across sessions
- Advanced reasoning tools
- Session persistence and management
- Learning from conversation history
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools

# Load environment variables
load_dotenv()

def create_memory_agent(session_name=None):
    """
    Create a Level 3 agent with memory and reasoning capabilities.
    
    Args:
        session_name: Optional name for the session. If None, a new session is created.
    """
    
    # Create the agent with memory and reasoning capabilities
    agent = Agent(
        name="Memory-Enabled Assistant",
        role="A helpful assistant that remembers conversations and uses reasoning",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
        ],
        instructions=[
            "You have memory of our previous conversations",
            "Use reasoning tools to work through complex problems step by step",
            "Reference previous discussions when relevant",
            "Be consistent with your previous advice",
            "Learn from our conversation history to provide better responses",
            "Use markdown formatting for better readability"
        ],
        markdown=True,
        show_tool_calls=True,
        # Enable memory capabilities
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
        add_memory_references=True,
        add_session_summary_references=True,
        # Enable reasoning
        reasoning=True,
        reasoning_min_steps=2,
        reasoning_max_steps=8,
        # Session management
        session_name=session_name,
        cache_session=True,
        add_history_to_messages=True,
        num_history_responses=5,
        num_history_sessions=3,
    )
    
    return agent

def demonstrate_memory_capabilities():
    """
    Demonstrate the memory agent's capabilities.
    """
    print("🤖 Creating Memory-Enabled Agent...")
    print("=" * 50)
    
    # Create agent with a specific session name
    session_name = "memory_demo_session"
    agent = create_memory_agent(session_name)
    
    print(f"✅ Agent '{agent.name}' created successfully!")
    print(f"📋 Role: {agent.role}")
    print(f"🛠️  Tools: {len(agent.tools)} tools available")
    print(f"📝 Instructions: {len(agent.instructions)} instructions set")
    print(f"🧠 Memory: Agentic memory enabled")
    print(f"💭 Reasoning: Advanced reasoning enabled")
    print(f"📚 Session: '{session_name}'")
    print()
    
    # First conversation - establish context
    print("🗣️  First Conversation - Establishing Context:")
    print("-" * 40)
    
    context_questions = [
        "My name is Alex and I'm a software developer. I work with Python and JavaScript.",
        "I'm planning to build a web application for task management.",
        "What should I consider when choosing between different frameworks?"
    ]
    
    for i, question in enumerate(context_questions, 1):
        print(f"\n👤 Alex: {question}")
        print("🤖 Thinking...")
        
        try:
            response = agent.run(question)
            print(f"🤖 Assistant: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    # Second conversation - testing memory
    print("🗣️  Second Conversation - Testing Memory:")
    print("-" * 40)
    
    memory_questions = [
        "What's my name and what do I do?",
        "What project am I working on?",
        "Based on our previous discussion, what framework would you recommend for my task management app?",
        "Can you summarize what we've discussed so far?"
    ]
    
    for i, question in enumerate(memory_questions, 1):
        print(f"\n👤 Alex: {question}")
        print("🤖 Thinking...")
        
        try:
            response = agent.run(question)
            print(f"🤖 Assistant: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    # Third conversation - complex reasoning
    print("🗣️  Third Conversation - Complex Reasoning:")
    print("-" * 40)
    
    reasoning_questions = [
        "I'm thinking about adding user authentication to my app. What are the security considerations I should think about?",
        "How should I structure my database for this task management system?",
        "What deployment strategy would you recommend for a beginner developer like me?"
    ]
    
    for i, question in enumerate(reasoning_questions, 1):
        print(f"\n👤 Alex: {question}")
        print("🤖 Thinking...")
        
        try:
            response = agent.run(question)
            print(f"🤖 Assistant: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("🎉 Memory agent demonstration completed!")
    print(f"\n💡 The agent has maintained context across {len(context_questions) + len(memory_questions) + len(reasoning_questions)} questions")
    print(f"💡 Session '{session_name}' has been cached for future use")
    print(f"💡 Try running 'memory_test.py' to see memory persistence across sessions!")

def main():
    """
    Main function to run the memory agent demonstration.
    """
    demonstrate_memory_capabilities()

if __name__ == "__main__":
    main()
