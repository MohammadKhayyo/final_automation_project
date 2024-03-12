FROM python:3.12


WORKDIR /usr/src/tests

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "test_api/test_runner.py"]