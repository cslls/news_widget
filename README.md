# Новостной виджет для сайта

Простая новостная лента для внедрения на страницу.

```
#Запуск контейнера
docker-compose up --build
```

```
#При изменении models.py
docker exec -it app-news bash
python manage.py makemigrations
python manage.py migrate
```

Примерное содержание .env

```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
