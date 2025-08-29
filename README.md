# E-Commerce Sales ETL Pipeline

This project demonstrates a simple yet complete **ETL (Extract, Transform, Load) pipeline** using Python and SQL. The dataset contains anonymized e-commerce transactions, and the pipeline cleans, transforms, and loads the data into a relational database for analysis.

The goal of this project is to show practical, job-ready skills in building and working with ETL pipelines.

## ETL Workflow

### 1. Extract
- Raw data is downloaded from a public dataset (Kaggle).  
- Stored in the `data/raw/` folder.

### 2. Transform
- Clean missing or invalid values.  
- Standardize fields (e.g., dates, currencies).  
- Add derived columns such as revenue in USD.  
- Save cleaned data to `data/processed/`.

### 3. Load
- Load the processed dataset into a **SQLite database**.  
- Create a `sales` table for structured querying.

---

## Example Queries

A few example queries included in `queries.py`:

- Total number of transactions  
- Top 10 products by revenue  
- Revenue by country  
- Monthly sales trend  

These queries demonstrate how cleaned data can be used for reporting and insights.

---

## Technologies Used

- **Python** (pandas, SQLAlchemy, requests)  
- **SQLite** for database storage  
- **pandas** for data transformation and analysis  
- **Excel export** for reporting  

---

## How to Run

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
3. Run the pipeline:
   ```bash
   python scripts/transform.py
   python scripts/load.py
   python scripts/queries.py
4. Check the database (data/ecommerce.db)

## Key Skills Demonstrated

- Building and running an end-to-end ETL pipeline

- Data cleaning and transformation with pandas

- Database loading with SQLAlchemy + SQLite

- Writing SQL queries for insights and reporting

- Generating structured reports for stakeholders
