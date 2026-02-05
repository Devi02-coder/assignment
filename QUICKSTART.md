# Quick Start Guide - AI Operations Assistant

## ⚡ Get Started in 5 Minutes

### Step 1: Get Your API Keys

You need THREE API keys (note: I see you provided OpenAI and GitHub keys, but you still need an OpenWeatherMap key):

1. **OpenAI API Key** ✅ (You have this)
   - Already provided: `sk-proj-NbgQKT6zEyJ...`

2. **GitHub Token** ✅ (You have this)
   - Already provided: `github_pat_11BT66X7Y...`

3. **OpenWeatherMap API Key** ⚠️ (You need to get this)
   - Go to: https://openweathermap.org/api
   - Sign up for free account
   - Get your API key from the dashboard
   - It looks like: `abc123def456...` (32 characters)

### Step 2: Setup Environment

```bash
# Navigate to project
cd ai_ops_assistant

# Install dependencies
pip install -r requirements.txt

# Edit .env file and add your OpenWeatherMap API key
# The file already has OpenAI and GitHub keys
nano .env  # or use any text editor
```

Your `.env` should look like:
```
OPENAI_API_KEY=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
GITHUB_TOKEN=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
WEATHER_API_KEY=YOUR_OPENWEATHER_KEY_HERE
```

### Step 3: Run the Application

```bash
uvicorn main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### Step 4: Test It

Open your browser and go to:
- **Interactive API docs**: http://localhost:8000/docs
- **Simple test**: http://localhost:8000/

Or use curl:
```bash
curl -X POST "http://localhost:8000/run-task" \
  -H "Content-Type: application/json" \
  -d '{"task": "Find top 3 Python GitHub repos and tell me the weather in Bangalore"}'
```

### Step 5: Create GitHub Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Operations Assistant"

# Create repository on GitHub
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/ai-ops-assistant.git
git branch -M main
git push -u origin main
```

## 🎯 What to Submit

1. **GitHub Repository URL** - Make it public or give access
2. **README.md** - Already included ✅
3. **Working Code** - All files are ready ✅

## ⚠️ Important Notes

- **NEVER commit your `.env` file** - It contains secret keys
- The `.gitignore` file already excludes `.env`
- Use `.env.example` as a template for others

## 🐛 Troubleshooting

**Problem**: `ModuleNotFoundError`
**Solution**: Run `pip install -r requirements.txt`

**Problem**: API authentication error
**Solution**: Check your `.env` file has correct keys

**Problem**: Weather API not working
**Solution**: Get a free API key from OpenWeatherMap

## ✅ Checklist Before Submission

- [ ] All API keys added to `.env`
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Application runs (`uvicorn main:app --reload`)
- [ ] Tested with at least one example query
- [ ] Code pushed to GitHub
- [ ] Repository is public or access granted
- [ ] `.env` file NOT committed

## 📧 Submit

Send to TrulyMadly:
- Your GitHub repository link
- Mention you followed the README for setup

Good luck! 🚀
