import pytest
from types import SimpleNamespace
from app.optimizer import calculate_vendor_score, optimize_procurement

def test_calculate_vendor_score():
    # Mock vendor object using SimpleNamespace
    vendor = SimpleNamespace(
        id=1,
        name="Test Vendor",
        unit_price=100.0,
        lead_time_days=5,
        defect_rate=0.01,  # 1%
        max_capacity=500
    )
    
    # Calculate score against $150 budget and 10 day target limit
    score = calculate_vendor_score(vendor, max_budget_unit=150.0, target_days=10)
    
    # Verify score formula calculation:
    # (0.50 * 100/150) + (0.30 * 5/10) + (0.20 * 1.0) = 0.3333 + 0.15 + 0.20 = 0.6833
    assert score == 0.6833

def test_optimize_procurement_success():
    vendors = [
        SimpleNamespace(id=1, name="Vendor A (Expensive & Fast)", unit_price=120.0, lead_time_days=3, defect_rate=0.01, max_capacity=300),
        SimpleNamespace(id=2, name="Vendor B (Cheap & Slow)", unit_price=80.0, lead_time_days=12, defect_rate=0.05, max_capacity=500),
        SimpleNamespace(id=3, name="Vendor C (Balanced)", unit_price=90.0, lead_time_days=5, defect_rate=0.02, max_capacity=400),
    ]
    
    # Request 500 units with budget $100 and max 10 days
    result = optimize_procurement(
        vendors=vendors,
        required_quantity=500,
        max_budget_unit=100.0,
        max_days=10
    )
    
    assert result["status"] == "SUCCESS"
    assert result["fulfilled_units"] == 500
    assert result["unfulfilled_units"] == 0
    # Vendor B should be filtered out (lead time 12 > max 10 days)
    # Vendor A should be filtered out (unit price $120 > budget $100)
    # Vendor C should fulfill the allocation
    assert len(result["allocation_plan"]) == 1
    assert result["allocation_plan"][0]["vendor_id"] == 3
