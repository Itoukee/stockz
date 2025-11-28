from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title="StockZ API",
        description="FastAPI application using hexagonal architecture",
    )
    return app
