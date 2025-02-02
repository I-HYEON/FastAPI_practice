from fastapi import FastAPI
from .routes import router

app = FastAPI()

# 라우터를 FastAPI 애플리케이션에 추가
app.include_router(router)