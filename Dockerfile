FROM python:3.11-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app1.py .

# Run the app
CMD ["python", "app.py"]