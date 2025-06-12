import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")


sample_data = [
    ('2025-06-01', 'Product A', 10, 100.0),
    ('2025-06-02', 'Product B', 5, 200.0),
    ('2025-06-03', 'Product A', 7, 100.0),
    ('2025-06-04', 'Product C', 3, 300.0),
    ('2025-06-05', 'Product B', 2, 200.0),
]

cursor.executemany("INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("Database created and data inserted successfully!")
