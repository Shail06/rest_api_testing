# Use a Python 3 base image
FROM openjdk:11-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy your requirements.txt to the container
COPY requirements.txt .

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Install the dependencies from the requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Install Allure commandline tool (for generating reports)
RUN apt-get update && apt-get install -y wget \
    && wget -qO- https://github.com/allure-framework/allure2/releases/download/2.32.1/allure-2.32.1.tgz | tar xvz -C /opt \
    && ln -s /opt/allure-2.32.1/bin/allure /usr/local/bin/allure

# Expose a port for viewing reports (optional)
EXPOSE 9090

# Use shell form for CMD to chain commands with &&
CMD ["sh", "-c", "python3 runner.py && /usr/local/bin/allure serve test-report/allure-results -p 9090"]
