from fastapi import APIRouter, HTTPException
from app.crud import BookRepository
from app.schemas import Book

router = APIRouter()


@router.get("/books", response_model=list[Book])
def get_books():
    return BookRepository.get_all()


@router.post("/books", status_code=201)
def create_book(book: Book):
    book_data = book.dict()
    book_data.pop('id', None)
    book_id = BookRepository.create(book_data)
    return {"id": book_id, "сообщение": "книга добавлена"}


@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = BookRepository.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    updates = book.dict()
    updates.pop('id', None)
    success = BookRepository.update(book_id, updates)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Book updated"}


@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    success = BookRepository.delete(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return None


@router.get("/books/search/")
def search_books(q: str):
    return BookRepository.search(q)


