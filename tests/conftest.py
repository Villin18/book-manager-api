import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from app.main import app
from app.DataBase import Database
from app.crud import db as global_db


@pytest.fixture
def test_db():
    """Создает временную БД для каждого теста"""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
        tmp_path = tmp.name

    test_db_instance = Database(tmp_path)

    global_db.db_path = tmp_path
    global_db._init_db()

    yield test_db_instance

    os.unlink(tmp_path)


@pytest.fixture
def client(test_db):
    """Тестовый клиент FastAPI"""
    return TestClient(app)


@pytest.fixture
def sample_book():
    """Образец книги для тестов"""
    return {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian",
        "is_read": True
    }


@pytest.fixture
def created_book(client, sample_book):
    """Создает книгу через API и возвращает её"""
    response = client.post("/books/", json=sample_book)
    assert response.status_code == 201
    return response.json()