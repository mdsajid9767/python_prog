import mysql.connector as c

con = c.connect(host="localhost", user="sajid", passwd="sajid123", database="learn_mysql")

# -----------------CHECK-CONNECTION----------------
# if con.is_connected():
#     print("Successfully Connected...")
# else:
#     print("Some issue...")

mycursor = con.cursor()

# -------------------CREATE-TABLE--------------------
#mycursor.execute("create table customer(name varchar(25), address varchar(50))")

# ---------------------SHOW-DATABASES&TABLES------------------
mycursor.execute("show tables")
for x in mycursor:
    print(x)