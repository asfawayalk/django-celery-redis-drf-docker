**This project includes**

- Django

- Django Rest Framework

- Flower

- Celery

- Celery Beat

- Docker

- Docker Compose

- Redis

- Postgres

- Swagger


**How to run the project**

**using docker**

docker-compose up --build

**usage**

***to create an item with celery***
got to 
POST localhost:8000/api/todo/, payload body {"name": "your name"}

***with restframework***
got to
POST localhost:8000/api/items/, payload body {"name": "your name"}

***credential***
the default user is
username: asfaw
password: password

you can use basic authentication for test