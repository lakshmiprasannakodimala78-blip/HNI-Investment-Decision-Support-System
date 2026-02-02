def calculate_health_score(row):
    score = (
        row["RevenueGrowth"] * 30 +
        row["ProfitMargin"] * 25 +
        row["CashFlow"] * 25 +
        (1 - row["RiskScore"]) * 20
    )
    return round(score, 2)

def generate_pros_cons(row):
    pros, cons = [], []

    if row["RevenueGrowth"] > 0.15:
        pros.append("Strong revenue growth")
    else:
        cons.append("Low revenue growth")

    if row["ProfitMargin"] > 0.2:
        pros.append("High profit margin")
    else:
        cons.append("Low profitability")

    if row["CashFlow"] > 0.25:
        pros.append("Strong cash flow")
    else:
        cons.append("Weak cash flow")

    if row["RiskScore"] > 0.2:
        cons.append("High risk exposure")
    else:
        pros.append("Low risk profile")

    return ", ".join(pros), ", ".join(cons)
