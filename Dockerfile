FROM python:3.12.1-alpine3.18

COPY web_app /web_app
COPY requirements.txt /web_app/temp/requirements.txt
RUN apk update && apk add postgresql postgresql-contrib

WORKDIR /web_app
RUN pip install -r temp/requirements.txt
EXPOSE 8000
RUN chmod a+rw /web_app/prep/is_updated.ini

RUN adduser --disabled-password app-user
USER app-user
