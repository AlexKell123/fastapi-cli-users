class UserRepositorySqlite:
    def __init__(self, database, er_handler):
        self._db = database
        self._error_handler = er_handler
        self._db.execute_query('''CREATE TABLE IF NOT EXISTS users 
                                (id INTEGER PRIMARY KEY, full_name TEXT, email TEXT)''')

    def create(self, full_name: str, email: str):
        cursor = self._db.execute_query(f'INSERT INTO users (full_name, email) VALUES ("{full_name}", "{email}")')
        user_id = cursor.lastrowid
        key = f"user:{user_id}"
        data = {"full_name": full_name, "email": email}
        return {f"{key} created": data}

    def read(self, user_id: int):
        cursor = self._db.execute_query(f'SELECT * FROM users WHERE id = {user_id}')
        data = cursor.fetchone()
        key = f"user:{user_id}"
        if not data:
            return self._error_handler.not_found(key)
        return {key: data}

    def update(self, user_id: int, full_name: str, email: str):
        # self.read
        cursor = self._db.execute_query(f'SELECT * FROM users WHERE id = {user_id}')
        user = cursor.fetchone()
        key = f"user:{user_id}"
        if not user:
            return self._error_handler.not_found(key)
        data = {"full_name": full_name, "email": email}
        self._db.execute_query(f'UPDATE users SET full_name="{full_name}", email="{email}" WHERE id = {user_id}')
        return {f"{key} updated": data}

    def delete(self, user_id: int):
        # self.read
        cursor = self._db.execute_query(f'SELECT * FROM users WHERE id = {user_id}')
        user = cursor.fetchone()
        key = f"user:{user_id}"
        if not user:
            return self._error_handler.not_found(key)
        self._db.execute_query(f'DELETE FROM users WHERE id = {user_id}')
        return {"message": f"{key} deleted"}

    def read_by_email(self, email: str, ignore_key=None):
        query = f'SELECT id FROM users WHERE email = "{email}"'
        if ignore_key:
            query += f'AND id != {ignore_key}'
        cursor = self._db.execute_query(query)
        return cursor.fetchone()
