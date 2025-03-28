class PositionRepositorySqlite:
    def __init__(self, database, er_handler):
        self._db = database
        self._error_handler = er_handler
        self._db.execute_query('''CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, title TEXT)''')

    def create(self, title: str):
        cursor = self._db.execute_query(f'INSERT INTO positions (title) VALUES ("{title}")')
        position_id = cursor.lastrowid
        key = f"position:{position_id}"
        data = {"title": title}
        return {f"{key} created": data}

    def read(self, position_id: int):
        cursor = self._db.execute_query(f'SELECT * FROM positions WHERE id = {position_id}')
        data = cursor.fetchone()
        key = f"position:{position_id}"
        if not data:
            return self._error_handler.not_found(key)
        return {key: data}

    def update(self, position_id: int, title: str):
        # self.read
        cursor = self._db.execute_query(f'SELECT * FROM positions WHERE id = {position_id}')
        position = cursor.fetchone()
        key = f"position:{position_id}"
        if not position:
            return self._error_handler.not_found(key)
        data = {"title": title}
        self._db.execute_query(f'UPDATE positions SET title="{title}" WHERE id = {position_id}')
        return {f"{key} updated": data}

    def delete(self, position_id: int):
        # self.read
        cursor = self._db.execute_query(f'SELECT * FROM positions WHERE id = {position_id}')
        position = cursor.fetchone()
        key = f"position:{position_id}"
        if not position:
            return self._error_handler.not_found(key)
        self._db.execute_query(f'DELETE FROM positions WHERE id = {position_id}')
        return {"message": f"{key} deleted"}
