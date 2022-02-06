FROM python:3.11-rc-bullseye

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python -m flask run