FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3.11 python3.11-distutils

RUN apt-get install -y nano

RUN apt-get install -y python3-pip

RUN pip install aiogram

COPY . .

CMD ["python3", "main.py"]