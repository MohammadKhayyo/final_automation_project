FROM python:3.12


WORKDIR /usr/src/tests

COPY . .
COPY Utils/ Utils/
COPY Utils/users.py Utils/
COPY Utils/generate_string.py Utils/

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install unzip
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*



#docker build --build-arg IMAGE_NAME=tests --build-arg TAG=latest -t tests:latest .