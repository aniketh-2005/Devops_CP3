FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app ./app

# Set the working directory to /app/app for the execution
WORKDIR /app/app

EXPOSE 5000

CMD ["python", "server.py"]