from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base
from app.database import engine
from app.routes.patient_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Health Prediction API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Health Prediction API Running Successfully"
    }