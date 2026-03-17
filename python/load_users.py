import pandas as pd
import mysql.connector

# baca csv
df = pd.read_csv("../dataset/users.csv")

# koneksi mysql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="userdb"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO users (user_id, income, employment, credit_score) VALUES (%s,%s,%s,%s)",
        (row["user_id"], row["income"], row["employment"], row["credit_score"])
    )

conn.commit()

print("Users data loaded successfully!")