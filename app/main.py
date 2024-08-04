from fastapi import FastAPI
from app.api import users
from app.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API."}
