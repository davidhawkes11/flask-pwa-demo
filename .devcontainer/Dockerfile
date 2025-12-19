FROM python:3.13-slim
WORKDIR /workspace

# Install Git and other essentials RUN apt-get update && apt-get install -y git nano && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
COPY app/ ./app
CMD ["python", "app/main.py"]
