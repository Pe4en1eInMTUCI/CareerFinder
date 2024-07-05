FROM python:3.12.4-slim-bullseye

WORKDIR /CareerFinder/frontend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /CareerFinder/frontend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt