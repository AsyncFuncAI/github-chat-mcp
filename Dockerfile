# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

# Install the project into /app
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy the lock file and pyproject.toml for dependency management
COPY uv.lock pyproject.toml /app/

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev --no-editable

# Then, add the rest of the project source code and install it
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable

# Create the final image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy the virtual environment directly
COPY --from=uv --chown=app:app /app/.venv /app/.venv

# Create app user
RUN useradd -m app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Environment variable for the GitHub API key
ENV GITHUB_API_KEY=YOUR_API_KEY_HERE

# Switch to non-root user
USER app

# Run the MCP server
ENTRYPOINT ["github-chat-mcp"]
