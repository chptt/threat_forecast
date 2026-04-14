# Cyberthreat Forecast

A data science project that analyzes and forecasts global cyberthreat trends across 225 countries using machine learning models, with a Power BI dashboard for interactive visualization.

---

## Project Structure

```
├── cyber_data.csv                          # Raw dataset (77,623 rows, 18 columns)
├── Cyberthreat_forecast.ipynb              # Main analysis & forecasting notebook
├── Cyberthreat_Forecasting_Detailed_Report.pdf  # Full project report
├── powerbi/
│   ├── prepare_dashboard_data.py           # Script to generate Power BI data files
│   ├── dax_measures.txt                    # DAX measures for Power BI
│   ├── dashboard_setup_guide.md            # Step-by-step Power BI setup guide
│   └── data/                               # Auto-generated CSVs for Power BI
│       ├── fact_threats.csv
│       ├── monthly_avg_threats.csv
│       ├── country_avg_threats.csv
│       └── threat_summary.csv
```

---

## Dataset

`cyber_data.csv` contains daily cyberthreat rates per country from **October 2022 to December 2023**.

| Column | Description |
|---|---|
| `AttackDate` | Date of observation |
| `Country` | Country name (225 countries) |
| `Spam`, `Ransomware`, `Local Infection`, `Exploit`, `Malicious Mail`, `Network Attack`, `On Demand Scan`, `Web Threat` | Threat rate (0–1) |
| `Rank *` | Country rank for each threat type |

---

## Prerequisites

- Python 3.8+
- Jupyter Notebook or Google Colab
- Power BI Desktop (for dashboard)

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Running the Notebook

### Option 1 — Local

```bash
git clone https://github.com/chptt/threat_forecast.git
cd threat_forecast
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook Cyberthreat_forecast.ipynb
```

### Option 2 — Google Colab

1. Upload `Cyberthreat_forecast.ipynb` and `cyber_data.csv` to your Colab session
2. Run all cells in order

---

## Notebook Walkthrough

The notebook covers these steps in order:

1. Loading & previewing the dataset
2. Exploratory Data Analysis (EDA) — distributions, correlations, country-level trends
3. Feature engineering — lag features, rolling mean, date parts, country encoding
4. Model training & evaluation on 5 models:

| Model | MAE | R² |
|---|---|---|
| Linear Regression | 0.0157 | 0.226 |
| Decision Tree | 0.0119 | 0.478 |
| SVM (RBF kernel) | — | — |
| Lasso Regression | — | — |
| Random Forest | — | — |

5. Actual vs Predicted visualizations for each model
6. 7-day future threat forecast

---

## Power BI Dashboard

The dashboard has 4 pages: Overview, Trends Over Time, Country Analysis, and Threat Deep Dive.

### Setup

**Step 1** — Generate the data files:

```bash
python powerbi/prepare_dashboard_data.py
```

**Step 2** — Open Power BI Desktop and import all 4 CSVs from `powerbi/data/` via `Get Data → Text/CSV`.

**Step 3** — Follow `powerbi/dashboard_setup_guide.md` to build the visuals.

**Step 4** — Paste DAX measures from `powerbi/dax_measures.txt` into `Modeling → New Measure`.

---

## License

MIT
