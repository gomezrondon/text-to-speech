FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY web.py ./web.py

# Install production dependencies.
RUN pip install Flask

ENTRYPOINT FLASK_APP=./web.py flask run --host=0.0.0.0