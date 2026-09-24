from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, optimizer, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SmartProcure Engine API", version="1.0.0")

# Serve the static HTML frontend
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("app/static/index.html")

@app.post("/api/v1/vendors", response_model=schemas.VendorResponse)
def add_vendor(vendor: schemas.VendorCreate, db: Session = Depends(database.get_db)):
    db_vendor = models.Vendor(**vendor.model_dump())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@app.get("/api/v1/vendors", response_model=List[schemas.VendorResponse])
def get_vendors(db: Session = Depends(database.get_db)):
    return db.query(models.Vendor).all()

@app.post("/api/v1/procure/optimize")
def run_optimization(
    required_quantity: int,
    max_budget_per_unit: float,
    max_lead_time_days: int,
    db: Session = Depends(database.get_db)
):
    vendors = db.query(models.Vendor).all()
    if not vendors:
        raise HTTPException(status_code=400, detail="No vendors registered in database.")
        
    return optimizer.optimize_procurement(
        vendors=vendors,
        required_quantity=required_quantity,
        max_budget_unit=max_budget_per_unit,
        max_days=max_lead_time_days
    )
