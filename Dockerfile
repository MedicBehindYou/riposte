# Not Done Yet
FROM debian:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3

RUN pip install sqlalchemy uvicorn fastapi

COPY . /app

RUN mkdir /config && mkdir /app/downloads

RUN chmod 777 /app/ -R

ENTRYPOINT ["python3", "-u", "/app/main.py"]