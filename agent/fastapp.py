from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from agent.utils import hashgenerator
from agent.process import run_agent

app = FastAPI(
    title="LLM Order Booking API",
    version="1.0.0"
)

class Payload(BaseModel):
    username: str
    query: str
    hashed_data: str

@app.get("/health")
async def health_check():
    return JSONResponse(content={"message": "health check route is active!"}, status_code=200)

@app.get("/get-uuid")
async def get_uuid(username: str):
    salt, hashed_value = hashgenerator(username)
    return {"username": username, "salt": salt, "hashed_data": hashed_value}

@app.post("/api/chat")
async def chat_endpoint(req: Payload):
    try:
        model_response = run_agent(
            user_input=req.query,
            usersname=req.username,
            sessionID=req.hashed_data
        )
        return JSONResponse(
            content={"status": "success", "response": model_response},
            status_code=201
        )
    except Exception as e:
        return JSONResponse(
            content={"status": "error", "message": str(e)},
            status_code=500
        )
