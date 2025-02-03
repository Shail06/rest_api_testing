# Use a Python 3 base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy your requirements.txt to the container
COPY requirements.txt .

# Install the dependencies from the requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Install Allure commandline tool (for generating reports)
RUN apt-get update && apt-get install -y wget \
    && wget -qO- https://dl.bintray.com/qameta/maven/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.tgz | tar xvz -C /opt \
    && ln -s /opt/allure-2.13.9/bin/allure /usr/local/bin/allure

# Expose a port for viewing reports (optional)
EXPOSE 8080

# Command to run the tests (adjust according to your setup)
CMD ["python3", "runner.py"]
