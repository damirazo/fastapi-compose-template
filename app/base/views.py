from fastapi import APIRouter

base_router = APIRouter(prefix='/base')


@base_router.get("/")
def read_root():
    return {"Hello": "World"}
