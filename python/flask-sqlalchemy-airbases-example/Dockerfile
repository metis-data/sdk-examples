# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the working directory
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV DB_CONNECTION_STRING=postgresql://demo_user:demo_user@containers-us-west-97.railway.app:6613/demo
ENV METIS_API_KEY=<YOUR_API_KEY_HERE>
ENV TAKE_ENV_FROM_DOCKER_FILE=true
# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
