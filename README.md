# 📚 Book Manager API

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4-purple.svg)](https://pytest.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-ff69b4.svg)](https://sqlite.org/)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen.svg)]()

**REST API для управления библиотекой книг с полным набором автотестов.**

Проект создан для портфолио и демонстрирует навыки разработки на Python, написания автотестов, работы с базами данных и тестовой документации.

---

## ✨ Возможности

- ✅ **CRUD операции** — создание, чтение, обновление, удаление книг
- 🔍 **Поиск** — по названию, автору и жанру
- 📊 **Статистика** — общее количество книг, уникальных авторов, прочитанных книг
- 📄 **Пагинация и фильтрация** — удобная навигация по библиотеке
- 🧪 **Автотесты** — 19 тестов с покрытием 85%
- 📖 **Автодокументация** — Swagger UI и ReDoc
- 🐍 **Чистый SQL** — без ORM, полный контроль над запросами

---

## 🛠 Технологический стек

| Технология | Назначение |
|------------|------------|
| **FastAPI** | Веб-фреймворк для создания API |
| **SQLite3** | Лёгкая реляционная база данных |
| **Pytest** | Фреймворк для автотестов |
| **Pydantic** | Валидация данных и сериализация |
| **Uvicorn** | ASGI-сервер для запуска приложения |

---
## 📖 API Endpoints

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/` | Приветствие |
| GET | `/books` | Получить все книги |
| GET | `/books/{id}` | Получить книгу по ID |
| POST | `/books` | Создать новую книгу |
| PUT | `/books/{id}` | Обновить книгу |
| DELETE | `/books/{id}` | Удалить книгу |
| GET | `/books/search/?q=` | Поиск по ключевому слову |
| GET | `/stats/` | Получить статистику |

---

## 📝 Примеры запросов

### Создание книги

```bash
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "Dystopian",
    "is_read": true
  }'
```
## Пример ответа
```
{
  "id": 1,
  "message": "Book created"
}
```

В папке [`test-documentation/`](test-documentation) находится полная тестовая документация:

| Файл | Содержание |
|------|------------|
| `Test-Plan.md` | Стратегия тестирования, scope, риски |
| `Test-Cases.md` | 12 тест-кейсов с шагами и результатами |
| `Bug-Reports.md` | 4 баг-репорта с исправлениями |

---
