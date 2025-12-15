FROM python:3.11-slim

WORKDIR /app

# Install system deps (git needed later)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install python deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend
COPY backend/app ./app

# Copy frontend (served later)
COPY frontend ./frontend

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

