#!/usr/bin/env python3
"""
Team Test Script
================

This script demonstrates various team collaboration scenarios and individual agent interactions.
Run this after running team_agents.py to see more team dynamics in action.
"""

import os
from dotenv import load_dotenv
from team_agents import create_team, create_project_manager, create_developer, create_designer, create_qa_tester

def test_individual_agent_capabilities():
    """Test individual agent capabilities and expertise."""
    
    print("🧪 Testing Individual Agent Capabilities")
    print("=" * 50)
    print("This test shows how each agent contributes their specialized expertise.\n")
    
    # Create individual agents
    pm = create_project_manager()
    dev = create_developer()
    designer = create_designer()
    qa = create_qa_tester()
    
    agents = [
        (pm, "Project Management"),
        (dev, "Technical Development"),
        (designer, "User Experience Design"),
        (qa, "Quality Assurance")
    ]
    
    # Test each agent with a relevant question
    test_questions = [
        "What are the key phases in a 3-month software development project?",
        "What technology stack would you recommend for a scalable web application?",
        "How would you design the user interface for a task management app?",
        "What testing strategy would you use for a web application with real-time features?"
    ]
    
    for i, ((agent, expertise), question) in enumerate(zip(agents, test_questions), 1):
        print(f"👤 {agent.name} - {expertise}")
        print("-" * 40)
        print(f"❓ Question: {question}")
        
        try:
            print("🤖 Thinking...")
            response = agent.run(question)
            print(f"🤖 Answer: {response.content[:300]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()

def test_team_problem_solving():
    """Test team problem-solving on a complex scenario."""
    
    print("🤝 Testing Team Problem-Solving")
    print("=" * 40)
    print("This test shows how the team works together on a complex problem.\n")
    
    # Create the team
    team = create_team()
    
    # Complex problem scenario
    problem_scenario = """
    We have a critical issue: Our e-commerce platform is experiencing:
    
    1. **Performance Issues**: Page load times increased from 2s to 8s
    2. **User Complaints**: 15% increase in support tickets
    3. **Business Impact**: 20% drop in conversion rate
    4. **Technical Debt**: Outdated dependencies and inefficient database queries
    5. **Timeline**: Must be resolved within 2 weeks
    
    The team needs to:
    - Analyze the root causes
    - Propose immediate fixes
    - Plan long-term improvements
    - Estimate resources and timeline
    - Consider business impact and user experience
    
    Please provide a coordinated response addressing all aspects.
    """
    
    print("🚨 Critical Problem Scenario:")
    print("-" * 35)
    print(problem_scenario)
    print()
    
    print("🤝 Team is collaborating on the solution...")
    print("=" * 50)
    
    try:
        response = team.run(problem_scenario)
        print(f"🤖 Team Response:\n{response.content}")
        
    except Exception as e:
        print(f"❌ Error during team collaboration: {e}")
        print("Falling back to individual responses...")
        
        # Get individual responses
        for agent in team.agents:
            print(f"\n👤 {agent.name} Analysis:")
            print("-" * 25)
            try:
                response = agent.run(problem_scenario)
                print(f"🤖 {response.content[:200]}...")
            except Exception as e:
                print(f"❌ Error: {e}")

def test_agent_memory_and_learning():
    """Test how agents remember and learn from previous interactions."""
    
    print("🧠 Testing Agent Memory and Learning")
    print("=" * 40)
    print("This test shows how agents remember previous discussions and build on them.\n")
    
    # Create a developer agent
    dev = create_developer()
    
    # First conversation
    print("👤 First Conversation - Establishing Context:")
    print("-" * 45)
    
    context_question = "I'm building a React application that needs to handle real-time data updates. What should I consider?"
    
    print(f"❓ Question: {context_question}")
    try:
        response = dev.run(context_question)
        print(f"🤖 Developer: {response.content[:250]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    
    # Second conversation - testing memory
    print("👤 Second Conversation - Testing Memory:")
    print("-" * 40)
    
    memory_question = "Based on our previous discussion about real-time React apps, what specific libraries would you recommend for my use case?"
    
    print(f"❓ Question: {memory_question}")
    try:
        response = dev.run(memory_question)
        print(f"🤖 Developer: {response.content[:250]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    
    # Third conversation - building on previous knowledge
    print("👤 Third Conversation - Building on Knowledge:")
    print("-" * 45)
    
    followup_question = "Given the real-time requirements we discussed, how should I structure my component architecture for optimal performance?"
    
    print(f"❓ Question: {followup_question}")
    try:
        response = dev.run(followup_question)
        print(f"🤖 Developer: {response.content[:250]}...")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_cross_agent_consultation():
    """Test how agents can consult with each other on complex topics."""
    
    print("🔄 Testing Cross-Agent Consultation")
    print("=" * 40)
    print("This test shows how agents can work together on interdisciplinary topics.\n")
    
    # Create agents
    pm = create_project_manager()
    dev = create_developer()
    designer = create_designer()
    
    # Complex interdisciplinary question
    consultation_question = """
    We need to decide on the architecture for a new mobile app that will:
    - Have both iOS and Android versions
    - Include real-time collaboration features
    - Support offline functionality
    - Handle sensitive user data
    
    This decision affects:
    - Development timeline and cost
    - User experience and performance
    - Maintenance and scalability
    - Security and compliance
    
    Please provide a coordinated recommendation considering all aspects.
    """
    
    print("🤝 Cross-Agent Consultation Question:")
    print("-" * 40)
    print(consultation_question)
    print()
    
    # Get perspectives from each agent
    agents = [
        (pm, "Project Management Perspective"),
        (dev, "Technical Implementation Perspective"),
        (designer, "User Experience Perspective")
    ]
    
    for agent, perspective in agents:
        print(f"👤 {agent.name} - {perspective}")
        print("-" * 45)
        
        try:
            response = agent.run(consultation_question)
            print(f"🤖 {response.content[:300]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()

def main():
    """Main function to run all team tests."""
    
    print("🚀 Team Agents Testing Suite")
    print("=" * 40)
    print("This suite demonstrates various aspects of team collaboration.\n")
    
    # Run all tests
    test_individual_agent_capabilities()
    print("\n" + "="*60 + "\n")
    
    test_team_problem_solving()
    print("\n" + "="*60 + "\n")
    
    test_agent_memory_and_learning()
    print("\n" + "="*60 + "\n")
    
    test_cross_agent_consultation()
    
    print("\n🎉 All team tests completed!")
    print("\n💡 Key Insights:")
    print("   - Each agent brings specialized expertise")
    print("   - Team collaboration provides comprehensive solutions")
    print("   - Agents remember and build on previous discussions")
    print("   - Cross-agent consultation enables interdisciplinary solutions")

if __name__ == "__main__":
    main()
