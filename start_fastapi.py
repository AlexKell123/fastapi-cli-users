import uvicorn
from fastapi import FastAPI

from src.init_services import init_services
from src.gateways import get_user_router, get_position_router


user_service, position_service = init_services('config.json', 'fastapi')

app = FastAPI()

user_router = get_user_router(user_service)
position_router = get_position_router(position_service)
app.include_router(user_router)
app.include_router(position_router)

if __name__ == "__main__":
    uvicorn.run("start_fastapi:app", host="0.0.0.0", port=8000, reload=True)
