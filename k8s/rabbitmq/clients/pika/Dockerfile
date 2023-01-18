FROM python:3.11.1-slim-buster

WORKDIR /scripts

RUN apt-get update \
    && apt-get install -y vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY client.py /scripts
