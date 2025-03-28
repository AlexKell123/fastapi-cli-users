from fastapi import APIRouter


def get_position_router(service):
    router = APIRouter(prefix="/positions", tags=["positions"])

    @router.post("/")
    def create_position(title: str):
        return service.create(title)

    @router.get("/{position_id}")
    def read_position(position_id: int):
        return service.read(position_id)

    @router.put("/{position_id}")
    def update_position(position_id: int, title: str):
        return service.update(position_id, title)

    @router.delete("/{position_id}")
    def delete_position(position_id: int):
        return service.delete(position_id)

    return router
