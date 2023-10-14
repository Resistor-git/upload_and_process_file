# upload_and_process_file
Тестовое задание для Picasso.
Текст задания в "задание.txt"

Проект позволяет загружать на сервер файлы и обрабатывать их с помощью Сelery.

## Как использовать
Скачать проект.

Создать в корневой папке проекта `/upload_and_process_file/` файл `.env` с `SECRET_KEY` (см. `.env.example`)

В терминале зайти в папку с файлом docker-compose.
Выполнить команду `docker compose up --build`

Отправить файл на сервер можно по адресу http://127.0.0.1:8001/upload/
Получить список файлов можно по адресу http://127.0.0.1:8001/files/

## Стэк
Django, Django Rest Framework, Celery, Redis, Docker