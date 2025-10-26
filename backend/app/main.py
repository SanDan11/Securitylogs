from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db_setup import Base, engine
from app.models import user, incident, dar

from app.routers import users, incidents, dars

app = FastAPI(title="SecurityLogs API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(incidents.router)
app.include_router(dars.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the SecurityLogs API"}