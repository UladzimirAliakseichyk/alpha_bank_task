FROM python:3.12.1-alpine3.18

RUN apk update && apk add postgresql postgresql-contrib

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic

COPY web-app /web-app
#COPY init.sql /docker-entrypoint-initdb.d/
WORKDIR /web-app
EXPOSE 8000

RUN adduser --disabled-password app-user

USER app-user