# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE Vessel_Dashboard.settings

# requirements
COPY requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install -r /requirements.txt

# Make port 8000 available to the world outside this container
# EXPOSE 8000

# Run app.py when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app