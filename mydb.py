import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Owner_1998'
)

# Prepare cursor
cursorObj = db.cursor()

# Create a database
cursorObj.execute("CREATE DATABASE myCRM")

print("All Done!")
