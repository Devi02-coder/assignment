"""
Simple test script to verify the AI Operations Assistant
"""
import requests
import json

def test_api():
    base_url = "http://localhost:8006"
    
    print("=" * 60)
    print("Testing AI Operations Assistant")
    print("=" * 60)
    
    # Test 1: Health check
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"[OK] Health check: {response.json()}")
    except Exception as e:
        print(f"[ERROR] Health check failed: {e}")
        return
    
    # Test 2: Root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(base_url)
        print(f"[OK] Root endpoint: {response.json()['message']}")
    except Exception as e:
        print(f"[ERROR] Root endpoint failed: {e}")
    
    # Test 3: Run task
    print("\n3. Testing task execution...")
    test_task = "Find top 1 Python GitHub repos and tell me the weather in Bangalore"
    
    try:
        response = requests.post(
            f"{base_url}/run-task",
            json={"task": test_task}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Task executed successfully!")
            print(f"\nPlan created: {json.dumps(result['plan'], indent=2)}")
            print(f"\nExecution results: {json.dumps(result['execution_results'], indent=2)}")
            print(f"\nFinal output: {json.dumps(result['final_output'], indent=2)}")
        else:
            print(f"[FAIL] Task failed with status {response.status_code}")
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"[ERROR] Task execution failed: {e}")
    
    print("\n" + "=" * 60)
    print("Testing complete!")
    print("=" * 60)

if __name__ == "__main__":
    print("\nMake sure the server is running with: uvicorn main:app --reload")
    print("Then run this test script.")
    input("\nPress Enter to start tests...")
    test_api()
