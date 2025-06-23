import sqlite3
import random

conn = sqlite3.connect("products.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS products")
c.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)
""")

names = [f"Product {i}" for i in range(1, 101)]
for name in names:
    c.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
              (name, "Electronics", round(random.uniform(1000, 5000), 2)))

conn.commit()
conn.close()
