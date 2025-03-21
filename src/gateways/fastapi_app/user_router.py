from fastapi import APIRouter


def get_user_router(service):
    router = APIRouter(prefix="/users", tags=["users"])

    @router.post("/")
    def create_user(full_name: str, email: str):
        return service.create(full_name, email)

    @router.get("/{user_id}")
    def read_user(user_id: int):
        return service.read(user_id)

    @router.put("/{user_id}")
    def update_user(user_id: int, full_name: str, email: str):
        return service.update(user_id, full_name, email)

    @router.delete("/{user_id}")
    def delete_user(user_id: int):
        return service.delete(user_id)

    return router
