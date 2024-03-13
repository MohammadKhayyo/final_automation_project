# Use a specific version of the python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /usr/src/tests

# Install Chrome browser
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire contents of the current directory into the working directory inside the container
COPY . .
COPY Utils/configurations.py infra/
COPY Utils/users.py Utils/
COPY Utils/generate_string.py Utils/
# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the test runner when the container starts
#CMD ["python", "./test_api/test_runner.py"]

CMD ["python", "-m", "unittest", "./Test/non_parallel/serial_home_tests.py"]
