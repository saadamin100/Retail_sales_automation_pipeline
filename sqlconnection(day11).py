import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Saadsql2006!?@localhost/retail_project')

print("Connection Successful! Ab data khichne ki bari hai.")

query = """
SELECT 
    l.city, 
    p.category, 
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_location l ON f.location_id = l.location_id
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY l.city, p.category
"""

df = pd.read_sql(query, engine)

print(df.isnull().sum())

print(f"Total duplications are:, {df.duplicated().sum()}")
loss_making = df[df['total_profit'] < 0]
print(loss_making)

df.to_csv('daily_report.csv', index=False)
print("Daily report saved successfully")

