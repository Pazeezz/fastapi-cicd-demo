# Dockerfile
FROM python:3.11-slim

# Keep Python from buffering logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app ./app

# (Optional) pass the git SHA at build time for the UI "Version" chip
ARG GIT_SHA=dev
ENV GIT_SHA=$GIT_SHA

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
