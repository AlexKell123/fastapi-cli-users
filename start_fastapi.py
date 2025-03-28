import uvicorn
from fastapi import FastAPI

from src.init_services import init_services
from src.gateways import get_user_router, get_position_router


def init_fastapi():
    user_service, position_service = init_services('config.json', 'fastapi')

    fastapi_app = FastAPI()

    user_router = get_user_router(user_service)
    position_router = get_position_router(position_service)
    fastapi_app.include_router(user_router)
    fastapi_app.include_router(position_router)

    return fastapi_app


app = init_fastapi()

if __name__ == "__main__":
    uvicorn.run("start_fastapi:app", host="0.0.0.0", port=8000, reload=True)
