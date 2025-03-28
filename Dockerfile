# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI application code
COPY app /var/task/app

# Install AWS Lambda adapter to make FastAPI compatible with Lambda
RUN pip install awslambdaric

# Expose the handler
CMD ["app.main.handler"]
