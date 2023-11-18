FROM python:3.11-alpine

WORKDIR /project

COPY ./mcc ./mcc

COPY ./pyproject.toml ./

RUN pip install --no-cache-dir .
