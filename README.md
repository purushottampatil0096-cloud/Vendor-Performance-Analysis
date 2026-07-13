# Vendor Performance Analytics
### End-to-End Business Intelligence & Data Analytics Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey)
![SQL](https://img.shields.io/badge/SQL-Queries-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Executive Summary

Businesses often struggle to identify which vendors genuinely contribute to profitability, where procurement costs can be optimized, and how inventory affects financial performance.

This project develops a complete **end-to-end Vendor Performance Analytics solution** by integrating multiple transactional datasets into a unified analytical model. Using **Python, MySQL, SQL, Statistical Analysis, and Power BI**, the project transforms raw operational data into actionable business insights that support procurement, inventory, and vendor management decisions.

Unlike a traditional dashboard project, this repository demonstrates the complete analytics lifecycle—from ETL and database design to exploratory analysis, statistical validation, KPI engineering, and interactive reporting.

---

# Business Problem

A retail organization purchases products from hundreds of vendors.

Management needs answers to questions such as:

- Which vendors generate the highest revenue?
- Which vendors deliver the highest profit?
- How much inventory remains unsold?
- Is bulk purchasing reducing procurement costs?
- Which products deserve promotional investment?
- Which vendors create inventory risk?
- Is the business overly dependent on a small number of vendors?

The objective is to convert raw transactional data into business intelligence that supports strategic decision-making.

---

# Project Architecture

```
CSV Files
        │
        ▼
Python ETL Pipeline
        │
        ▼
MySQL Database
        │
        ▼
SQL Data Transformation
        │
        ▼
Vendor Sales Summary Table
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Testing
        │
        ▼
Power BI Dashboard
```

---

# Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Database | MySQL |
| Query Language | SQL |
| Data Processing | Pandas, NumPy |
| Database Connectivity | SQLAlchemy |
| Statistical Analysis | SciPy |
| Data Visualization | Matplotlib, Seaborn |
| Dashboard | Power BI |
| Notebook | Jupyter Notebook |
| Environment Variables | python-dotenv |
| Logging | Python Logging |

---

# Project Workflow

## 1. Data Ingestion

- Automated CSV ingestion
- Modular ETL pipeline
- MySQL integration
- Execution logging
- Runtime monitoring

---

## 2. SQL Data Modeling

Merged multiple datasets including:

- Purchases
- Purchase Prices
- Sales
- Vendor Invoices

using SQL joins and Common Table Expressions (CTEs) to generate a consolidated analytical dataset.

---

## 3. Data Cleaning

Performed:

- Missing value handling
- Data type conversion
- Infinite value replacement
- String normalization
- Data validation

---

## 4. Feature Engineering

Created several business KPIs including:

- Gross Profit
- Profit Margin
- Stock Turnover
- Sales-to-Purchase Ratio

These metrics significantly enhanced downstream analysis.

---

## 5. Exploratory Data Analysis

Performed:

- Distribution Analysis
- Outlier Detection
- Correlation Analysis
- Vendor Analysis
- Product Analysis
- Inventory Analysis
- Profitability Analysis

---

## 6. Statistical Analysis

Applied statistical techniques including:

- Confidence Intervals
- Welch's Independent Two Sample T-Test

to validate business hypotheses instead of relying only on visual observations.

---

## 7. Dashboard Development

Designed an interactive Power BI dashboard featuring:

- Executive KPI Cards
- Vendor Performance
- Revenue Analysis
- Profit Analysis
- Purchase Analysis
- Inventory Insights
- Interactive Filters

---

# Key Business Questions Answered

- Which vendors contribute the highest revenue?
- Which vendors are the most profitable?
- Which vendors have poor stock turnover?
- How much capital is locked in inventory?
- Which brands deserve promotion?
- Does purchasing in bulk reduce unit cost?
- How concentrated is vendor dependency?
- Are profit margins statistically different between top and low-performing vendors?

---

# Key Insights

- Top vendors account for a significant share of procurement, indicating vendor concentration risk.
- Large purchase volumes substantially reduce unit procurement cost.
- Several high-margin products underperform in sales and are strong candidates for targeted promotions.
- Low-performing vendors exhibit statistically higher profit margins.
- Millions of dollars remain tied up in slow-moving inventory.
- Stock turnover alone does not guarantee higher profitability.

---

# Business Recommendations

- Diversify procurement across vendors.
- Increase bulk purchasing where operationally feasible.
- Promote high-margin products rather than discounting them.
- Improve inventory planning for slow-moving products.
- Use vendor profitability metrics during procurement negotiations.

---

# Repository Structure

```
vendor-performance-analytics/

│
├── dashboard/
│      vendor_performance.pbix
│
├── data/
│
├── docs/
│      Vendor_Performance_Business_Report.md
│
├── images/
│
├── logs/
│
├── notebooks/
│      EDA.ipynb
│      Vendor_Performance_Analysis.ipynb
│
├── ingestion_db.py
├── get_vendor_summary.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── LICENSE
```

---

# Documentation

This repository also contains a detailed business report covering:

- Data Understanding
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Statistical Testing
- Business Insights
- Recommendations

📄 **Business Report**

```
docs/Vendor_Performance_Business_Report.md
```

---

# Skills Demonstrated

- Python Programming
- SQL
- MySQL
- ETL Pipeline Development
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Statistical Analysis
- Business Intelligence
- Power BI Dashboard Development
- Data Storytelling
- Business Problem Solving

---

# Future Improvements

- Apache Airflow pipeline scheduling
- Docker containerization
- Cloud deployment (AWS/Azure)
- Streamlit analytical application
- Automated data validation tests
- CI/CD integration using GitHub Actions

---

# Author

**Purushottam Patil**

Aspiring Data Analyst | Python | SQL | Power BI | MySQL | Business Intelligence | ETL | Data Visualization

If you found this project useful, feel free to ⭐ this repository.
