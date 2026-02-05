"""
Environment Setup Verification Script
Run this to check if your environment is correctly configured
"""

import os
import sys

def check_environment():
    print("=" * 60)
    print("AI Operations Assistant - Environment Check")
    print("=" * 60)
    
    issues = []
    warnings = []
    
    # Check Python version
    print("\n✓ Checking Python version...")
    if sys.version_info < (3, 8):
        issues.append("Python 3.8+ required")
    else:
        print(f"  Python {sys.version_info.major}.{sys.version_info.minor} detected ✓")
    
    # Check for .env file
    print("\n✓ Checking .env file...")
    if not os.path.exists('.env'):
        issues.append(".env file not found - copy .env.example to .env")
    else:
        print("  .env file exists ✓")
    
    # Check dependencies
    print("\n✓ Checking installed packages...")
    required_packages = ['fastapi', 'uvicorn', 'requests', 'openai', 'dotenv', 'pydantic']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  {package} ✓")
        except ImportError:
            missing_packages.append(package)
            print(f"  {package} ✗")
    
    if missing_packages:
        issues.append(f"Missing packages: {', '.join(missing_packages)}")
        print(f"\n  Run: pip install -r requirements.txt")
    
    # Check environment variables
    print("\n✓ Checking environment variables...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        openai_key = os.getenv('OPENAI_API_KEY')
        github_token = os.getenv('GITHUB_TOKEN')
        weather_key = os.getenv('WEATHER_API_KEY')
        
        if not openai_key or openai_key == 'your_openai_key_here':
            issues.append("OPENAI_API_KEY not set in .env")
        else:
            print(f"  OPENAI_API_KEY: {openai_key[:20]}... ✓")
        
        if not github_token or github_token == 'your_github_token_here':
            issues.append("GITHUB_TOKEN not set in .env")
        else:
            print(f"  GITHUB_TOKEN: {github_token[:20]}... ✓")
        
        if not weather_key or weather_key == 'your_openweather_api_key_here':
            warnings.append("WEATHER_API_KEY not set - get one from https://openweathermap.org/api")
        else:
            print(f"  WEATHER_API_KEY: {weather_key[:20]}... ✓")
    
    except Exception as e:
        issues.append(f"Error loading environment: {e}")
    
    # Check file structure
    print("\n✓ Checking project structure...")
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'agents/planner_agent.py',
        'agents/executor_agent.py',
        'agents/verifier_agent.py',
        'tools/github_tool.py',
        'tools/weather_tool.py',
        'llm/llm_client.py'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  {file_path} ✓")
        else:
            issues.append(f"Missing file: {file_path}")
            print(f"  {file_path} ✗")
    
    # Summary
    print("\n" + "=" * 60)
    if not issues and not warnings:
        print("✅ ALL CHECKS PASSED! You're ready to run the application.")
        print("\nStart the server with:")
        print("  uvicorn main:app --reload")
    else:
        if issues:
            print("❌ ISSUES FOUND:")
            for issue in issues:
                print(f"  • {issue}")
        
        if warnings:
            print("\n⚠️  WARNINGS:")
            for warning in warnings:
                print(f"  • {warning}")
        
        print("\nFix these issues before running the application.")
    
    print("=" * 60)

if __name__ == "__main__":
    check_environment()
