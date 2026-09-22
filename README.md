# BharatCorp Financial OS | AI-Powered Enterprise Financial Intelligence Platform
### Enterprise B2B Fintech & Corporate Treasury Analytics Suite (Indian Localization | INR ₹)
**Tech Stack**: Python (FastAPI, Scikit-Learn, Pandas, NumPy) | SQL (Kimball Star Schema & Analytical Views) | Conversational AI ("Artha AI") | Modern Enterprise Dark UI

---

## Executive Summary

**BharatCorp Financial OS** is a modern, enterprise-grade corporate treasury and financial intelligence platform designed specifically for the **Indian Corporate Ecosystem** (denominated in Indian Rupee `₹`, formatted in Indian Lakhs/Crores, aligned with the Indian Fiscal Calendar April 1 – March 31, and integrated with GST/TDS statutory compliance).

The platform bridges modern AI algorithms with dimensional data warehousing and corporate financial governance:
1. **Indian Corporate Financial Localization**: Denominated in INR (`₹`) with Indian numbering (`₹1.45 Cr`, `₹12.50 L`, `₹45,000`), Indian corporate banking accounts (HDFC Current, ICICI Payroll, SBI Term Deposit, Axis Treasury, Zerodha Liquid Funds), and authentic Indian enterprise vendors (AWS India, DLF CyberCity, WeWork, Tata Power, Swiggy Corporate, IndiGo, Zoho).
2. **Statutory GST & TDS Compliance Suite**: Real-time tracking of claimable GST Input Tax Credit (ITC) under Section 16 across 18%, 12%, and 5% slabs, TDS withholding under Sections 194J, 194C, and 194I, and Advance Tax statutory quarterly schedules.
3. **Descriptive Multi-Period Comparison Charts**:
   - **Monthly Corporate Cash Flow & Burn Analysis**: Dual-axis inflows vs. outflows with 30-day moving burn overlay.
   - **Indian FY Quarter-over-Quarter (QoQ) Comparison**: Grouped quarter-by-quarter comparison across Indian fiscal quarters (Q1 Apr-Jun, Q2 Jul-Sep, Q3 Oct-Dec, Q4 Jan-Mar).
   - **Departmental Budget vs. Actual Variance**: Variance analysis against annual and monthly cost-center budgets.
   - **Top 10 Vendor Concentration (Pareto 80/20)**: Supplier dependency and credit risk distribution.
   - **90-Day Predictive Cash Runway Forecast**: Monte Carlo time-series projections with P10/P90 confidence envelopes.
4. **Artha AI Financial Intelligence Engine**: Conversational assistant trained on corporate runway, monthly burn, GST ITC eligibility, TDS deduction guidelines, and Advance Tax calendars.
5. **Corporate Data Management**: Instant **Empty Slate** capability (`POST /api/database/empty`) to start fresh with zero transactions, along with **Seed Indian Data** (`POST /api/database/seed-indian`) to populate 3,000+ realistic multi-year enterprise records.

---

## Architectural Blueprint

flowchart TD
    subgraph Data_Layer [Data & Storage Layer]
        DG[Indian Enterprise Generator] -->|3,100+ Transactions (INR)| DB[(SQLite Star Schema Warehouse)]
        DB --> FT[fact_transactions]
        DB --> DD[dim_date (Indian FY)]
        DB --> DC[dim_categories]
        DB --> DM[dim_merchants (Indian B2B)]
        DB --> DA[dim_accounts (HDFC/ICICI/SBI)]
        DB --> DBG[dim_budgets]
        DB --> V_QOQ[vw_qoq_comparison]
        DB --> V_TAX[vw_gst_tds_summary]
    end

    subgraph AI_Engine [Python AI & Machine Learning]
        FT --> NLP[NLP Expense Categorizer<br/>Indian Corporate Memos]
        FT --> ANOM[Anomaly Detector<br/>IsolationForest + INR Outlier Thresholds]
        FT --> FC[Cash Runway Forecaster<br/>Cyclic Ridge Regression]
        FT --> ARTHA[Artha AI Conversational Assistant<br/>Runway, GST ITC, TDS 194J/C/I, Advance Tax]
    end

    subgraph Web_Portal [BharatCorp Financial OS Web Interface]
        AI_Engine --> API[FastAPI REST Services]
        DB --> API
        API --> UI_OVR[Executive Overview & Live Market Ticker]
        API --> UI_CMP[Comparisons & Trends (QoQ, Variance, Pareto)]
        API --> UI_ARTHA[Artha AI Interactive Chatbot]
        API --> UI_TAX[GST & TDS Statutory Tax Hub]
        API --> UI_AI[AI Sandbox & Inference Studio]
        API --> UI_LEDGER[Enriched Transaction Ledger Explorer]
        API --> UI_MODAL[Add Transaction & Empty Slate Modals]
    end
```

---


## Project Directory Structure

```
ai-expense-financial-analytics/
├── data/
│   ├── raw/
│   │   └── transactions_raw.csv           # Multi-year synthetic transaction dump
│   ├── processed/                         # Cleaned Star Schema CSVs for Power BI
│   │   ├── DimDate.csv
│   │   ├── DimCategories.csv
│   │   ├── DimMerchants.csv
│   │   ├── DimAccounts.csv
│   │   ├── DimBudgets.csv
│   │   ├── FactTransactions.csv
│   │   ├── VwMonthlyCashflow.csv
│   │   ├── VwCategoryMonthlyBurn.csv
│   │   └── Vw503020Compliance.csv
│   └── financial_analytics.db             # Relational SQLite database
├── sql/
│   ├── schema.sql                         # Star Schema DDL with foreign keys & indexes
│   ├── seed_data.sql                      # Seed data for categories, accounts & budgets
│   ├── analytics_queries.sql              # 10+ Production SQL financial analytics queries
│   └── views.sql                          # Analytical views for Power BI / reporting
├── src/
│   ├── config.py                          # Global Indian corporate config, tax rules & paths
│   ├── database.py                        # Database connection & query execution engine
│   ├── data_generator.py                  # High-fidelity Indian corporate transaction generator
│   ├── advisor.py                         # 50/30/20 rule evaluator, GST ITC & TDS analytics
│   ├── chatbot.py                         # Artha AI domain-trained conversational financial assistant
│   └── models/
│       ├── categorizer.py                 # NLP expense categorization model
│       ├── anomaly_detector.py            # IsolationForest & INR outlier detector
│       └── forecaster.py                  # Predictive cashflow & runway forecaster
├── power_bi/
│   ├── dax_measures.dax                   # 30+ Production DAX measures with full documentation
│   ├── power_query_etl.m                  # Power Query M-scripts for data ingestion
│   ├── power_bi_schema.json               # Semantic data model relationships & properties
│   ├── report_design_blueprint.md         # Visual wireframe & design guidelines for 4 pages
│   └── export_powerbi_data.py             # Script to extract SQLite data into Power BI CSVs
├── web/
│   ├── app.py                             # FastAPI backend application & REST endpoints
│   ├── static/
│   │   ├── css/
│   │   │   └── corporate_theme.css        # Modern Enterprise Dark Theme (B2B Fintech)
│   │   └── js/
│   │       └── dashboard.js               # Client controller, Chart.js, Artha AI & Modals
│   └── templates/
│       └── index.html                     # BharatCorp Financial OS Web Portal
├── tests/
│   ├── test_data_pipeline.py              # Tests for database tables, dimensions & integrity
│   ├── test_models.py                     # Tests for Categorizer, Anomaly Detector, Forecaster
│   └── test_sql_analytics.py              # Tests for analytical queries and calculations
├── run_demo.py                            # One-click startup script
├── run_tests.py                           # Self-contained test suite runner
├── requirements.txt                       # Python dependencies
└── README.md                              # Complete platform documentation
```

---

## AI & Machine Learning Architecture

### 1. NLP Expense Categorizer (`src/models/categorizer.py`)
- **Objective**: Accurately classify unstructured, noisy bank memo strings into standardized budget categories.
- **Preprocessing**: Strips card swipe tags (`POS`, `DEBIT`, `ACH`, `SWIPE`), terminal codes, store numbers, and authorization traces.
- **Representation**: Sublinear `TfidfVectorizer` extracting unigrams, bigrams, and trigrams.
- **Model**: Regularized `LogisticRegression` with calibrated probability estimation.
- **Performance**: Achieves **100% accuracy** on representative test sets with confidence metrics and tax-deductible eligibility tagging.

### 2. Financial Anomaly & Fraud Outlier Detector (`src/models/anomaly_detector.py`)
- **Objective**: Flag anomalous spending spikes, duplicate card charges, and irregular vendor charges in real time.
- **Algorithms**: Unsupervised Machine Learning (`LocalOutlierFactor` with novelty detection) combined with category-specific **Rolling Z-Scores** and IQR upper bounds.
- **Scoring**: Mapped to an intuitive risk score (`0.00` to `1.00`) and classified into `Normal`, `Medium Risk`, or `Critical Risk` with human-readable explanations (e.g., *"Z-Score 8.4: Spending is 6.2x higher than category mean"*).

### 3. Predictive Cashflow Forecaster (`src/models/forecaster.py`)
- **Objective**: Forecast daily expenditures for the next 30, 60, and 90 days, and calculate treasury runway in months.
- **Methodology**: Cyclical Ridge regression capturing:
  - Linear time-trend index.
  - Day-of-week seasonality (weekend vs. weekday variance).
  - Day-of-month surges (1st of month rent/investments, 15th payday).
- **Output**: Point projection `P50` flanked by `P10` (lower floor) and `P90` (upper ceiling) confidence intervals.

### 4. AI Strategic Financial Health Advisor (`src/advisor.py`)
- **50/30/20 Governance**: Tracks actual distribution against target macro-ratios:
  - **Needs (50%)**: Housing, utilities, groceries, healthcare, transit.
  - **Wants (30%)**: Dining, travel, SaaS subscriptions, electronics.
  - **Savings & Investments (20%)**: Index funds, 401(k), cash reserves.
- **Subscription Auditor**: Identifies recurring price creep, calculates annualized SaaS commitments, and flags consolidation opportunities.

---

## SQL Dimensional Modeling & Production Queries

### Star Schema Relationships
- `fact_transactions` -> `dim_date` (Many-to-One on `date_id`)
- `fact_transactions` -> `dim_categories` (Many-to-One on `category_id`)
- `fact_transactions` -> `dim_merchants` (Many-to-One on `merchant_id`)
- `fact_transactions` -> `dim_accounts` (Many-to-One on `account_id`)
- `dim_budgets` -> `dim_categories` (Many-to-One on `category_id`)

### Core Analytical Queries (`sql/analytics_queries.sql`)
1. **30-Day Moving Average Daily Outflow**: Smoothed operational burn rate using window functions.
2. **Month-over-Month (MoM) Outflow Variance**: Computes growth deltas via `LAG(total_outflow, 1) OVER (ORDER BY year, month)`.
3. **Pareto 80/20 Vendor Concentration**: Running cumulative totals to isolate the top 80% cost drivers.
4. **Subscription Price Creep**: Identifies recurring bills whose charge increased relative to prior months.
5. **AI Flagged Anomaly Incident Audit**: Filters and ranks all machine learning flagged risks.
6. **Cash Reserves Runway Analysis**: Computes runway in months based on liquid checking/cash reserves vs average net burn.

---

## Power BI Integration Suite

The project includes an enterprise-ready Power BI asset bundle in `power_bi/`:

1. **`dax_measures.dax`**: Over 30 production DAX formulas organized into:
   - Core Aggregations (`[Total Inflow]`, `[Total Outflow]`, `[Net Cash Flow]`)
   - Time Intelligence (`[Outflow YTD]`, `[MoM Outflow Growth %]`, `[Rolling 90D Outflow]`)
   - Budget Governance (`[Budget Variance $]`, `[Budget Variance %]`, `[Budget Burn Velocity %]`)
   - 50/30/20 Metrics (`[Needs Allocation %]`, `[Wants Allocation %]`, `[Financial Health Index]`)
   - Anomaly & Risk (`[Anomaly Count]`, `[Anomaly Exposure $]`, `[Anomaly Rate %]`)
   - Treasury & Runway (`[Liquid Cash Capital]`, `[Cash Runway in Months]`, `[Runway Health Status]`)
2. **`power_bi_schema.json`**: Semantic data model definition specifying table cardinalities, data types, and formatting strings.
3. **`power_query_etl.m`**: Power Query M-scripts for zero-friction ingestion from CSV or SQLite.
4. **`report_design_blueprint.md`**: Visual layout specifications for 4 executive pages:
   - *Page 1*: Executive C-Suite Command Center
   - *Page 2*: Expense Drilldown & Category Deep-Dive
   - *Page 3*: AI Anomaly Watch & Fraud Governance
   - *Page 4*: Cash Runway & Budget Allocation

---

## Classical Financial Executive Portal

The web application (`web/app.py`) runs on FastAPI with a custom **Classical Wall Street & Private Banking** design system:
- **Real-Time Ticker Ribbon**: Continuous header displaying market proxies, total inflow, outflow, runway, and anomaly counts.
- **Executive Dashboard**: Top KPI cards with gold borders, dual-axis monthly cashflow chart, category doughnut chart, and 50/30/20 animated progress meters.
- **Interactive AI Sandbox**:
  - Test custom bank memos against the NLP categorizer with real-time confidence scores.
  - Test individual amounts against the Anomaly Detector with instant risk verdicts.
  - Dynamically adjust the forecast horizon (30, 60, 90 days) with confidence intervals.
- **SQL Analytics Studio**: Interactive SQL terminal with 8 pre-loaded query templates, execution timer, and formatted tabular rendering.
- **Power BI Resource Hub**: Inspect and copy DAX formulas with one click and refresh processed datasets.
- **Transactions Ledger Explorer**: Real-time search, category filtering, anomaly badge tags, and client-side CSV export.

---

## Quick Start Guide

### Prerequisites
- Python 3.10+ (Python 3.11 recommended)
- `pip install -r requirements.txt`

### Launch the Application
Run the one-click bootstrap script from the project root:
```bash
python run_demo.py
```
This script will automatically:
1. Verify and initialize the SQLite database schema and views.
2. Generate 4,000+ realistic multi-year transactions spanning 2024 to 2026.
3. Train and persist the NLP Categorizer and Anomaly Detector models.
4. Export pre-packaged CSV datasets into `data/processed/` for Power BI.
5. Run all 11 unit tests to ensure pipeline integrity.
6. Launch the FastAPI server and open `http://127.0.0.1:8000` in your default browser.

### Run Unit Tests
To run the automated verification test suite:
```bash
python run_tests.py
```
All 11 unit tests will validate schema continuity, ML inference accuracy, and analytical calculations.
