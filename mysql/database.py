import mysql.connector

#Install packages (mysql-connection, mysql-connection-python, mysql-connection-python-rf)

#Connect to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "111111",
    auth_plugin='mysql_native_password',
    database = 'testdb'
)

## Create cursor instance
my_cursor = mydb.cursor()

## Create database table
# my_cursor.execute('CREATE DATABASE testdb')

## Show all databases
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
#     print(db)

## Create tables and columns
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

## Show tables
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])

## Insert records
# insert_cmd = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("John", "john@codemy.com", 40)
# my_cursor.execute(insert_cmd, record1)
# mydb.commit()

## Insert multiple records
# insert_multi_cmd = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# records = [
#     ("Tim", "tim@tim.com", 32),
#     ("Mary", "mary@mary.com", 21),
#     ("Steve", "steve@steve.com", 57),
#     ("Tina", "tina@tina.com", 29),]

# my_cursor.executemany(insert_multi_cmd, records)
# mydb.commit()

## Update records
# update_cmd = "UPDATE users SET age = 41 WHERE user_id = 1"
# my_cursor.execute(update_cmd)
# mydb.commit()

## Delete records
del_cmd = "DELETE FROM users WHERE user_id = 7"
my_cursor.execute(del_cmd)
mydb.commit()

## Select columns
# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

