# Use official Python 3.14 slim image for smaller base
FROM python:3.14-slim

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

# Copy Pipfile & Pipfile.lock first to leverage Docker cache
COPY Pipfile Pipfile.lock ./

# Install pipenv and project dependencies directly into system Python
RUN python -m pip install --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile --dev

# Copy source code and tests
COPY govuk_frontend_jinja govuk_frontend_jinja
COPY tests/utils tests/utils

# Set default command
CMD ["/src/tests/utils/test-entrypoint.sh"]
