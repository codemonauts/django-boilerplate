FROM python:3

ENV PYTHONUNBUFFERED 1

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /usr/local/bin/wait
RUN chmod +x /usr/local/bin/wait

RUN mkdir /code 
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN python -m pip install -r requirements.txt
