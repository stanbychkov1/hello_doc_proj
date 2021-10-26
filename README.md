# helo_doc_tags

Данное приложение позволяет получить количество используемых на сайте html тэгов.

Требования:
1. Docker ([install](https://docs.docker.com/engine/install/))
2. Docker-compose ([install](https://docs.docker.com/compose/install/))

Запуск приложения:
Сперва скачайте приложение из репозитория:
```bash
git clone git@github.com:stanbychkov/hello_doc_proj.git
````
Затем создать .env файл с переменными и заполните все поля значениями, где есть <>:
````
DJANGO_SECRET_KEY='<secret_key>'
DJANGO_DEBUG=false
DOMAIN_NAME=localhost
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=<postgres_username>
POSTGRES_PASSWORD=<postgres_password>
DJANGO_DATABASE_HOST=db
DJANGO_DATABASE_PORT=5432
````
После следует запустить приложение с помощью команды docker-compose, находясь в корневой папке проекта:
```bash
docker-compose up --build
````
По ссылке [localhost/tags/](localhost/tags/) с помощью POST-запроса, в теле которого указан данные в формате:
```json
{
  "url": "<url>"
}
````
вы получите обратно индетификатор задания в виде json:
```json
{
  "task_id": "<task_id>"
}
````
По ссылке [localhost/tags/](localhost/tags/)<task_id> вы сможете получить весь список тэгов в формате json:

```json
{
  "tags": {
    "<tag>": 1,
    "<tag>": 3
  }
}
````
В случае если была переданна ссылка не на html-шаблон или задание еще выполянется, то вы получите ответ в формате json:
```json
{
  "response": "<response>"
}
````
