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
ADD start.sh /showcase/
ADD runserver.sh /showcase/
ADD wait-for-it.sh /showcase/
RUN chmod 755 /showcase/start.sh
RUN chmod 755 /showcase/runserver.sh
RUN chmod 755 /showcase/wait-for-it.sh


CMD ["bash", "server.sh"]
