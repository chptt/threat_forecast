"""
Prepares aggregated data tables for the Cyberthreat Power BI Dashboard.
Run this script to generate the CSVs, then import them into Power BI Desktop.
"""

import pandas as pd
import os

os.makedirs("powerbi/data", exist_ok=True)

df = pd.read_csv("cyber_data.csv")
df["AttackDate"] = pd.to_datetime(df["AttackDate"], dayfirst=True)
df["Year"] = df["AttackDate"].dt.year
df["Month"] = df["AttackDate"].dt.to_period("M").astype(str)

THREAT_COLS = [
    "Spam", "Ransomware", "Local Infection",
    "Exploit", "Malicious Mail", "Network Attack",
    "On Demand Scan", "Web Threat"
]

# --- Table 1: Raw fact table (cleaned) ---
fact = df[["AttackDate", "Year", "Month", "Country"] + THREAT_COLS].copy()
fact.to_csv("powerbi/data/fact_threats.csv", index=False)
print("fact_threats.csv written:", len(fact), "rows")

# --- Table 2: Monthly threat totals (for trend line charts) ---
monthly = (
    df.groupby("Month")[THREAT_COLS]
    .mean(numeric_only=True)
    .reset_index()
)
monthly.to_csv("powerbi/data/monthly_avg_threats.csv", index=False)
print("monthly_avg_threats.csv written:", len(monthly), "rows")

# --- Table 3: Country-level averages (for map / bar charts) ---
country = (
    df.groupby("Country")[THREAT_COLS]
    .mean(numeric_only=True)
    .reset_index()
)
country["Total Threat Score"] = country[THREAT_COLS].sum(axis=1)
country.to_csv("powerbi/data/country_avg_threats.csv", index=False)
print("country_avg_threats.csv written:", len(country), "rows")

# --- Table 4: Threat type summary (for donut / KPI cards) ---
threat_summary = pd.DataFrame({
    "Threat Type": THREAT_COLS,
    "Global Average": [df[c].mean() for c in THREAT_COLS],
    "Global Max": [df[c].max() for c in THREAT_COLS],
})
threat_summary.to_csv("powerbi/data/threat_summary.csv", index=False)
print("threat_summary.csv written")

print("\nAll data files ready in powerbi/data/")
