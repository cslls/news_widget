# Новостной виджет для сайта

Простая новостная лента для внедрения на страницу.

Запуск контейнера

```
docker-compose up --build
```

При изменении models.py

```
docker exec -it app-news bash
python manage.py makemigrations
python manage.py migrate
```

Для создания суперпользователя:

```
docker exec -it app-news bash
python manage.py createsuperuser
```

Примерное содержание .env

```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
Для добавления на сайт:
```
<div id="app"></div>
    <script src="http://16.16.82.26/static/widget/widget.js"></script>
    <link
      href="http://16.16.82.26/static/widget/widget.css"
      rel="stylesheet"
      type="text/css"
    />
```
