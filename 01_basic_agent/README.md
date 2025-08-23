# Example 1: Basic Agent with Tools

This is the first example in the Agno learning series. We'll build a **Level 1** agent that has tools and instructions.

## What You'll Learn
- How to create a basic Agno agent
- How to use built-in tools
- How to give instructions to your agent
- Basic agent interaction

## What We're Building
A simple agent that can:
- Answer questions using reasoning tools
- Get current time and date
- Perform basic calculations
- Follow specific instructions

## Files
- `basic_agent.py` - The main agent code
- `requirements.txt` - Dependencies
- `run_example.py` - Script to test the agent

## Example Output

When you run `python basic_agent.py`, you'll see:

```
🤖 Creating Basic Agno Agent...
==================================================
✅ Agent 'Basic Helper Agent' created successfully!
📋 Role: A helpful assistant that can reason and calculate
🛠️  Tools: 2 tools available
📝 Instructions: 4 instructions set

🧪 Testing the agent with example questions:
==================================================

❓ Question 1: What is 15% of 240? Show your calculation.
----------------------------------------
🤖 Answer: 15% of 240 is calculated as follows:

- Convert 15% to a decimal by dividing by 100:  
  \( 15\% = 0.15 \)

- Multiply 240 by 0.15:  
  \( 240 \times 0.15 = 36.0 \)

Therefore, 15% of 240 is **36.0**.

❓ Question 2: If I have 3 apples and give away 1, then buy 5 more, how many do I have?
----------------------------------------
🤖 Answer: You have 7 apples in total.

❓ Question 3: Explain the concept of compound interest in simple terms.
----------------------------------------
🤖 Answer: Compound interest is the interest on a loan or deposit that is calculated based on both the initial principal and the accumulated interest from previous periods...

🎉 Basic agent example completed!
```

## Next Steps
After this example, you'll learn about:
- Agents with knowledge and storage (Level 2)
- Agents with memory and reasoning (Level 3)
- Multi-agent teams (Level 4)
- Complex workflows (Level 5)
