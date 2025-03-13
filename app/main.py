from fastapi import FastAPI
from .routes import router

app = FastAPI(title="MinIO Bucket Service")

app.include_router(router)
