import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute a query to fetch all results
cursor.execute('SELECT * FROM values_table')

# Fetch all results
rows = cursor.fetchall()
# Print the results
for row in rows:
    print(row)

# Now, delete all rows
cursor.execute("DELETE FROM values_table")
conn.commit()

# Close the connection
conn.close()
