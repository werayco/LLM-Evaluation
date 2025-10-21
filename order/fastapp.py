from fastapi.responses import JSONResponse
from fastapi import Request, FastAPI
from pydantic import BaseModel

service = FastAPI(
    description="this is an api the llm uses to book orders", version="1.0.0"
)

class responsemodel(BaseModel):
    status_code: int
    response: str


class requestmodel(BaseModel):
    user_id: int
    item_id: int
    quantity: int


@service.get("/", response_model=responsemodel)
async def health():
    return JSONResponse(content="health check route is active!", status_code=200)


@service.post("/api/v1/book", response_model=responsemodel)
async def book(req: requestmodel):
    payload = req.dict()
    print(f"Booking request: {payload}")

    return {
        "status_code": 201,
        "response": f"Appointment booked for user {req.user_id} (item {req.item_id}, qty {req.quantity})",
    }
