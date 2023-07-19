# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory in the container to /app
# WORKDIR /app 

# Copy the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt

RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc
RUN apt-get install -y pkg-config 
RUN apt-get install -y python3-mysqldb
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
