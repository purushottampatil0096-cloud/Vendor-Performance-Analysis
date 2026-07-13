# Vendor Performance Analysis

**An End-to-End Data Analytics Project | SQL + Python (EDA, Statistics & Visualization)**

---

## Executive Summary

This project develops an end-to-end vendor performance analytics solution using SQL, Python, and Power BI to evaluate procurement efficiency, profitability, and inventory movement.

By integrating multiple transactional datasets into a consolidated analytical model, the project identifies vendor concentration risk, pricing opportunities, inventory inefficiencies, and profitability drivers. Statistical hypothesis testing and business-focused KPIs were used to validate findings and support data-driven recommendations.

The project demonstrates practical experience in ETL, SQL, exploratory data analysis, statistical analysis, feature engineering, and interactive dashboard development.



## 📌 Project Overview

Retail and wholesale businesses depend on strong vendor relationships to stay profitable. Choosing the right vendors, pricing products correctly, and managing inventory efficiently can be the difference between healthy margins and locked-up capital.

This project analyzes vendor and brand-level sales, purchase, and profitability data to answer a core business question:

> **Which vendors and brands are truly driving profitability, and where is the business losing money through pricing, inventory, or vendor inefficiencies?**

The analysis combines SQL (for data consolidation), Python (for cleaning, EDA, and statistical testing), and data visualization to turn raw transactional data into actionable business recommendations.

---

## 🎯 Business Objectives

- Identify vendors and brands that contribute the most (and least) to sales and profitability
- Detect brands that are under-priced relative to their potential margin, or over-priced relative to their sales
- Understand vendor concentration risk — how dependent the business is on a small set of top vendors
- Quantify the impact of bulk purchasing on unit cost
- Identify vendors with slow-moving inventory and capital locked in unsold stock
- Statistically test whether high-performing and low-performing vendors truly differ in profit margins

---

## 🛠️ Tools & Tech Stack

| Category | Tools |
|---|---|
| Database | MySQL |
| Data Processing | Python, Pandas, NumPy, SQLAlchemy |
| Statistical Analysis | SciPy (t-test, confidence intervals) |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |

---

## 🗂️ Data Understanding

The raw data was spread across four related tables in the database:

- **purchases** – actual purchase transactions: date, vendor, brand, quantity, and dollar amount
- **purchase_prices** – vendor-brand level actual purchase price (unique per vendor-brand combination)
- **vendor_invoice** – aggregated purchase data with freight cost, unique per vendor and PO number
- **sales** – actual sales transactions: brand, quantity sold, selling price, and revenue

Since the data needed for analysis was spread across these tables, a consolidated summary table (**`vendor_sales_summary`**) was built in SQL, aggregating:

- Purchase transactions per vendor
- Sales transactions per vendor
- Freight costs per vendor
- Actual product prices per vendor

Pre-aggregating this data avoided repeated expensive joins on large tables and made downstream dashboarding/reporting significantly faster.

### Data Cleaning

During validation, the following inconsistencies were identified and resolved:

- **Volume** column was stored as a string and converted to `FLOAT64`
- Extra whitespace in **Vendor Name** was stripped for consistent grouping
- **Infinite values** (from divide-by-zero cases in ratio columns like Profit Margin) were replaced and handled before loading to the database
- New derived features were engineered for deeper analysis: **Gross Profit, Profit Margin, Stock Turnover, and Sales-to-Purchase Ratio**

---

## 📊 Exploratory Data Analysis

### Distribution of Numerical Columns

![Distribution plots](images/01_distribution_plots.png)

### Outlier Detection

![Outlier boxplots](images/02_outlier_boxplots.png)

**Key observations from summary statistics:**

- **Gross Profit** had a minimum of **-52,002.78**, indicating some transactions were sold at a loss
- **Profit Margin** had cases trending toward negative infinity, pointing to transactions with zero or negative effective revenue
- Some products had **zero total sales quantity**, suggesting slow-moving or obsolete stock
- **Purchase and Actual Prices** showed large positive outliers (max ~5,681 and ~7,499 vs. means of ~24 and ~35), indicating a small set of premium products
- **Freight Cost** varied enormously (0.09 to 257,032), pointing to logistics inefficiencies or inconsistent bulk shipments
- **Stock Turnover** ranged from 0 to 274.5 — some products sell almost instantly while others sit in inventory indefinitely

### Categorical Distribution

![Categorical count plots](images/03_categorical_countplots.png)

### Correlation Analysis

![Correlation heatmap](images/04_correlation_heatmap.png)

**Correlation insights:**

- **Purchase Price** showed a weak correlation with both Total Sales Dollars (-0.012) and Gross Profit (-0.016) — price alone doesn't drive revenue or profit
- **Total Purchase Quantity** and **Total Sales Quantity** were almost perfectly correlated (0.999), confirming efficient inventory flow-through overall
- **Profit Margin** and **Total Sales Price** were negatively correlated (-0.179), suggesting margins shrink as sales price rises — likely due to competitive pricing pressure
- **Stock Turnover** had weak negative correlations with both Gross Profit (-0.038) and Profit Margin (-0.055) — faster turnover does not automatically mean higher profitability

---

## 💡 Identifying Brands for Pricing/Promotional Adjustment

Brands were flagged if they fell in the **bottom 15% of total sales** but the **top 15% of profit margin** — high-margin products that are underperforming on volume, and good candidates for promotional push or repricing.

![Brand promotional scatterplot](images/06_brand_promotional_scatterplot.png)

This highlighted a set of niche, high-margin brands (e.g. several wine and specialty spirit labels) that could benefit from increased marketing visibility rather than price cuts.

---

## ❓ Business Questions Answered

### 1. Which vendors and brands demonstrate the highest sales performance?

![Top vendors and brands](images/07_top_vendors_brands_barplot.png)

**Diageo North America Inc** led all vendors with **~$67.99M** in total sales, followed by Martignetti Companies (~$39.33M) and Pernod Ricard USA (~$32.06M). At the brand level, **Jack Daniels No. 7 Black** topped the list at **~$7.96M**, followed closely by Tito's Handmade Vodka and Grey Goose Vodka.

### 2. Which vendors contribute the most to total purchase dollars?

Diageo North America Inc again led with **$50.10M** in purchase dollars and **$17.89M** in gross profit, ahead of Martignetti Companies and Pernod Ricard USA.

### 3. How much of total procurement is dependent on the top vendors?

![Pareto chart of vendor contribution](images/08_vendor_pareto_chart.png)

![Vendor contribution donut chart](images/09_vendor_contribution_donut.png)

The **top 10 vendors account for 65.69%** of total purchase dollars — a meaningful concentration risk. If any one of these relationships were disrupted, it could materially affect supply continuity.

### 4. Does purchasing in bulk reduce unit price, and what's the optimal purchase volume?

![Bulk purchase boxplot](images/10_bulk_purchase_boxplot.png)

| Order Size | Avg. Unit Purchase Price |
|---|---|
| Small | $39.06 |
| Medium | $15.49 |
| Large | $10.78 |

Vendors buying in **large volumes pay ~72% less per unit** than those buying small quantities — a clear, quantifiable case for consolidating orders into larger, less frequent purchases wherever storage and cash flow allow.

### 5. Which vendors have low inventory turnover (excess/slow-moving stock)?

Vendors including **Alisa Carr Beverages, Highland Wine Merchants, and Park Street Imports** showed the lowest stock turnover ratios (all below ~0.75), indicating products that are purchased but not moving through sales at a healthy pace.

### 6. How much capital is locked in unsold inventory, and which vendors contribute the most?

Total unsold inventory across the business was valued at **~$2.71M**. The largest contributors were:

| Vendor | Capital Locked |
|---|---|
| Diageo North America Inc | $722.21K |
| Jim Beam Brands Company | $554.67K |
| Pernod Ricard USA | $470.63K |
| William Grant & Sons Inc | $401.96K |
| E & J Gallo Winery | $228.28K |

Interestingly, the same top-selling vendors also hold the most locked-up capital — a natural consequence of scale, but still an opportunity for tighter inventory planning.

### 7. Do top-performing and low-performing vendors differ in profit margin? (Statistical Testing)

![Confidence interval comparison](images/11_profit_margin_confidence_interval.png)

Using a **95% confidence interval**:

- **Top-performing vendors** (top 25% by sales): Mean profit margin **31.17%**, CI (30.74%, 31.61%)
- **Low-performing vendors** (bottom 25% by sales): Mean profit margin **41.55%**, CI (40.48%, 42.62%)

An independent two-sample **t-test** (Welch's, unequal variance) was run to confirm this statistically:

- **T-statistic: -17.64, p-value: 0.0000**
- **Result: The null hypothesis is rejected** — there is a statistically significant difference in profit margins between top and low-performing vendors.

This confirms that low-volume vendors are not underperforming on margin — they are actually operating at meaningfully *higher* margins, likely due to premium pricing or lower operational overhead. Their challenge is one of volume and visibility, not profitability.

---

## Business Impact

The analysis provides actionable insights that can help organizations:

- Reduce procurement costs through optimized bulk purchasing strategies.
- Minimize vendor dependency by identifying concentration risk.
- Increase revenue by promoting high-margin, low-volume products.
- Improve inventory planning and reduce capital locked in unsold stock.
- Support strategic vendor negotiations using profitability and performance metrics.


## ✅ Key Insights

1. **Vendor concentration risk is high** — 65.69% of purchases flow through just 10 vendors.
2. **Bulk purchasing is a strong, underused lever** — moving from small to large order sizes cuts unit cost by ~72%.
3. **High-margin, low-volume brands exist across the catalog** — these are candidates for promotion rather than discounting.
4. **Low-performing vendors have significantly higher margins**, statistically confirmed — the issue is sales volume, not pricing.
5. **~$2.71M in capital is tied up in unsold inventory**, concentrated among the largest vendors — an inventory optimization opportunity even at scale.
6. **Stock turnover and profitability are not directly linked** — fast-moving inventory doesn't guarantee higher profit margins.

## 📋 Recommendations

- **Diversify vendor dependency** to reduce concentration risk from the top 10 vendors
- **Encourage bulk ordering** where storage/cash flow permits, to capture unit-cost savings
- **Run targeted promotions** on high-margin, low-sales-volume brands instead of discounting them
- **Improve marketing and distribution** for low-performing (but high-margin) vendors to convert margin advantage into higher volume
- **Tighten inventory planning** for top vendors to reduce capital locked in unsold stock

---

## 📁 Project Structure

```
├── EDA.ipynb                          # SQL-based data consolidation & cleaning
├── Vendor_Performance_Analysis.ipynb  # EDA, business questions, statistical testing
├── images/                            # All exported charts used in this report
└── Vendor_Performance_Analysis_Report.md
```

---

*This project was built as an end-to-end data analytics case study combining SQL, Python (Pandas, Seaborn, SciPy), and statistical hypothesis testing to solve real vendor performance business problems.*
