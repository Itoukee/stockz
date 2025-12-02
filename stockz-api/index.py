import uvicorn


from infra.http_handler.user_handler import users_router
from settings import settings
from app import create_app


app = create_app()

app_base_configs = {
    "host": settings.host,
    "port": settings.ports,
    "workers": settings.workers,
    "access_log": True,
    "reload": True,
}


app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run("index:app", **app_base_configs)
