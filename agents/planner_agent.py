from llm.llm_client import call_llm
import json
import re

def create_plan(user_task: str):
    """
    Planner Agent - Breaks down user task into structured execution steps
    
    Args:
        user_task: Natural language task from user
    
    Returns:
        JSON plan with steps for execution
    """
    system_prompt = """
You are a Planner Agent. Your job is to break down user tasks into structured execution steps.

Available tools:
- github: Search GitHub repositories (queries like: "python repos", "AI repositories", "machine learning projects")
- weather: Get weather information for cities (queries like: "Bangalore", "Delhi", "Mumbai")

Analyze the user's task and create a JSON plan with the following structure:
{
  "steps": [
    {"step_id": 1, "tool": "github", "action": "search for python repositories", "params": {"query": "python", "limit": 3}},
    {"step_id": 2, "tool": "weather", "action": "get weather for Bangalore", "params": {"city": "Bangalore"}}
  ]
}

Rules:
1. Extract city names for weather queries
2. Extract search topics for GitHub queries
3. Return ONLY valid JSON, no other text
4. Each step must have: step_id, tool, action, params
"""

    user_prompt = f"Task: {user_task}\n\nCreate an execution plan."
    
    response = call_llm(system_prompt, user_prompt)
    
    # Clean the response to extract JSON
    response = response.strip()
    
    # Remove markdown code blocks if present
    if response.startswith("```"):
        response = re.sub(r'^```(?:json)?\n', '', response)
        response = re.sub(r'\n```$', '', response)
    
    try:
        plan = json.loads(response)
        return plan
    except json.JSONDecodeError as e:
        # Fallback plan if JSON parsing fails
        return {
            "steps": [
                {"step_id": 1, "tool": "github", "action": "search repositories", "params": {"query": "python", "limit": 3}},
                {"step_id": 2, "tool": "weather", "action": "get weather", "params": {"city": "Bangalore"}}
            ],
            "parse_error": str(e)
        }
