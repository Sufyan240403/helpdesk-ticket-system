from fastapi import FastAPI
from routers import users, tickets
import models
from database import engine, Base 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "greetings, FastAPI is running!"}

app.include_router(users.router)
app.include_router(tickets.router)
models.Base.metadata.create_all(bind=engine)