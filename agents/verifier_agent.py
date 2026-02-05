from llm.llm_client import call_llm
import json
import re

def verify_results(results, original_task=""):
    """
    Verifier Agent - Validates execution results and formats final output
    
    Args:
        results: Execution results from Executor Agent
        original_task: Original user task for context
    
    Returns:
        Structured and verified final output
    """
    system_prompt = """
You are a Verifier Agent. Your job is to:
1. Check if all required data is present
2. Validate data completeness
3. Format into a clean, structured JSON output

Return a JSON object with:
{
  "status": "complete" or "incomplete",
  "summary": "Brief summary of findings",
  "github_results": [...],
  "weather_results": {...},
  "missing_data": []
}

Rules:
- Return ONLY valid JSON, no other text
- Check for errors in the results
- Summarize key findings
- Flag any missing or incomplete data
"""

    user_prompt = f"""
Original Task: {original_task}

Execution Results:
{json.dumps(results, indent=2)}

Verify and format these results.
"""
    
    response = call_llm(system_prompt, user_prompt)
    
    # Clean the response to extract JSON
    response = response.strip()
    
    # Remove markdown code blocks if present
    if response.startswith("```"):
        response = re.sub(r'^```(?:json)?\n', '', response)
        response = re.sub(r'\n```$', '', response)
    
    try:
        verified_output = json.loads(response)
        return verified_output
    except json.JSONDecodeError as e:
        # Return raw results if verification fails
        return {
            "status": "verification_failed",
            "raw_results": results,
            "error": str(e)
        }
