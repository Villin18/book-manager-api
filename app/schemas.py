from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None
    is_read: bool = False