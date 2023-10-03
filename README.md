# Запуск веб-сервиса

1. Создать и активировать виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Установить зависимости:
```bash 
pip install -r requirements.txt
```

3. Создать в корневой директории проекта файл .env со следующими переменными окружения:
```bash
BROCKER_HOST=localhost # Хост брокера сообщения
BROCKER_PORT=8001 # Порт брокера сообщений
```

4. Запустить брокер сообщений. Для локальных тестов использовал Redis через Docker:

```bash
docker run --name redis-test -p 8001:6379 -d redis redis-server --loglevel warning
```

5. В отдельном терминале запустить Celery:
```bash
cd src
celery --app=service.celery worker
```

6. В отдельном терминале запустить веб-сервис:
```bash
uvicorn main:app --reload
```

Спецификация API с описанием доступных эндпоинтов доступна по адресам http://127.0.0.1:8000/redoc и http://127.0.0.1:8000/docs.
