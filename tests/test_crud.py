import pytest
from app.crud import BookRepository


class TestBookRepository:

    def test_create_book(self, test_db):
        """Тест создания книги"""
        book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'year': 2020,
            'genre': 'Test Genre'
        }

        book_id = BookRepository.create(book_data)

        assert book_id is not None
        assert isinstance(book_id, int)
        assert book_id > 0

    def test_get_all_books_empty(self, test_db):
        """Тест получения всех книг (пустая БД)"""
        books = BookRepository.get_all()
        assert books == []
        assert isinstance(books, list)

    def test_get_all_books_with_data(self, test_db):
        """Тест получения всех книг (с данными)"""
        book_data = {'title': 'Book1', 'author': 'Author1'}
        BookRepository.create(book_data)

        books = BookRepository.get_all()

        assert len(books) == 1
        assert books[0]['title'] == 'Book1'
        assert books[0]['author'] == 'Author1'

    def test_get_by_id(self, test_db):
        """Тест получения книги по ID"""
        book_data = {'title': 'Unique Book', 'author': 'Unique Author'}
        book_id = BookRepository.create(book_data)

        book = BookRepository.get_by_id(book_id)

        assert book is not None
        assert book['id'] == book_id
        assert book['title'] == 'Unique Book'

    def test_get_by_id_not_found(self, test_db):
        """Тест получения несуществующей книги"""
        book = BookRepository.get_by_id(99999)
        assert book is None

    def test_update_book(self, test_db):
        """Тест обновления книги"""
        book_id = BookRepository.create({'title': 'Old Title', 'author': 'Author'})

        updates = {'title': 'New Title', 'year': 2023}
        result = BookRepository.update(book_id, updates)

        assert result is True

        book = BookRepository.get_by_id(book_id)
        assert book['title'] == 'New Title'
        assert book['year'] == 2023
        assert book['author'] == 'Author'

    def test_update_book_not_found(self, test_db):
        """Тест обновления несуществующей книги"""
        result = BookRepository.update(99999, {'title': 'New Title'})
        assert result is False

    def test_delete_book(self, test_db):
        """Тест удаления книги"""
        book_id = BookRepository.create({'title': 'To Delete', 'author': 'Author'})

        result = BookRepository.delete(book_id)

        assert result is True

        book = BookRepository.get_by_id(book_id)
        assert book is None

    def test_delete_book_not_found(self, test_db):
        """Тест удаления несуществующей книги"""
        result = BookRepository.delete(99999)
        assert result is False

    def test_search_books(self, test_db):
        """Тест поиска книг"""
        BookRepository.create({'title': 'Python Programming', 'author': 'John Doe'})
        BookRepository.create({'title': 'Java Basics', 'author': 'Jane Smith'})
        BookRepository.create({'title': 'Django Guide', 'author': 'John Doe'})

        results = BookRepository.search('John')
        assert len(results) == 2

        results = BookRepository.search('Python')
        assert len(results) == 1
        assert results[0]['title'] == 'Python Programming'

        results = BookRepository.search('xyz')
        assert results == []

