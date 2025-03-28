# fastapi-cli-users

Сервис, реализующий CRUD-операции над сущностями User и Position, с помощью FastAPI и консольного приложения.
В качестве репозитория используется Redis или Sqlite в зависимости от настроек указанных в файле config.json.

Установка:
```shell
git clone https://github.com/AlexKell123/fastapi-cli-users
cd fastapi-cli-users
pip install -r requirements.txt 
```

Запуск FastAPI:
```shell
python start_fastapi.py
```

Запуск консольного приложения:
```shell
python start_cli.py
```
