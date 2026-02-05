from tools.github_tool import search_repos
from tools.weather_tool import get_weather

def execute_plan(plan):
    """
    Executor Agent - Executes the plan by calling appropriate APIs
    
    Args:
        plan: JSON plan from Planner Agent
    
    Returns:
        Dictionary with execution results
    """
    results = {}
    
    for step in plan.get("steps", []):
        step_id = step.get("step_id")
        tool = step.get("tool")
        params = step.get("params", {})
        
        try:
            if tool == "github":
                query = params.get("query", "python")
                limit = params.get("limit", 3)
                results[f"step_{step_id}_github"] = search_repos(query=query, limit=limit)
                
            elif tool == "weather":
                city = params.get("city", "Bangalore")
                results[f"step_{step_id}_weather"] = get_weather(city)
                
            else:
                results[f"step_{step_id}_error"] = f"Unknown tool: {tool}"
                
        except Exception as e:
            results[f"step_{step_id}_error"] = str(e)
    
    return results
