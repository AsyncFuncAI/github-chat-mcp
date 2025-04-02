# GitHub Chat MCP

A Machine Computer Program (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

## Installation

```bash
# Install with pip
pip install github-chat-mcp

# Or install with the newer uv package manager
uv install github-chat-mcp
```

## Usage

1. Get a GitHub Chat API key from https://github-chat.com

2. Add the MCP to your Claude config file:

```json
{
  "mcpServers": {
    "github-chat": {
      "command": "github-chat-mcp",
      "env": {
        "GITHUB_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

3. Start using it with Claude!

Example prompts:
- "Use github-chat-mcp to analyze the React repository"
- "Index the TypeScript repository with github-chat-mcp and ask about its architecture"

# GitHub Chat MCP server

[![smithery badge](https://smithery.ai/badge/github-chat-mcp)](https://smithery.ai/server/github-chat-mcp)

## Setup Instructions
> Before anything, ensure you have a GitHub Chat API key. This is required to use the service.

Install uv first.

MacOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Setup with Claude Desktop
```json
# claude_desktop_config.json
# Can find location through:
# Hamburger Menu -> File -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
    "github-chat": {
      "command": "uvx",
      "args": ["github-chat-mcp"],
      "env": {
        "GITHUB_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Installing via Smithery

You can install GitHub Chat for Claude Desktop automatically via Smithery:

```bash
npx -y @smithery/cli install github-chat-mcp --client claude
```

### Using GitHub Chat with Claude
1. Index a GitHub repository first:
   "Index the GitHub repository at https://github.com/username/repo"

2. Then ask questions about the repository:
   "What is the core tech stack used in this repository?"

### Debugging
Run:
```bash
npx @modelcontextprotocol/inspector uvx github-chat-mcp
```

## Local/Dev Setup Instructions

### Clone repo
`git clone https://github.com/yourusername/github-chat-mcp.git`

### Install dependencies
Install uv first.

MacOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install MCP server dependencies:
```bash
cd github-chat-mcp

# Create virtual environment and activate it
uv venv

source .venv/bin/activate # MacOS/Linux
# OR
.venv/Scripts/activate # Windows

# Install dependencies
uv sync
```
### Setup with Claude Desktop

#### Using MCP CLI SDK
```bash
# `pip install mcp[cli]` if you haven't
mcp install /ABSOLUTE/PATH/TO/PARENT/FOLDER/github-chat-mcp/src/github_chat_mcp/server.py -v "GITHUB_API_KEY=API_KEY_HERE"
```

#### Manually
```json
# claude_desktop_config.json
# Can find location through:
# Hamburger Menu -> File -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
    "github-chat": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/github-chat-mcp",
        "run",
        "github-chat-mcp"
      ],
      "env": {
        "GITHUB_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Using GitHub Chat with Claude
1. Index a GitHub repository first:
   "Index the GitHub repository at https://github.com/username/repo"

2. Then ask questions about the repository:
   "What is the core tech stack used in this repository?"

### Debugging
Run:
```bash
# If mcp cli installed (`pip install mcp[cli]`)
mcp dev /ABSOLUTE/PATH/TO/PARENT/FOLDER/github-chat-mcp/src/github_chat_mcp/server.py

# If not
npx @modelcontextprotocol/inspector \
      uv \
      --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/github-chat-mcp \
      run \
      github-chat-mcp
```
Then access MCP Inspector at `http://localhost:5173`. You may need to add your GitHub API key in the environment variables in the inspector under `GITHUB_API_KEY`.

# Notes
- Level of logging is adjustable through the `FASTMCP_LOG_LEVEL` environment variable (e.g. `FASTMCP_LOG_LEVEL="ERROR"`)
- This MCP server provides two main tools:
  1. Repository Indexing - Index and analyze a GitHub repository
  2. Repository Querying - Ask questions about the indexed repository