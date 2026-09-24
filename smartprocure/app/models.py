from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)        # Cost per unit ($/₹)
    lead_time_days = Column(Integer, nullable=False)  # Delivery speed in days
    defect_rate = Column(Float, nullable=False)       # Quality penalty (e.g. 0.02 = 2%)
    max_capacity = Column(Integer, nullable=False)    # Max units they can supply
