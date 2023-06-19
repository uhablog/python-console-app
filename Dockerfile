FROM python:3.10

RUN mkdir /application
WORKDIR /application

RUN pip install --upgrade pip

ADD . /application/

CMD ["python", "main.py"]
