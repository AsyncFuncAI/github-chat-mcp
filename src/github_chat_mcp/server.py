import json
import os
import requests
from typing import List, Dict, Any, Optional

from mcp.server.fastmcp import FastMCP
from pydantic import Field


GITHUB_CHAT_API_BASE = "https://api.github-chat.com"
API_KEY = os.environ.get("GITHUB_API_KEY", "")

mcp = FastMCP("github-chat-mcp", dependencies=["requests", "mcp[cli]"])


@mcp.tool()
def index_repository(
    repo_url: str = Field(
        description="The GitHub repository URL to index (format: https://github.com/username/repo)."
    ),
) -> str:
    """Index a GitHub repository to analyze its codebase. This must be done before asking questions about the repository."""
    try:
        if not repo_url:
            raise ValueError("Repository URL cannot be empty.")
        
        if not repo_url.startswith("https://github.com/"):
            raise ValueError("Repository URL must be in the format: https://github.com/username/repo")
        
        # Call the verify API endpoint
        response = requests.post(
            f"{GITHUB_CHAT_API_BASE}/verify",
            headers={"Content-Type": "application/json"},
            json={"repo_url": repo_url}
        )
        
        if response.status_code != 200:
            return f"Error indexing repository: {response.text}"
        
        return f"Successfully indexed repository: {repo_url}. You can now ask questions about this repository."
    
    except Exception as e:
        return f"Error: {str(e) or repr(e)}"


@mcp.tool()
def query_repository(
    repo_url: str = Field(
        description="The GitHub repository URL to query (format: https://github.com/username/repo)."
    ),
    question: str = Field(
        description="The question to ask about the repository."
    ),
    conversation_history: Optional[List[Dict[str, str]]] = Field(
        description="Previous conversation history for multi-turn conversations.", default=None
    ),
) -> str:
    """Ask questions about a GitHub repository and receive detailed AI responses. The repository must be indexed first."""
    try:
        if not repo_url or not question:
            raise ValueError("Repository URL and question cannot be empty.")
        
        if not repo_url.startswith("https://github.com/"):
            raise ValueError("Repository URL must be in the format: https://github.com/username/repo")
        
        # Prepare messages array
        messages = conversation_history or []
        messages.append({"role": "user", "content": question})
        
        # Call the chat completions API endpoint
        response = requests.post(
            f"{GITHUB_CHAT_API_BASE}/chat/completions/sync",
            headers={"Content-Type": "application/json"},
            json={
                "repo_url": repo_url,
                "messages": messages
            }
        )
        
        if response.status_code != 200:
            return f"Error querying repository: {response.text}"
        
        # Format the response
        result = response.json()
        formatted_response = format_chat_response(result)
        
        return formatted_response
    
    except Exception as e:
        return f"Error: {str(e) or repr(e)}"


def format_chat_response(response: Dict[str, Any]) -> str:
    """Format the chat response in a readable way."""
    formatted = ""
    
    if "answer" in response:
        formatted += response["answer"] + "\n\n"
    
    if "contexts" in response and response["contexts"]:
        formatted += "Sources:\n"
        for i, context in enumerate(response["contexts"], 1):
            if "meta_data" in context and "file_path" in context["meta_data"]:
                formatted += f"{i}. {context['meta_data']['file_path']}\n"
    
    return formatted.strip()


def main():
    mcp.run()


if __name__ == "__main__":
    main() 