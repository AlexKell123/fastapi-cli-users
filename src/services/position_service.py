class PositionService:
    def __init__(self, repository):
        self._repository = repository

    def create(self, title: str):
        return self._repository.create(title)

    def read(self, position_id: int):
        return self._repository.read(position_id)

    def update(self, position_id: int, title: str):
        return self._repository.update(position_id, title)

    def delete(self, position_id: int):
        return self._repository.delete(position_id)
