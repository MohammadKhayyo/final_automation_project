# Use a specific version of the python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /usr/src/tests

# Copy the entire contents of the current directory into the working directory inside the container
# The .dockerignore file should be set to ignore non-essential files
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the test runner when the container starts
CMD ["python", "./test_api/test_runner.py"]
