<<<<<<< HEAD
# AI Operations Assistant – Multi-Agent GenAI System

A production-ready multi-agent system that uses LLM-powered planning, API execution, and result verification to handle complex user queries.

## 🏗️ Architecture

This system implements a **three-agent architecture**:

### Agent Roles

| Agent | Responsibility | Implementation |
|-------|----------------|----------------|
| **Planner Agent** | Analyzes user tasks and creates structured execution plans | Uses GPT-4o-mini to break down natural language into JSON steps |
| **Executor Agent** | Executes the plan by calling appropriate APIs | Interfaces with GitHub and Weather APIs based on plan |
| **Verifier Agent** | Validates results and formats final output | Uses LLM to check completeness and structure response |

### Data Flow

```
User Query
    ↓
Planner Agent (LLM) → JSON Plan
    ↓
Executor Agent → API Calls (GitHub + Weather)
    ↓
Verifier Agent (LLM) → Validated JSON Response
    ↓
User
```

## 🔌 Integrated APIs

1. **GitHub API** - Search and retrieve repository information
   - Endpoint: `https://api.github.com/search/repositories`
   - Returns: Repository name, stars, URL, description
   
2. **OpenWeatherMap API** - Fetch current weather data
   - Endpoint: `http://api.openweathermap.org/data/2.5/weather`
   - Returns: Temperature, conditions, humidity, wind speed

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- GitHub Personal Access Token
- OpenWeatherMap API key

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai_ops_assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
GITHUB_TOKEN=your_github_token_here
WEATHER_API_KEY=your_openweather_api_key_here
```

#### How to Get API Keys:

- **OpenAI**: https://platform.openai.com/api-keys
- **GitHub**: Settings → Developer settings → Personal access tokens → Generate new token
- **OpenWeatherMap**: https://openweathermap.org/api (Free tier available)

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 🧪 Testing the System

### Using cURL

```bash
curl -X POST "http://localhost:8000/run-task" \
  -H "Content-Type: application/json" \
  -d '{"task": "Find top 3 Python GitHub repos and tell me the weather in Bangalore"}'
```

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/run-task",
    json={"task": "Show trending AI repositories and weather in Delhi"}
)
print(response.json())
```

### Using Browser

Visit `http://localhost:8000/docs` for interactive Swagger UI

## 📝 Example Prompts

1. **Basic Query**
   ```
   Find top 3 Python GitHub repos and tell me the weather in Bangalore
   ```

2. **AI Focused**
   ```
   Show trending AI repositories and weather in Delhi
   ```

3. **Machine Learning**
   ```
   Get best machine learning repositories and weather in Mumbai
   ```

4. **Custom Search**
   ```
   Search for React repositories and show weather in Chennai
   ```

5. **Multi-City**
   ```
   Find top JavaScript repos and weather in Pune
   ```

## 📂 Project Structure

```
ai_ops_assistant/
│
├── agents/
│   ├── planner_agent.py      # Task planning with LLM
│   ├── executor_agent.py     # API execution logic
│   └── verifier_agent.py     # Result validation
│
├── tools/
│   ├── github_tool.py        # GitHub API integration
│   └── weather_tool.py       # Weather API integration
│
├── llm/
│   └── llm_client.py         # OpenAI client wrapper
│
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

## ⚙️ How It Works

### 1. User submits a task
```json
{
  "task": "Find Python repos and Bangalore weather"
}
```

### 2. Planner Agent creates a plan
```json
{
  "steps": [
    {
      "step_id": 1,
      "tool": "github",
      "action": "search for python repositories",
      "params": {"query": "python", "limit": 3}
    },
    {
      "step_id": 2,
      "tool": "weather",
      "action": "get weather for Bangalore",
      "params": {"city": "Bangalore"}
    }
  ]
}
```

### 3. Executor Agent calls APIs
- Fetches GitHub repositories
- Retrieves weather data

### 4. Verifier Agent validates and formats
```json
{
  "status": "complete",
  "summary": "Found 3 Python repositories and weather for Bangalore",
  "github_results": [...],
  "weather_results": {...}
}
```

## ⚠️ Known Limitations

1. **No Caching** - Each request makes fresh API calls
2. **Sequential Execution** - Steps are executed one after another (not parallel)
3. **Fixed City Extraction** - Weather queries rely on LLM to extract city names
4. **Limited Error Retries** - Failed API calls are not automatically retried
5. **Rate Limiting** - Subject to GitHub and OpenWeatherMap API rate limits
6. **LLM Dependency** - Requires OpenAI API for planning and verification

## 🎯 Design Tradeoffs

| Choice | Benefit | Tradeoff |
|--------|---------|----------|
| Sequential execution | Simple, predictable | Slower than parallel |
| LLM-based planning | Flexible, handles varied inputs | Adds latency and cost |
| No caching | Always fresh data | Redundant API calls |
| Structured outputs | Easy to parse | Requires careful prompt engineering |

## 🔧 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **API authentication failures**
   - Check your `.env` file has correct keys
   - Ensure no extra spaces in API keys

3. **OpenAI errors**
   - Verify API key is valid and has credits
   - Check model name is correct (`gpt-4o-mini`)

4. **GitHub rate limiting**
   - Use authenticated requests (add GitHub token)
   - Wait for rate limit reset

## 📊 Success Criteria

✅ Multi-agent architecture (Planner, Executor, Verifier)  
✅ LLM with structured outputs (GPT-4o-mini)  
✅ 2+ real APIs integrated (GitHub + Weather)  
✅ End-to-end functionality  
✅ No hardcoded responses  
✅ Runs with single command  

## 🤝 Contributing

This project was built as a technical assignment for the GenAI Intern position at TrulyMadly.

## 📄 License

MIT License - feel free to use for learning purposes.

## 👤 Author

Created as part of TrulyMadly GenAI Intern hiring process.

---

**Note**: Remember to never commit your `.env` file to version control. The `.env.example` file is provided as a template.
=======
OPENAI_API_KEY=AIzaSyCCmxUUzGZ7RJPdAjTqakQ20Fk7HgNApHg
GITHUB_TOKEN=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
WEATHER_API_KEY=a0e5f8bc17daa14ae5e7bc59c49c8528
>>>>>>> e2794eeab62ee33f167964a64496d569ab83a8a6
