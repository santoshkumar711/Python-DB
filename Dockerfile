FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies with minimum disk usage
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libssl-dev \
    && pip install --no-cache-dir flask mysql-connector-python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Run the application
CMD ["python", "app.py"]
