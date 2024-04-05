FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install

ENV FLASK_APP=./src/main.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=3000 \
    TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE1OTYwNzYwMjJ9.7

EXPOSE 3000

CMD pipenv run flask run