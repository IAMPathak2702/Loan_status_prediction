# Use the official Python 3.11 slim-buster image as the base image
FROM python:3.11.8-slim-bullseye

# Update package index and install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Set the working directory in the container
WORKDIR /code

# Copy the local directory's contents into the container at /code
COPY . /code

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /code/src/requirements.txt

# Expose port 9654 to the outside world
EXPOSE 8005

WORKDIR /code/src
# Set PYTHONPATH environment variable
ENV PYTHONPATH "${PYTHONPATH}:/code/src"

RUN pip install -e .

# Define the default command to run when the container starts
CMD ["python", "/code/src/prediction_model/training_pipeline.py"]
