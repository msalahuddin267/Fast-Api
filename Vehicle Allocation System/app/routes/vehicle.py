from fastapi import APIRouter, HTTPException
from app.services.allocation import create_allocation, delete_allocation, update_allocation
from app.models.allocation import Allocation

router = APIRouter()

@router.post("/allocate", response_model=Allocation)
async def allocate_vehicle(allocation: Allocation):
    try:
        new_allocation = await create_allocation(allocation.employee_id, allocation.vehicle_id, allocation.allocation_date)
        return new_allocation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/update/{allocation_id}", response_model=Allocation)
async def update_allocation_endpoint(allocation_id: str, allocation: Allocation):
    try:
        updated_allocation = await update_allocation(allocation_id, allocation.employee_id, allocation.vehicle_id, allocation.allocation_date)
        return updated_allocation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{allocation_id}")
async def delete_allocation_endpoint(allocation_id: str):
    deleted = await delete_allocation(allocation_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="Could not delete the allocation")
    return {"detail": "Allocation deleted"}