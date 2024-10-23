from datetime import date, datetime
from app.config import db

async def create_allocation(employee_id: str, vehicle_id: str, allocation_date: date):
    # Ensure the vehicle is not allocated for that day
    existing_allocation = await db.allocations.find_one({"vehicle_id": vehicle_id, "allocation_date": allocation_date})
    if existing_allocation:
        raise ValueError("Vehicle is already allocated on this date.")
    
    # Ensure the allocation date is not in the past
    if allocation_date < datetime.now().date():
        raise ValueError("Allocation date cannot be in the past.")
    
    # Insert new allocation
    allocation = {
        "employee_id": employee_id,
        "vehicle_id": vehicle_id,
        "allocation_date": allocation_date
    }
    
    await db.allocations.insert_one(allocation)
    return allocation


async def update_allocation(allocation_id: str, employee_id: str, vehicle_id: str, allocation_date: date):
    # Fetch the existing allocation
    allocation = await db.allocations.find_one({"_id": allocation_id})

    # Check if allocation exists
    if not allocation:
        raise ValueError("Allocation not found.")
    
    # Ensure the allocation date is not in the past
    if allocation["allocation_date"] < datetime.now().date():
        raise ValueError("Cannot update allocations for past dates.")
    
    # Ensure the vehicle is not already allocated for the new date
    if allocation_date != allocation["allocation_date"]:
        existing_allocation = await db.allocations.find_one({"vehicle_id": vehicle_id, "allocation_date": allocation_date})
        if existing_allocation:
            raise ValueError("Vehicle is already allocated on this date.")

    # Update the allocation
    updated_data = {
        "employee_id": employee_id,
        "vehicle_id": vehicle_id,
        "allocation_date": allocation_date
    }
    
    await db.allocations.update_one({"_id": allocation_id}, {"$set": updated_data})
    return updated_data

async def delete_allocation(allocation_id: str):
    allocation = await db.allocations.find_one({"_id": allocation_id})
    if allocation and allocation['allocation_date'] > datetime.now().date():
        await db.allocations.delete_one({"_id": allocation_id})
        return True
    return False