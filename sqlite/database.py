import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

## Create a table
# c.execute('''
#           CREATE TABLE customers (
#               first_name text,
#               last_name text,
#               email text
#           )
#           ''')



## Insert records
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@mary.com')")

## Select records
c.execute("SELECT * FROM customers")
tables = c.fetchall()
print(tables)


# Commit our command
conn.commit()


# Cloase our connection
conn.close()