# Basic-Sales-Summary-
1️⃣ create_database.py

Creates an SQLite database (sales_data.db)

Creates a table sales with columns: id, date, product, quantity, price

Inserts 5 rows of sample data

Closes connection after creation

Prints:
Database created and data inserted successfully!

2️⃣ sales_summary.py

Connects to sales_data.db

Executes SQL query to calculate total quantity and revenue per product.

Stores result in Pandas DataFrame

Displays the sales summary in console

Generates a bar chart using matplotlib (product vs revenue)

Closes connection after completion

3️⃣ sales_data.db

This is the database file created by create_database.py.

4️⃣ requirements.txt

Lists required packages:

nginx
pandas
matplotlib

