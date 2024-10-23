from pydantic import BaseModel

class Vehicle(BaseModel):
    vehicle_id: str
    driver_name: str
    model: str
    plate_number: str