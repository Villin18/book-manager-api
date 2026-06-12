from app.DataBase import Database

db = Database()


class BookRepository:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM books")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(book_id: int):
        with db.get_connection() as conn:
            cursor = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def create(book_data: dict) -> int:
        with db.get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO books (title, author, year, genre, is_read) VALUES (?, ?, ?, ?, ?)",
                (
                    book_data['title'],
                    book_data['author'],
                    book_data.get('year'),
                    book_data.get('genre'),
                    book_data.get('is_read', 0)
                )
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def update(book_id: int, updates: dict) -> bool:
        with db.get_connection() as conn:
            fields = []
            values = []

            # Разрешенные поля для обновления
            allowed_fields = ['title', 'author', 'year', 'genre', 'is_read']

            for field in allowed_fields:
                if field in updates and updates[field] is not None:
                    fields.append(f"{field} = ?")
                    values.append(updates[field])

            if not fields:
                return False

            values.append(book_id)
            query = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"

            cursor = conn.execute(query, values)
            conn.commit()
            return cursor.rowcount > 0

    @staticmethod
    def delete(book_id: int) -> bool:
        with db.get_connection() as conn:
            cursor = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            return cursor.rowcount > 0

    @staticmethod
    def search(query: str):
        with db.get_connection() as conn:
            search_pattern = f"%{query}%"
            cursor = conn.execute(
                "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?",
                (search_pattern, search_pattern, search_pattern)
            )
            return [dict(row) for row in cursor.fetchall()]