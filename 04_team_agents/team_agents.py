"""
Example 4: Team Agents (Level 4)
================================

This example demonstrates a Level 4 Agno system with multiple agents working together:
- A Project Manager agent that coordinates the team
- A Developer agent that handles technical implementation
- A Designer agent that focuses on user experience
- A QA Tester agent that ensures quality
- Team collaboration and communication protocols
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.calculator import CalculatorTools
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

# Load environment variables
load_dotenv()

def create_project_manager():
    """Create a Project Manager agent that coordinates the team."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="pm_memories", db_file="memory_pm.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Project Manager",
        role="A project manager who coordinates team efforts, manages timelines, and ensures project success",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a skilled project manager with expertise in agile methodologies",
            "Coordinate team efforts and manage project timelines",
            "Break down complex projects into manageable tasks",
            "Identify dependencies and critical path items",
            "Communicate clearly with stakeholders and team members",
            "Use markdown formatting for project plans and status updates",
            "Always consider resource constraints and deadlines"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="pm",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_developer():
    """Create a Developer agent that handles technical implementation."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="dev_memories", db_file="memory_dev.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Developer",
        role="A senior software developer with expertise in multiple programming languages and frameworks",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a senior software developer with 10+ years of experience",
            "Provide technical solutions and implementation guidance",
            "Consider code quality, performance, and maintainability",
            "Suggest appropriate technologies and frameworks",
            "Break down technical tasks into implementable steps",
            "Consider security, scalability, and best practices",
            "Use markdown formatting for technical documentation"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="dev",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_designer():
    """Create a Designer agent that focuses on user experience."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="design_memories", db_file="memory_design.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="Designer",
        role="A UX/UI designer who creates intuitive and beautiful user interfaces",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a UX/UI designer with expertise in user-centered design",
            "Focus on user experience, accessibility, and visual appeal",
            "Consider user workflows and interaction patterns",
            "Suggest design systems and component libraries",
            "Balance aesthetics with functionality and usability",
            "Consider responsive design and cross-platform compatibility",
            "Use markdown formatting for design specifications"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="design",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_qa_tester():
    """Create a QA Tester agent that ensures quality."""
    
    memory = Memory(
        model=OpenAIChat(id="gpt-4o"),
        db=SqliteMemoryDb(table_name="qa_memories", db_file="memory_qa.db"),
        delete_memories=True,
        clear_memories=True,
    )
    
    agent = Agent(
        name="QA Tester",
        role="A quality assurance specialist who ensures software meets high standards",
        model=OpenAIChat(id="gpt-4o"),
        tools=[
            ReasoningTools(add_instructions=True),
            CalculatorTools(),
        ],
        instructions=[
            "You are a QA specialist focused on quality and testing",
            "Identify potential issues and edge cases",
            "Suggest testing strategies and methodologies",
            "Consider user acceptance criteria and requirements",
            "Focus on reliability, performance, and security testing",
            "Suggest automated testing approaches where appropriate",
            "Use markdown formatting for test plans and bug reports"
        ],
        markdown=True,
        show_tool_calls=True,
        memory=memory,
        user_id="qa",
        enable_agentic_memory=True,
        enable_user_memories=True,
        enable_session_summaries=True,
    )
    
    return agent

def create_team():
    """Create a team of agents that can collaborate on projects."""
    
    # Create individual agents
    pm = create_project_manager()
    dev = create_developer()
    designer = create_designer()
    qa = create_qa_tester()
    
    # Create the team
    team = Team(
        name="Software Development Team",
        members=[pm, dev, designer, qa],
        mode="coordinate",
        instructions=[
            "Work together to solve complex software development problems",
            "Each agent should contribute their expertise to the solution",
            "Communicate clearly and coordinate efforts effectively",
            "Consider all aspects: project management, technical implementation, design, and quality",
            "Provide comprehensive solutions that address all stakeholder needs"
        ]
    )
    
    return team

def demonstrate_team_collaboration():
    """Demonstrate how the team of agents collaborates on a project."""
    
    print("🤝 Creating Software Development Team...")
    print("=" * 50)
    
    # Create the team
    team = create_team()
    
    print(f"✅ Team '{team.name}' created successfully!")
    print(f"👥 Team Members: {len(team.members)} agents")
    for agent in team.members:
        print(f"   - {agent.name}: {agent.role}")
    print()
    
    # Project scenario
    project_scenario = """
    We need to build a task management web application with the following requirements:
    
    1. **Project Scope**: A web app for teams to manage tasks, projects, and deadlines
    2. **Target Users**: Small to medium-sized teams (5-50 people)
    3. **Key Features**: Task creation, assignment, tracking, real-time updates, and reporting
    4. **Technical Requirements**: Modern web technologies, responsive design, secure authentication
    5. **Timeline**: 3 months development time
    6. **Team Size**: 4 developers, 2 designers, 1 QA specialist
    
    Please provide a comprehensive project plan that covers:
    - Project timeline and milestones
    - Technical architecture and technology stack
    - User experience design considerations
    - Quality assurance and testing strategy
    - Risk assessment and mitigation strategies
    """
    
    print("📋 Project Scenario:")
    print("-" * 30)
    print(project_scenario)
    print()
    
    print("🤝 Team Collaboration in Action:")
    print("=" * 40)
    
    # Let the team work on the project
    try:
        print("🤖 Team is analyzing the project requirements...")
        response = team.run(project_scenario)
        print(f"🤖 Team Response:\n{response.content}")
        
        # Check if there are any team-specific attributes
        if hasattr(response, 'team_work') and response.team_work:
            print(f"\n👥 Team Work Details: {response.team_work}")
        
    except Exception as e:
        print(f"❌ Error during team collaboration: {e}")
        print("Falling back to individual agent responses...")
        
        # Fallback: Get responses from individual agents
        print("\n🔄 Individual Agent Responses:")
        print("-" * 35)
        
        for agent in team.members:
            print(f"\n👤 {agent.name}:")
            print("-" * 20)
            try:
                response = agent.run(project_scenario)
                print(f"🤖 {response.content[:200]}...")
            except Exception as e:
                print(f"❌ Error: {e}")
    
    print("\n🎉 Team collaboration demonstration completed!")
    print(f"\n💡 The team has collaborated on a complex project scenario")
    print(f"💡 Each agent contributed their specialized expertise")
    print(f"💡 Try running 'team_test.py' to see more team interactions!")

def main():
    """Main function to run the team agents demonstration."""
    demonstrate_team_collaboration()

if __name__ == "__main__":
    main()
