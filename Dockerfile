# syntax=docker/dockerfile:1

FROM FROM --platform=linux/x86_64 python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
