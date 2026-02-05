from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.planner_agent import create_plan
from agents.executor_agent import execute_plan
from agents.verifier_agent import verify_results

app = FastAPI(
    title="AI Operations Assistant",
    description="Multi-Agent GenAI System with Planner, Executor, and Verifier",
    version="1.0.0"
)

class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    plan: dict
    execution_results: dict
    final_output: dict

@app.get("/")
def read_root():
    return {
        "message": "AI Operations Assistant API",
        "endpoints": {
            "POST /run-task": "Execute a task using multi-agent system",
            "GET /health": "Health check endpoint"
        },
        "example_tasks": [
            "Find top 3 Python GitHub repos and tell me the weather in Bangalore",
            "Show trending AI repositories and weather in Delhi",
            "Get best machine learning repositories and weather in Mumbai"
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/run-task", response_model=TaskResponse)
def run_task(request: TaskRequest):
    """
    Main endpoint that orchestrates the multi-agent system
    
    Flow:
    1. Planner Agent creates execution plan
    2. Executor Agent calls APIs based on plan
    3. Verifier Agent validates and formats results
    """
    try:
        task = request.task
        
        # Step 1: Planning
        plan = create_plan(task)
        
        # Step 2: Execution
        execution_results = execute_plan(plan)
        
        # Step 3: Verification
        final_output = verify_results(execution_results, original_task=task)
        
        return {
            "plan": plan,
            "execution_results": execution_results,
            "final_output": final_output
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Task execution failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
