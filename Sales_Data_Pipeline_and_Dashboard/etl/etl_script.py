import pandas as pd
import sqlite3
from pathlib import Path
import os

# Paths
current_dir = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(current_dir, '../data/sales.csv'))
db_path = os.path.abspath(os.path.join(current_dir, '../db/sales.db'))

# Load CSV
print(f"Loading data from: {csv_path}")
df = pd.read_csv(csv_path)

# Transform
df.dropna(inplace=True)
df['order_date'] = pd.to_datetime(df['order_date'])
df['total_price'] = df['quantity'] * df['price']

# Ensure DB directory exists
Path(os.path.dirname(db_path)).mkdir(parents=True, exist_ok=True)

# Insert into SQLite
print(f"Inserting data into DB: {db_path}")
conn = sqlite3.connect(db_path)
df.to_sql('sales', conn, if_exists='replace', index=False)

# Verify
df_check = pd.read_sql("SELECT * FROM sales", conn)
print("\n✅ ETL Done. Sample loaded data:")
print(df_check.head())
