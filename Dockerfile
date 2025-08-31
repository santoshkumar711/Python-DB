FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y gcc libssl-dev \
    && pip install --no-cache-dir flask mysql-connector-python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
