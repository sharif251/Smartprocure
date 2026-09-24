def calculate_vendor_score(vendor, max_budget_unit: float, target_days: int) -> float:
    """
    Lower score = Better vendor match.
    Weights: 50% Cost, 30% Delivery Speed, 20% Quality (Defects)
    """
    cost_penalty = vendor.unit_price / max_budget_unit
    speed_penalty = vendor.lead_time_days / target_days
    quality_penalty = vendor.defect_rate * 100

    total_score = (0.50 * cost_penalty) + (0.30 * speed_penalty) + (0.20 * quality_penalty)
    return round(total_score, 4)

def optimize_procurement(vendors, required_quantity: int, max_budget_unit: float, max_days: int):
    # Filter out vendors that break budget or lead time limits
    eligible = [v for v in vendors if v.lead_time_days <= max_days and v.unit_price <= max_budget_unit]
    
    # Sort by lowest penalty score
    ranked_vendors = sorted(eligible, key=lambda v: calculate_vendor_score(v, max_budget_unit, max_days))
    
    allocation = []
    remaining_units = required_quantity
    
    for v in ranked_vendors:
        if remaining_units <= 0:
            break
        
        take_units = min(remaining_units, v.max_capacity)
        remaining_units -= take_units
        
        allocation.append({
            "vendor_id": v.id,
            "vendor_name": v.name,
            "units_allocated": take_units,
            "unit_price": v.unit_price,
            "total_cost": take_units * v.unit_price,
            "lead_time_days": v.lead_time_days,
            "score": calculate_vendor_score(v, max_budget_unit, max_days)
        })
        
    return {
        "status": "SUCCESS" if remaining_units == 0 else "PARTIAL_FULFILLMENT",
        "fulfilled_units": required_quantity - remaining_units,
        "unfulfilled_units": remaining_units,
        "allocation_plan": allocation
    }
