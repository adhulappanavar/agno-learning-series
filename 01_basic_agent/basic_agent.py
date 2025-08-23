"""
Example 1: Basic Agent with Tools
==================================

This example demonstrates a Level 1 Agno agent that has:
- Tools for reasoning and calculations
- Clear instructions
- Basic interaction capabilities
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.calculator import CalculatorTools

# Load environment variables
load_dotenv()

def create_basic_agent():
    """
    Create a basic Level 1 agent with reasoning and calculation tools.
    """
    
    # Create the agent
    agent = Agent(
        name="Basic Helper Agent",
        role="A helpful assistant that can reason and calculate",
        model=OpenAIChat(id="gpt-4o"),  # Using GPT-4o for best reasoning
        tools=[
            ReasoningTools(add_instructions=True),  # Enables step-by-step reasoning
            CalculatorTools(),  # Enables mathematical calculations
        ],
        instructions=[
            "Always think step by step",
            "Show your work when solving problems",
            "Be concise but thorough",
            "Use markdown formatting for better readability"
        ],
        markdown=True,  # Enable markdown output
        show_tool_calls=True,  # Show which tools are being used
    )
    
    return agent

def main():
    """
    Main function to demonstrate the basic agent.
    """
    print("🤖 Creating Basic Agno Agent...")
    print("=" * 50)
    
    # Create the agent
    agent = create_basic_agent()
    
    print(f"✅ Agent '{agent.name}' created successfully!")
    print(f"📋 Role: {agent.role}")
    print(f"🛠️  Tools: {len(agent.tools)} tools available")
    print(f"📝 Instructions: {len(agent.instructions)} instructions set")
    print()
    
    # Example interactions
    examples = [
        "What is 15% of 240? Show your calculation.",
        "If I have 3 apples and give away 1, then buy 5 more, how many do I have?",
        "Explain the concept of compound interest in simple terms."
    ]
    
    print("🧪 Testing the agent with example questions:")
    print("=" * 50)
    
    for i, question in enumerate(examples, 1):
        print(f"\n❓ Question {i}: {question}")
        print("-" * 40)
        
        try:
            # Get response from agent
            response = agent.run(question)
            print(f"🤖 Answer: {response.content}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("🎉 Basic agent example completed!")
    print("\n💡 Try asking your own questions by modifying the examples list!")

if __name__ == "__main__":
    main()
