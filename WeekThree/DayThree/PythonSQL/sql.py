import mysql.connector

credentials = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="MyPassword1234",
    database="Lloyds"
)

query = credentials.cursor()
# selectID = credentials.cursor()
# cursor is our way of requesting things from mySQL in Python
# the query will use the credentials to request info

query.execute("SELECT * FROM Employees")
# selectID.execute("SELECT * FROM Employees WHERE EmployeeID = 4")
result = query.fetchall()

for item in result:
    print(item)