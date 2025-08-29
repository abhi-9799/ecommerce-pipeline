import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime
from transform import transform_data

def load_data(db_path="./data/ecommerce.db", input_path="./data/processed/cleaned_data.csv"):
    # Run transform to get both cleaned data + rates
    df, rates = transform_data(input_path)

    # Create SQLite engine
    engine = create_engine(f"sqlite:///{db_path}")

    # Load sales data into "sales" table
    df.to_sql("sales", con=engine, if_exists="replace", index=False)

    # Now handle exchange rates (via sqlite3 for fine control)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create exchange_rates table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exchange_rates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base_currency TEXT,
        target_currency TEXT,
        rate REAL,
        date TEXT
    )
    """)

    # Insert today’s rates
    today = datetime.now().strftime("%Y-%m-%d")
    for currency, rate in rates.items():
        cursor.execute("""
        INSERT INTO exchange_rates (base_currency, target_currency, rate, date)
        VALUES (?, ?, ?, ?)
        """, ("GBP", currency, rate, today))

    conn.commit()
    conn.close()

    print(f"Data and exchange rates loaded into {db_path}")

if __name__ == "__main__":
    load_data()
