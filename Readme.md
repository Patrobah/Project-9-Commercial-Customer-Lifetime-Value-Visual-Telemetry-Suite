# Project 9: Commercial Customer Lifetime Value Visual Telemetry Suite
### B2C Subscription Business Intelligence Architecture

## 📋 Project Overview
This enterprise-grade Business Intelligence suite provides advanced visual telemetry for a B2C Subscription-as-a-Service (SaaS) business model. Operating across a **600-day transactional window**, the suite engineers synthetic data, transforms relational tables into an optimized Star Schema, and delivers interactive executive dashboards in Power BI to track customer valuation, acquisition channel efficiency, and core operational profitability.

---

## 🛠️ Data Infrastructure & Telemetry Generation
The backend data engine is built using **Python (Pandas)** to generate highly realistic consumer purchase behaviors, subscription lifecycles, and operational overhead metrics. 

### Core Architecture (Star Schema)
- **`dim_customers` (Dimension Table):** Contains 3,000 unique B2C consumer profiles segmented by demographic parameters (`Signup_Age`), geographic markets (`Region`: Nairobi, Lagos, London, New York, Berlin), and marketing channels (`Acquisition_Channel`).
- **`fact_subscriptions` (Fact Table):** A dense transactional ledger recording daily recurring transactions, tiered software renewals (`Plan_Type`: Basic, Pro, Premium), contract pricing, and variable overhead parameters (`Operational_Cost_USD`).
- **`Dim_Calendar` (DAX-Engineered Dimension):** A dedicated, continuous date dimension table mapping the 600-day chronological timeline to avoid default hierarchies and guarantee perfect time intelligence.

---

## 🧮 Business Intelligence & Advanced DAX Suite
The analytical core consists of dedicated calculations engineered using Data Analysis Expressions (DAX) to parse commercial value:

*   **Total Revenue:** Gross cash flow tracking generated across the platform.
    ```dax
    Total_Revenue = SUM(fact_subscriptions[Invoice_Amount_USD])
    ```
*   **Total Active Customers:** Granular volume count of unique converting users.
    ```dax
    Total_Active_Customers = DISTINCTCOUNT(fact_subscriptions[Customer_ID])
    ```
*   **Customer Lifetime Value (CLV):** Critical B2C metric establishing the average gross value of an acquired consumer contract.
    ```dax
    Customer_Lifetime_Value = DIVIDE([Total_Revenue], [Total_Active_Customers], 0)
    ```
*   **Operational Overhead:** Dense compilation of server and customer service support parameters.
    ```dax
    Total_Cost = SUM(fact_subscriptions[Operational_Cost_USD])
    ```
*   **Gross Profit Margin %:** Tracks true enterprise platform profitability.
    ```dax
    Gross_Profit_Margin = DIVIDE([Total_Revenue] - [Total_Cost], [Total_Revenue], 0)
    ```

---

## 📊 Visual Telemetry Layout & Portfolio Insights
The finalized Power BI executive dashboard translates complex transactional streams into strategic business insights through a structured four-part layout grid:

1.  **Executive Core Cards:** Prominent summary metric headers showing **Total Gross Revenue**, **Total Active Consumer Scale**, and **Average Customer Lifetime Value** at an immediate glance.
2.  **600-Day Financial Performance Trend:** Chronological time-series visualization tracking **Revenue Pacing vs. Operational Overhead Costs** concurrently over the timeline.
3.  **Channel Performance Matrix Ledger:** Deep-dive operational spreadsheet matrix mapping individual traffic sources (Google SEO, Meta Ads, YouTube Influencers, Referrals) straight to customer volume and final profitability metrics.
4.  **Tier Plan & Regional Strength Mapping:** Dynamic column breakdowns and geographic bubble maps highlighting market penetration between EMEA and AMER zones, confirming product tier popularity.

---

## 🚀 Repository Structure
```text
├── data/
│   ├── dim_customers.csv          # Generated consumer profiles dimension
│   └── fact_subscriptions.csv     # Dense transactional subscription ledger
├── scripts/
│   └── telemetry_generator.py     # Python Pandas framework script
├── models/
│   └── clv_telemetry_suite.pbix   # Compiled Power BI Desktop workbook file
└── README.md                      # Professional project documentation
```
