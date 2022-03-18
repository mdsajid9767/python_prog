import mysql.connector as crud
con=crud.connect(
    host="localhost",
    user="sajid",
    passwd="sajid123",
    database="learn_mysql"
)
mycursor = con.cursor()

def insert():
    name = input("enter student name")
    st_class = input("enter student class")
    roll = int(input("enter student roll"))
    dob = input("enter student date of birth")

    sql = ("insert into student(name,class,roll,dob) values (%s,%s,%s,%s)")
    val = (name,st_class,roll,dob)
    try:
        mycursor.execute(sql,val)
        con.commit()
    except Exception as e:
        print(e)
    print("---RECORD INSERTED SUCCESSFULLY...")

def read():
    try:
        mycursor.execute("select * from student")
        myresult = mycursor.fetchall()
        print("                      ---YOUR RECORDS---\n")
        for x in myresult:
            print("st_id = {} name = {} class = {} roll = {} date of birth = {}".format(x[0],x[1],x[2],x[3],x[4]))
    except Exception as e:
        print(e)

def update():
    u_id=input("enter st_id to update:- ")
    search_record(u_id)
    try:
        check=input("are you sure to update this record")
        if(check == 'y'):
            choice=int(input("what do you want to update \n1. name\n2. class\n3. roll\n4. date of birth"))
            if choice==1:
                new_name=input("enter your new name:- ")
                sql1="update student set name = %s where st_id = %s"
                val=(new_name, u_id)
                try:
                    mycursor.execute(sql1, val)
                    con.commit()
                except Exception as e:
                    print(e)
            elif choice==2:
                new_class = input("enter your new class:- ")
                sql2 = "update student set class = %s where st_id = %s"
                val = (new_class, u_id)
                try:
                    mycursor.execute(sql2, val)
                    con.commit()
                except Exception as e:
                    print(e)
            elif choice==3:
                new_roll = input("enter your new roll:- ")
                sql3 = "update student set roll = %s where st_id = %s"
                val3 = (new_roll, u_id)
                try:
                    mycursor.execute(sql3, val3)
                    con.commit()
                except Exception as e:
                    print(e)
            elif choice==4:
                new_dob = input("enter your new date of birth:- ")
                sql4 = "update student set dob = %s where st_id = %s"
                val = (new_dob, u_id)
                try:
                    mycursor.execute(sql4, val)
                    con.commit()
                except Exception as e:
                    print(e)
            else:
                print("invalid choice")
                menu()
            print("---RECORD UPDATED SUCCESSFULLY---")
        else:
            print("---RECORD IS NOT UPDATED---")
    except Exception as e:
        print(e)

def delete():
    d_id=input("enter st_id to delete:- ")
    search_record(d_id)
    try:
        sql = "delete from student where st_id = %s"
        val = (d_id,)
        check=input("are you sure to delete this record")
        if(check == 'y'):
            mycursor.execute(sql,val)
            con.commit()
            print("---RECORD DELETED SUCCESSFULLY---")
        else:
            print("---RECORD IS NOT DELETED---")
    except Exception as e:
        print(e)


def search_record(s_id):
    s_id1=int(s_id)
    try:
        mycursor.execute("select st_id from student")
        myresult=mycursor.fetchall()
        change_in_list = [item for t in myresult for item in t]
    except Exception as e:
        print(e)
    check=s_id1 in change_in_list
    if check== True:
        print("st_id {} is present...\n".format(s_id1))
        try:
            sql="select * from student where st_id=%s"
            val=(s_id,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            print("                      ---YOUR RECORDS---\n")
            for x in myresult:
                print("st_id = {} name = {} class = {} roll = {} date of birth = {}\n".format(x[0], x[1], x[2], x[3], x[4]))
        except Exception as e:
            print(e)
    else:
        print("st_id {} is not present...".format(s_id1))
        menu()

def exit1():
    con.close()
    return 'n'

def menu():
    check = 'y'
    while check == 'y':
        choice = int(input("enter your choice\n1. Insert\n2. Read\n3. Update\n4. Delete\n5. Search\n0. Exit\n"))
        if choice == 1:
            insert()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            s_id = input("enter st_id to search:- ")
            search_record(s_id)
        elif choice == 0:
            print("CONNECTION CLOSED ")
            print("PROGRAM TERMINATED")
            check=exit1()

menu()