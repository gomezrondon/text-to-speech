FROM python:3.9-slim

COPY web.py ./web.py
COPY main.py ./main.py
COPY push_to_bucket.py ./push_to_bucket.py
COPY requirements.txt ./requirements.txt

# Install production dependencies.
RUN pip install -r requirements.txt

ENTRYPOINT FLASK_APP=./web.py flask run --host=0.0.0.0 --port=8080