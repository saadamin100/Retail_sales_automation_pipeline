import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df = pd.read_csv('SampleSuperstore.csv')
print(df)

# 1. Pehle saare columns ko lowercase karlein taake naming ka rora khatam ho
# --- STEP 1: CLEAN NAMES ---
# Ye line Category, Sub-Category, Ship Mode sab ko category, sub_category, ship_mode bana degi
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

# --- STEP 2: DIM_CUSTOMERS ---
dim_customers = df[['segment']].drop_duplicates().reset_index(drop=True)
dim_customers['customer_id'] = dim_customers.index + 1

# --- STEP 3: DIM_LOCATION ---
loc_cols = ['country', 'city', 'state', 'postal_code', 'region']
dim_location = df[loc_cols].drop_duplicates().reset_index(drop=True)
dim_location['location_id'] = dim_location.index + 1

# --- STEP 4: DIM_PRODUCTS ---
prod_cols = ['category', 'sub_category'] # Ab ye lowercase aur underscores ke sath hai
dim_products = df[prod_cols].drop_duplicates().reset_index(drop=True)
dim_products['product_id'] = dim_products.index + 1

# --- STEP 5: FACT_SALES ---
# Join hamesha unhi columns par karein jo upar define kiye hain
fact_sales = df.merge(dim_customers, on='segment') \
               .merge(dim_location, on=loc_cols) \
               .merge(dim_products, on=prod_cols)

# Final columns filter
fact_sales = fact_sales[['customer_id', 'location_id', 'product_id', 'sales', 'quantity', 'discount', 'profit', 'ship_mode']]
# --- STEP 6: SQL CONNECTION ---

db_user = 'root'
db_password = 'Saadsql2006!?'  # <--- Yahan apna asli password likhein (e.g., '1234')
db_name = 'retail_project'
db_host = 'localhost'
db_port = '3306'

# Connection string ko is tarah likhein (f-string use karte waqt dhyan rakhein)
# Format: mysql+pymysql://user:password@host:port/database
connection_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connection_url)

try:
    # Tables bhejte waqt:
    dim_customers.to_sql('dim_customers', engine, if_exists='replace', index=False)
    dim_location.to_sql('dim_location', engine, if_exists='replace', index=False)
    dim_products.to_sql('dim_products', engine, if_exists='replace', index=False)
    fact_sales.to_sql('fact_sales', engine, if_exists='replace', index=False)
    print("Mubarak ho! Data SQL mein load ho gaya hai.")
except Exception as e:
    print(f"Abhi bhi error hai bhai: {e}")