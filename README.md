# test_cargo

Тестовое задание на вакансию Junior+ Backend specialist Remote в компанию SMIT.Studio

## Стек

- **[FastAPI](https://fastapi.tiangolo.com/)** (Python 3.11)
- **[PostgreSQL](https://www.postgresql.org/)** База данных
- **[Tortoise ORM](https://tortoise.github.io/)** ORM
- **[Aerich](https://github.com/tortoise/aerich)** Для миграций базы данных
- **[Docker Compose](https://docs.docker.com/compose/)**

## Запуск 

Склонируйте проект:

```
git clone https://github.com/Niolum/test_cargo.git
```

Создайте базу данных и файл ``.env``. Поместите туда переменные среды:

```
DATABASE_URL = "asyncpg://username:password@localhost/db_name"
```

Далее настройте виртуальную среду и основные зависимости из файла ``requirements.txt``

```
python -m venv venv
source venv/bin/activate 
# or for windows
venv/Scripts/activate 
pip install -r requirements.txt
```

Чтобы запустить веб-приложение, используйте::

```
uvicorn main:app --reload
```


Для запуска с помощью docker-compose сделайте следующие измения в файле ``.env``:

```
DATABASE_URL = "asyncpg://username:some_password@cargodb/some_name_db"
POSTGRES_USER=username
POSTGRES_PASSWORD=some_password
POSTGRES_DB=some_name_db
```

Запускаем через docker-compose:

```
docker-compose up -d
```