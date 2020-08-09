# Задача
Напишите скрип для удаления файлов в указанной директории (и поддиректориях), дата создания у которых старше 6 месяцев и размер которых превышает заданный лимит.

## установка
```
python3 -m venv venv/
source venv/bin/activate
pip install -e .
```

## тестирование
```
pytest -s
```

## запуск
```
python index.py dir_0 1000
```