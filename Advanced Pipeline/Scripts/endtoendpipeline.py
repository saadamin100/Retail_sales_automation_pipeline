import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import smtplib 

engine = create_engine('mysql+mysqlconnector://root:Saadsql2006!?@localhost/retail_store')
print("Successfully imported")

df = pd.read_sql_table('samplesuperstore', engine)
print(df)

Empty_rows = df.dropna(subset=['Sales', 'Profit'])
print(f"Your empty rows are {Empty_rows}")

null_data = df[df['Sales'].isnull() | df['Profit'].isnull()]
print(null_data)

Total_Sales = Empty_rows['Sales'].sum()
Total_Profit = Empty_rows['Profit'].sum()

print(f"The total sales are {Total_Sales} AND total profit is {Total_Profit}")

Empty_rows.to_sql('cleaned_superstore', engine)
print("Your data is in sql successfully")

sender_email = "muhammadsaadamin984@gmail.com"
reciever_email = "saadaminmemon875@gmail.com"
app_password = "ckrinkvsbvevwtcs"

subject = "Daily_Sales_Report"
body = f"The total sales are {Total_Sales} and Total profit is {Total_Profit}"
message = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
     server.login(sender_email, app_password)
     server.sendmail(sender_email, reciever_email, message)
    
    print("Congrats successfully send email")

except Exception as e:
    print("Can't able to send the message")
    








