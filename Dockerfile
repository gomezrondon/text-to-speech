FROM python:3.9-slim

COPY web.py ./web.py
COPY requirements.txt ./requirements.txt

# Install production dependencies.
RUN pip install -r requirements.txt

ENTRYPOINT FLASK_APP=./web.py flask run --host=0.0.0.0 --port=8080