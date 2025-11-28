import uvicorn

from settings import settings
from app import create_app


app = create_app()

app_base_configs = {
    "host": settings.host,
    "port": settings.ports,
    "workers": settings.workers,
    "access_log": True,
}

if __name__ == "__main__":
    uvicorn.run("main:app", **app_base_configs)
