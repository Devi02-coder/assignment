
import requests
import json
import sys

try:
    url = "http://localhost:8006/run-task"
    payload = {
        "task": "Find top 1 Python GitHub repos and tell me the weather in Bangalore"
    }
    headers = {
        "Content-Type": "application/json"
    }
    print(f"Sending request to {url}...")
    response = requests.post(url, json=payload, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Response:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Exception: {e}")
