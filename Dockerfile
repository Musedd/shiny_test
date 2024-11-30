FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code into the container
COPY app.py /app

# Expose port 8080 for the Flask app
EXPOSE 8080

# Define the command to run the app
CMD ["python", "app.py"]