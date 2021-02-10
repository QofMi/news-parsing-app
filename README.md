# Приложение агрегатор новостей (Django REST Framework)

## Как запустить
### Первоначальная установка
```
cd news-parsing-app
pip install -r requirements.txt
cd news-parsing-app/api
python manage.py migrate
```

### Запуск сервера
```
cd news-parsing-app/api
python manage.py runserver
```

### Запуск тестов

Тесты следует запускать при работающем сервере.

```
cd news-parsing-app/api
python manage.py test
```

## Описание API

См. [API.md](API.md)
