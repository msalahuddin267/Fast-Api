from fastapi import APIRouter
from app.config import db

router = APIRouter()

@router.get("/history")
async def get_allocations_history(employee_id: str = None, vehicle_id: str = None, date_from: str = None, date_to: str = None):
    query = {}
    if employee_id:
        query["employee_id"] = employee_id
    if vehicle_id:
        query["vehicle_id"] = vehicle_id
    if date_from and date_to:
        query["allocation_date"] = {"$gte": date_from, "$lte": date_to}
    
    allocations = await db.allocations.find(query).to_list(100)
    return allocations