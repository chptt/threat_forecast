# Cyberthreat Forecast — Power BI Dashboard Setup

## Step 1: Generate Data Files
Run the prep script (only needed once, or when `cyber_data.csv` changes):
```bash
python powerbi/prepare_dashboard_data.py
```
This creates 4 CSVs in `powerbi/data/`:
| File | Used For |
|---|---|
| `fact_threats.csv` | Main fact table (all rows) |
| `monthly_avg_threats.csv` | Trend line charts |
| `country_avg_threats.csv` | Map & country bar chart |
| `threat_summary.csv` | KPI cards & donut chart |

---

## Step 2: Import into Power BI Desktop

1. Open Power BI Desktop → **Get Data → Text/CSV**
2. Import all 4 files from `powerbi/data/`
3. In **Power Query**, set `AttackDate` column type to **Date/Time**

---

## Step 3: Build the Dashboard (4 Pages)

### Page 1 — Overview
| Visual | Data |
|---|---|
| KPI Card: Avg Ransomware | `fact_threats[Ransomware]` |
| KPI Card: Avg Spam | `fact_threats[Spam]` |
| KPI Card: Avg Network Attack | `fact_threats[Network Attack]` |
| KPI Card: Avg Exploit | `fact_threats[Exploit]` |
| Donut Chart: Threat Distribution | `threat_summary` — Threat Type / Global Average |
| Slicer: Year | `fact_threats[Year]` |

### Page 2 — Trends Over Time
| Visual | Data |
|---|---|
| Line Chart: All threats over time | `monthly_avg_threats` — Month on X-axis, all threat cols as lines |
| Area Chart: Ransomware trend | `monthly_avg_threats[Month]` vs `[Ransomware]` |

### Page 3 — Country Analysis
| Visual | Data |
|---|---|
| Filled Map | `country_avg_threats[Country]` + `[Total Threat Score]` (color saturation) |
| Bar Chart: Top 15 countries by threat score | `country_avg_threats` sorted by `Total Threat Score` |
| Table: Country breakdown | All threat columns |

### Page 4 — Threat Deep Dive
| Visual | Data |
|---|---|
| Scatter Plot: Ransomware vs Exploit | `fact_threats` — X: Exploit, Y: Ransomware, Legend: Country |
| Clustered Bar: Threat type by country (top 10) | `fact_threats` filtered by slicer |
| Slicer: Country | `fact_threats[Country]` |
| Slicer: Date Range | `fact_threats[AttackDate]` |

---

## Step 4: Add DAX Measures
Copy measures from `powerbi/dax_measures.txt` into **Modeling → New Measure**.

---

## Step 5: Theme & Formatting Tips
- Use a dark theme (built-in "Executive" or import a custom JSON theme)
- Color palette suggestion: Red (#E63946) for high-risk, Amber (#F4A261) for medium, Blue (#457B9D) for low
- Enable **drill-through** on Country visuals to navigate to Page 4 filtered by that country
