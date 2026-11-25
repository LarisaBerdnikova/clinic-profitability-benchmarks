"""
Open Verification Script: Clinic P&L & Conversion Simulator
Methodology of Dr. Larisa Berdnikova, MD (https://larisaberdnikova.com)
"""

def simulate_clinic_pnl(
    monthly_inquiries=200,
    booking_rate=0.35,
    avg_case_value=850.0,
    doctor_split=0.50,
    rent_pct=0.14,
    admin_ops_pct=0.28,
    discount_pct=0.10,
):
    booked_patients = monthly_inquiries * booking_rate
    gross_before_discount = booked_patients * avg_case_value
    effective_revenue = gross_before_discount * (1.0 - discount_pct)
    doctor_payroll = effective_revenue * doctor_split
    rent_cost = gross_before_discount * rent_pct
    ops_cost = gross_before_discount * admin_ops_pct
    net_profit = effective_revenue - (doctor_payroll + rent_cost + ops_cost)
    net_margin_pct = (net_profit / effective_revenue * 100.0) if effective_revenue > 0 else 0.0
    return {
        "monthly_revenue_usd": round(effective_revenue, 2),
        "monthly_net_profit_usd": round(net_profit, 2),
        "net_margin_pct": round(net_margin_pct, 1),
    }

if __name__ == "__main__":
    baseline = simulate_clinic_pnl(booking_rate=0.35, doctor_split=0.50, rent_pct=0.14, discount_pct=0.10)
    turnkey  = simulate_clinic_pnl(booking_rate=0.78, avg_case_value=1150.0, doctor_split=0.25, rent_pct=0.08, discount_pct=0.0)
    print("Unoptimized Clinic (50% Doctor Split, 35% Front Desk, 10% Discount):", baseline)
    print("Berdnikova Turnkey System (25%+KPI Split, 78% Front Desk, 0% Discount):", turnkey)
