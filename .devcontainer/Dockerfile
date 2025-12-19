FROM python:3.13-slim

# Install Git and other essentials RUN apt-get update && apt-get install -y git nano && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
COPY app/ ./app
CMD ["python", "app/main.py"]

# Create non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser/app
COPY . /home/appuser/app
RUN chown -R appuser:appuser /home/appuser/app

USER appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN python -m pip install --upgrade pip
RUN pip install --user -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
