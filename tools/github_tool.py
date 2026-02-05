import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_repos(query="python", sort="stars", limit=3):
    """
    Search GitHub repositories using GitHub API
    
    Args:
        query: Search query (default: "python")
        sort: Sort parameter (default: "stars")
        limit: Number of results to return (default: 3)
    
    Returns:
        List of repository details
    """
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    url = f"https://api.github.com/search/repositories?q={query}&sort={sort}&order=desc"
    
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()
        
        repos = []
        for item in data.get("items", [])[:limit]:
            repos.append({
                "name": item["name"],
                "stars": item["stargazers_count"],
                "url": item["html_url"],
                "description": item.get("description", "No description")
            })
        return repos
    except Exception as e:
        return {"error": f"GitHub API error: {str(e)}"}
