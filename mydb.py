import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'spprottoy9999'
)

#prepare a cursor object
cursorObject =  database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")