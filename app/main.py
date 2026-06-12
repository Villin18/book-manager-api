from fastapi import FastAPI
from app.routers.books import router as books_router

app = FastAPI(title="Book Manager API")

app.include_router(books_router)

@app.get("/")
def root():
    return {"Сообщение": "Book API Работает!"}

