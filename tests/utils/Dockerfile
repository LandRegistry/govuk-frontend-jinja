# Use official Python 3.14 slim image for smaller base
FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.12.23 /uv /uvx /bin/

# Set working directory
WORKDIR /src

# Install system dependencies in a single layer and clean up cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl wait-for-it && \
    rm -rf /var/lib/apt/lists/*

# Download and install govuk-frontend-diff
RUN curl -L https://github.com/matthew-shaw/govuk-frontend-diff/releases/download/v2.0.0/govuk-frontend-diff-linux \
    --output /usr/local/bin/govuk-frontend-diff && \
    chmod +x /usr/local/bin/govuk-frontend-diff

# Install project dependencies first to leverage Docker cache
COPY pyproject.toml uv.lock .python-version README.md LICENSE ./
RUN uv sync --locked --all-groups --no-install-project

# Copy source code and tests, then install the project
COPY govuk_frontend_jinja govuk_frontend_jinja
COPY tests/utils tests/utils
RUN uv sync --locked --all-groups

# Set default command
CMD ["/src/tests/utils/test-entrypoint.sh"]
