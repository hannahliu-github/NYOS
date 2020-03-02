FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

COPY main.py /app

COPY src/get_data.py /app/src/get_data.py

RUN pip install -r requirements.txt