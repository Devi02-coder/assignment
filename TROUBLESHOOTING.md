# Troubleshooting Guide

## Common Issues and Solutions

### 1. Installation Issues

#### Problem: `pip install` fails
```bash
ERROR: Could not find a version that satisfies the requirement...
```

**Solution**:
```bash
# Upgrade pip first
pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

#### Problem: Permission denied
```bash
ERROR: Could not install packages due to an EnvironmentError
```

**Solution**:
```bash
# Use --user flag
pip install --user -r requirements.txt

# OR use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. Environment Variable Issues

#### Problem: API keys not working
```
openai.AuthenticationError: Invalid API key
```

**Solution**:
1. Check `.env` file exists in project root
2. Verify no extra spaces around `=` sign
3. Ensure keys are on single lines
4. Restart the application after changing `.env`

**Correct format**:
```env
OPENAI_API_KEY=sk-proj-abc123...
GITHUB_TOKEN=github_pat_abc123...
WEATHER_API_KEY=abc123...
```

**Incorrect format**:
```env
OPENAI_API_KEY = sk-proj-abc123...  # Extra spaces ✗
OPENAI_API_KEY=sk-proj-abc123
...continuing on next line...  # Multi-line ✗
```

#### Problem: `.env` file not loaded
```
KeyError: 'OPENAI_API_KEY'
```

**Solution**:
```bash
# Verify .env exists
ls -la .env

# Check it's in the same directory as main.py
pwd
ls main.py .env

# Install python-dotenv
pip install python-dotenv
```

---

### 3. API-Specific Issues

#### Problem: OpenAI API errors
```
openai.RateLimitError: You exceeded your current quota
```

**Solutions**:
1. Check your OpenAI account has credits
2. Visit: https://platform.openai.com/account/billing
3. Add payment method if needed
4. Wait a few minutes if hitting rate limits

#### Problem: GitHub API rate limiting
```
GitHub API error: 403 Forbidden
```

**Solutions**:
1. Ensure `GITHUB_TOKEN` is set in `.env`
2. Check token has correct permissions
3. Generate new token: GitHub Settings → Developer settings → Personal access tokens
4. Required scopes: `public_repo` or `repo`

#### Problem: Weather API errors
```
Weather API error: 401 Unauthorized
```

**Solutions**:
1. Get API key from: https://openweathermap.org/api
2. Sign up for free account (supports 1000 calls/day)
3. Copy API key from dashboard
4. Add to `.env` file as `WEATHER_API_KEY`
5. Wait 10-15 minutes for key activation

---

### 4. Runtime Errors

#### Problem: Module not found
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution**:
```bash
# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list | grep fastapi
```

#### Problem: Port already in use
```
ERROR: [Errno 48] Address already in use
```

**Solution**:
```bash
# Find process using port 8000
lsof -i :8000  # On Mac/Linux
netstat -ano | findstr :8000  # On Windows

# Kill the process
kill -9 <PID>  # Use PID from above command

# OR use different port
uvicorn main:app --reload --port 8001
```

#### Problem: Import errors within project
```
ImportError: cannot import name 'create_plan' from 'agents.planner_agent'
```

**Solution**:
```bash
# Ensure you're in project root
cd ai_ops_assistant

# Check __init__.py files exist
ls agents/__init__.py tools/__init__.py llm/__init__.py

# If missing, create them
touch agents/__init__.py tools/__init__.py llm/__init__.py

# Restart server
uvicorn main:app --reload
```

---

### 5. Response/Output Issues

#### Problem: Empty or error responses
```json
{
  "detail": "Task execution failed: ..."
}
```

**Solution**:
1. Check all three API keys are valid
2. Test APIs individually:
```python
# Test OpenAI
from llm.llm_client import call_llm
result = call_llm("You are helpful", "Say hello")
print(result)

# Test GitHub
from tools.github_tool import search_repos
repos = search_repos()
print(repos)

# Test Weather
from tools.weather_tool import get_weather
weather = get_weather("Bangalore")
print(weather)
```

#### Problem: JSON parsing errors
```
JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Solution**:
- This is handled in the code with fallback plans
- Check OpenAI API is responding correctly
- Verify internet connection
- Check OpenAI service status: https://status.openai.com/

---

### 6. GitHub/Git Issues

#### Problem: Can't push to GitHub
```
remote: Repository not found
```

**Solution**:
```bash
# Create repository on GitHub first
# Then:
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

#### Problem: `.env` file pushed to GitHub
```
Your API keys are now public!
```

**URGENT Solution**:
1. **IMMEDIATELY** regenerate all API keys:
   - OpenAI: https://platform.openai.com/api-keys
   - GitHub: Settings → Developer settings → Tokens
   - Weather: https://openweathermap.org/api

2. Remove from Git history:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

git push origin --force --all
```

3. Verify `.gitignore` includes `.env`

---

### 7. Testing Issues

#### Problem: API requests timeout
```
requests.exceptions.Timeout: ...
```

**Solution**:
- Check internet connection
- Increase timeout in tool files:
```python
# In github_tool.py and weather_tool.py
response = requests.get(url, timeout=30)  # Increase from 10 to 30
```

#### Problem: Test script fails
```
Connection refused
```

**Solution**:
```bash
# Make sure server is running first
uvicorn main:app --reload

# In another terminal, run tests
python test_api.py
```

---

### 8. Verification Checklist

If something isn't working, go through this checklist:

```bash
# 1. Check Python version (3.8+)
python --version

# 2. Check you're in the right directory
pwd
ls main.py  # Should exist

# 3. Check .env file
cat .env  # Should show your keys (don't share output!)

# 4. Check dependencies
pip list | grep -E "fastapi|uvicorn|openai|requests"

# 5. Run setup checker
python check_setup.py

# 6. Check server starts
uvicorn main:app --reload
# Should show: "Application startup complete"
```

---

### 9. Getting Help

If none of the above solutions work:

1. **Check logs**: Look at the terminal output for specific error messages

2. **Verify each component**:
   - LLM client: `python -c "from llm.llm_client import call_llm; print('OK')"`
   - Tools: `python -c "from tools.github_tool import search_repos; print('OK')"`
   - Agents: `python -c "from agents.planner_agent import create_plan; print('OK')"`

3. **Test in isolation**:
   ```python
   # Test just one component at a time
   from tools.weather_tool import get_weather
   result = get_weather("London")
   print(result)
   ```

4. **Common quick fixes**:
   - Restart the server
   - Delete `__pycache__` folders: `find . -type d -name __pycache__ -exec rm -r {} +`
   - Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
   - Use a fresh virtual environment

---

### 10. Performance Issues

#### Problem: Responses are very slow (> 60 seconds)

**Causes**:
- OpenAI API latency (unavoidable)
- Multiple API calls in sequence
- Network issues

**Optimization tips**:
- Use faster OpenAI model (already using `gpt-4o-mini`)
- Implement caching for repeated queries
- Add parallel execution for independent API calls

**Note**: Some latency is expected due to:
1. LLM planning call (~2-3 seconds)
2. API executions (~2-5 seconds each)
3. LLM verification call (~2-3 seconds)
Total: ~10-15 seconds is normal

---

## Still Having Issues?

Document the following and share with reviewers:

1. **Error message** (full stack trace)
2. **Steps to reproduce**
3. **Your environment**:
   ```bash
   python --version
   pip list
   cat requirements.txt
   ```
4. **What you've tried** from this guide

Good luck! 🚀
