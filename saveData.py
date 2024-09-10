import mysql.connector

con = mysql.connector.connect(user='root', password='Ijse@1234', host='localhost')
cur = con.cursor()

# Create the 'test' database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS test")
cur.execute("USE test")
# Create the 'USER' table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS USER (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Get user input
userName = input("Enter your name: ")
userAge = input("Enter your age: ")

# Input validation
if not userName or not userAge:
    print("Please enter your name and age")
else:
    try:
        # Convert age to integer
        userAge = int(userAge)

        # Insert the data into the USER table
        cur.execute("INSERT INTO USER (name, age) VALUES (%s, %s)", (userName, userAge))
        con.commit()
        print("User added successfully!")

    except ValueError:
        print("Age must be an integer.")

cur.close()
con.close()
