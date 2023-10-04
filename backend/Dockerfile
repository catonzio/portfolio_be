FROM python:latest

WORKDIR /portfolio

COPY ./requirements.txt /portfolio/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /portfolio/requirements.txt

COPY ./src /portfolio/src

WORKDIR /portfolio/src

CMD ["python3", "main.py"]
