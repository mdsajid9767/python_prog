import mysql.connector as c
con=c.connect(
    host="localhost",
    user="sajid",
    passwd="sajid123",
    database="learn_mysql"
)
try:
    mycursor=con.cursor()
    sql="INSERT INTO student(name,class,roll,dob)VALUES(%s,%s,%s,%s)"
    val=("Rizwan","mca",12,"1999-12-03")
    mycursor.execute(sql,val)
    con.commit()
    # sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
    # val = ("John", "Highway 21")
    # mycursor.execute(sql, val)
except Exception as e:
    print(e)
print("Record Inserted...")

