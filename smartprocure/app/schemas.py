from pydantic import BaseModel

class VendorCreate(BaseModel):
    name: str
    unit_price: float
    lead_time_days: int
    defect_rate: float
    max_capacity: int

class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True
