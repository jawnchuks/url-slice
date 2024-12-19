from fastapi import FastAPI
from app import routes
from loguru import logger



app = FastAPI(
    title="URL Slice",
    description="A simple and lightweight URL shortening service built with FastAPI.",
    version="1.0.0"
)

# Include the routes
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Slice API"}


logger.add("logs/url_shortener.log", rotation="1 MB", level="INFO")

@app.on_event("startup")
def startup_event():
    logger.info("Application started")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Application shutting down")

