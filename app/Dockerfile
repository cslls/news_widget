FROM python:3.9-slim-bullseye
RUN apt-get update && \
    apt-get install -y  libpq-dev gcc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY app/ /app/
#RUN python manage.py makemigrations
