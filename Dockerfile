FROM python:3.14-slim-buster

WORKDIR /app

COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]