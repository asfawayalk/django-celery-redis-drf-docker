FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y gettext libgettextpo-dev

RUN mkdir /showcase
WORKDIR /showcase

ADD requirements.txt /showcase/
RUN pip install --default-timeout=100 -r requirements.txt

ADD . /showcase/
# ADD . /db.sqlite3
ADD flower /showcase/

