# CodeAlpha - Data Analytics Internship

Multi-tool data analytics project completed as part of the **CodeAlpha Data Analytics Internship**.
This repository covers multiple tasks combining web scraping, exploratory data analysis, and data visualization across Python, MySQL, Excel, and Power BI.

---

## 📋 Tasks Completed

| Task | Description | Status |
|------|-------------|--------|
| **Task 1** | Web Scraping | ✅ Complete |
| **Task 2** | Exploratory Data Analysis (EDA) | ✅ Complete |
| **Task 3** | Data Visualization | 🔄 In Progress |

*(Per CodeAlpha guidelines, minimum 2-3 tasks required for internship completion)*

---

## ✅ Task 1: Web Scraping

### Objective
Extract structured book data (title, price, rating, availability) from a public website using Python, and compile it into a clean, analysis-ready dataset.

### Tools Used
- **Python 3.13**
- `requests` – for fetching web pages
- `BeautifulSoup4` – for parsing HTML and extracting data
- `pandas` – for structuring and exporting data

### Target Website
[books.toscrape.com](https://books.toscrape.com) — a public sandbox site designed for scraping practice.

### Approach
1. Looped through all 50 catalogue pages of the site
2. For each page, parsed the HTML to extract:
   - Book title
   - Price (in GBP)
   - Star rating (converted from word format e.g. "Three" → `3`)
   - Stock availability
3. Added a 1-second delay between requests to avoid overloading the server
4. Compiled all records into a single structured dataset
5. Exported the final dataset to `books_data.csv`

### Output
- **File:** [`web_scraping/books_data.csv`](./web_scraping/books_data.csv)
- **Records scraped:** 1,000 books
- **Columns:** `Title`, `Price_gbp`, `Rating`, `Availability`

**Sample output:**

| Title | Price_gbp | Rating | Availability |
|-------|-----------|--------|--------------|
| A Light in the Attic | 51.77 | 3 | In stock |
| Tipping the Velvet | 53.74 | 1 | In stock |
| Soumission | 50.10 | 1 | In stock |
| Sharp Objects | 47.82 | 4 | In stock |
| Sapiens: A Brief History of Humankind | 54.23 | 5 | In stock |

### How to Run
```bash
cd web_scraping
pip install requests beautifulsoup4 pandas
python web_scraper.py
```

### Files
```
web_scraping/
├── web_scraper.py     # Scraping script
└── books_data.csv     # Scraped dataset (1000 records)
```

---

## ✅ Task 2: Exploratory Data Analysis (EDA)

### Objective
Explore the Superstore Sales dataset to understand its structure, clean it, and uncover meaningful business insights using statistics and visualizations.

### Tools Used
- **Python 3.13**
- `pandas` – data loading, cleaning, aggregation
- `matplotlib` / `seaborn` – visualizations

### Dataset
[Sample Superstore Sales Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) — 9,994 rows, 21 columns of retail order data (sales, profit, discount, region, category, customer details).

### Approach
1. Loaded and inspected the dataset (structure, data types, shape)
2. Checked data quality — missing values, duplicate rows
3. Cleaned the data:
   - Converted `Order Date` / `Ship Date` to datetime
   - Removed duplicate records
   - Engineered new columns: `Order Year`, `Order Month`, `Shipping Days`
4. Ran descriptive statistics on Sales, Profit, Discount, and Quantity
5. Answered 5 key business questions using groupby aggregations and correlation analysis
6. Visualized findings with 4 charts

### Key Insights

| Question | Finding |
|---|---|
| Most profitable category | **Technology** (₹145,454 profit) |
| Biggest loss-making sub-category | **Tables** (-₹17,725 loss) |
| Best performing region | **West** (highest sales & profit) |
| Discount vs Profit relationship | **Negative correlation (-0.219)** — higher discounts are associated with lower profit |
| Top customer by sales | **Sean Miller** (₹25,043) |

### Visualizations
| Chart | Insight |
|---|---|
| `profit_by_category.png` | Profit breakdown across Technology, Office Supplies, Furniture |
| `sales_by_region.png` | Sales & profit comparison across 4 regions |
| `discount_vs_profit.png` | Scatter plot showing discount's negative impact on profit |
| `monthly_sales_trend.png` | Sales trend over time, showing seasonality |

### Output
- **Cleaned dataset:** [`eda/superstore_cleaned.csv`](./eda/superstore_cleaned.csv)
- **Charts:** [`eda/`](./eda/) folder (4 PNG files)

### How to Run
```bash
cd eda
pip install pandas matplotlib seaborn
python eda_analysis.py
```

### Files
```
eda/
├── eda_analysis.py            # EDA script
├── Sample - Superstore.csv    # Raw dataset
├── superstore_cleaned.csv     # Cleaned dataset
├── profit_by_category.png
├── sales_by_region.png
├── discount_vs_profit.png
└── monthly_sales_trend.png
```

---

## 🔄 Task 3: Data Visualization

*Coming soon — Power BI dashboard built on cleaned Superstore Sales data.*

---

## 👤 Author

**Nikhil**
B.Tech CSE, Prabhat Engineering College (AKTU)
GitHub: [nikhil-1227](https://github.com/nikhil-1227)

---

## 📜 Internship Info

This project was completed as part of the **CodeAlpha Data Analytics Internship**.
- Website: [www.codealpha.tech](https://www.codealpha.tech)
