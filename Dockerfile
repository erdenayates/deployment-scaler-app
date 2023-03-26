# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py /app/
COPY templates/ /app/templates/

# Expose port for the application
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

