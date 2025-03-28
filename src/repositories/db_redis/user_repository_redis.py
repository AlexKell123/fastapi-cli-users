class UserRepositoryRedis:
    def __init__(self, database, er_handler):
        self._db = database
        self._error_handler = er_handler

    def create(self, full_name: str, email: str):
        user_id = self._db.db.incr("user_counter")
        key = f"user:{user_id}"
        data = {"full_name": full_name, "email": email}
        self._db.db.hmset(key, data)
        return {f"{key} created": data}

    def read(self, user_id: int):
        key = f"user:{user_id}"
        data = self._db.db.hgetall(key)
        if not data:
            return self._error_handler.not_found(key)
        return {key: data}

    def update(self, user_id: int, full_name: str, email: str):
        key = f"user:{user_id}"
        user = self._db.db.hgetall(key)
        if not user:
            return self._error_handler.not_found(key)
        data = {"full_name": full_name, "email": email}
        self._db.db.hmset(key, data)
        return {f"{key} updated": data}

    def delete(self, user_id: int):
        key = f"user:{user_id}"
        user = self._db.db.hgetall(key)
        if not user:
            return self._error_handler.not_found(key)
        self._db.db.delete(key)
        return {"message": f"{key} deleted"}

    def read_by_email(self, email: str, ignore_key=None):
        ignore_key = f"b'user:{ignore_key}'"
        for key in self._db.db.scan_iter(match=f"user:*"):
            if str(key) != ignore_key and self._db.db.hget(key, "email").decode() == email:
                return self._db.db.hgetall(key)
