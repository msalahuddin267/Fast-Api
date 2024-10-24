from fastapi import FastAPI
from app.routes import vehicle, history

app = FastAPI()

app.include_router(vehicle.router)
app.include_router(history.router)

@app.get("/")
async def home():
    return {"message": "Welcome to Vehicle Allocation System"}