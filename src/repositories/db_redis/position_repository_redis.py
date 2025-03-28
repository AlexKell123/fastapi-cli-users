class PositionRepositoryRedis:
    def __init__(self, database, er_handler):
        self._db = database
        self._error_handler = er_handler

    def create(self, title: str):
        position_id = self._db.db.incr("position_counter")
        key = f"position:{position_id}"
        data = {"title": title}
        self._db.db.hmset(key, data)
        return {f"{key} created": data}

    def read(self, position_id: int):
        key = f"position:{position_id}"
        data = self._db.db.hgetall(key)
        if not data:
            return self._error_handler.not_found(key)
        return {key: data}

    def update(self, position_id: int, title: str):
        key = f"position:{position_id}"
        position = self._db.db.hgetall(key)
        if not position:
            return self._error_handler.not_found(key)
        data = {"title": title}
        self._db.db.hmset(key, data)
        return {f"{key} updated": data}

    def delete(self, position_id: int):
        key = f"position:{position_id}"
        position = self._db.db.hgetall(key)
        if not position:
            return self._error_handler.not_found(key)
        self._db.db.delete(key)
        return {"message": f"{key} deleted"}
