from fastapi import FastAPI

from app.base.views import base_router

app = FastAPI()

app.include_router(base_router)
