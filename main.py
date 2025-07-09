from fastapi import FastAPI
from routes.translate import router
from utils.logger import init_db

app = FastAPI(title="Project Udaan Translation Microservice")

app.include_router(router)

@app.on_event("startup")
def startup_event():
    init_db()

