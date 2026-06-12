from fastapi.testclient import TestClient


class TestBookAPI:

    def test_root_endpoint(self, client):
        """Тест корневого эндпоинта"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json() or "Сообщение" in response.json()

    def test_create_book_success(self, client, sample_book):
        """Тест успешного создания книги"""
        response = client.post("/books/", json=sample_book)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["message"] == "Book created"

    def test_create_book_invalid_data(self, client):
        """Тест создания книги с невалидными данными"""
        invalid_book = {"title": 123, "author": "Author"}
        response = client.post("/books/", json=invalid_book)
        assert response.status_code == 422

    def test_get_all_books_empty(self, client):
        """Тест получения всех книг (пусто)"""
        response = client.get("/books/")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_all_books_with_data(self, client, created_book):
        """Тест получения всех книг (с данными)"""
        response = client.get("/books/")
        assert response.status_code == 200
        books = response.json()
        assert len(books) == 1
        assert books[0]["title"] == "1984"

    def test_get_book_by_id(self, client, created_book):
        """Тест получения книги по ID"""
        book_id = created_book["id"]
        response = client.get(f"/books/{book_id}")
        assert response.status_code == 200
        book = response.json()
        assert book["id"] == book_id
        assert book["title"] == "1984"

    def test_get_book_not_found(self, client):
        """Тест получения несуществующей книги"""
        response = client.get("/books/99999")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()

    def test_delete_book(self, client, created_book):
        """Тест удаления книги"""
        book_id = created_book["id"]
        response = client.delete(f"/books/{book_id}")
        assert response.status_code == 204

        get_response = client.get(f"/books/{book_id}")
        assert get_response.status_code == 404

    def test_search_books(self, client, sample_book):
        """Тест поиска книг"""
        client.post("/books/", json=sample_book)

        response = client.get("/books/search/?q=Orwell")
        assert response.status_code == 200
        results = response.json()
        assert len(results) == 1
        assert results[0]["author"] == "George Orwell"