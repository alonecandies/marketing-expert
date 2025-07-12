from fastapi import FastAPI
from app.api import auth, conversation, ai

app = FastAPI()

app.include_router(auth.router)
app.include_router(conversation.router)
app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"message": "Marketing Expert Backend is running."}
