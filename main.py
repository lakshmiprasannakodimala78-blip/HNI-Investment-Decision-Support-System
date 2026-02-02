import pandas as pd

from classification import classify_companies
from health_score import calculate_health_score, generate_pros_cons
from visualization import plot_market_cap

# Load dataset
df = pd.read_excel("Company.xlsx")

# Classify companies by market cap
df = classify_companies(df)

# Calculate health score
df["HealthScore (%)"] = df.apply(calculate_health_score, axis=1)

# Generate pros and cons
df["Pros"], df["Cons"] = zip(*df.apply(generate_pros_cons, axis=1))

# Display final dataframe
print("Final Investment Dataset:")
print(df)

# Plot visualization
plot_market_cap(df)
