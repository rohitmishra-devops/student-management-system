import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="studentdb"
)

cursor = con.cursor()

while True:
    print("\n1 Add Student")
    print("2 Show Students")
    print("3 Update Marks")
    print("4 Delete Student")
    print("5 Exit")

    choise = int(input("enter your choise"))
    if choise == 1:
        name = input("enter your name: ")
        rollno = int(input("enter your rollno: "))
        marks = int(input("enter your marks: "))
        cursor.execute("insert into student values (%s,%s,%s)", (name,rollno,marks))
        con.commit()
        print("student added ")

    elif choise == 2:
        cursor.execute("select * from student")
        data = cursor.fetchall()
        for row in data:
            print(row)

    elif choise == 3:
        rollno = int(input("enter your rollno : "))
        new_marks = int(input("enter your new marks : "))
        cursor.execute("update student set marks = %s where rollno =%s " , (new_marks,rollno))
        con.commit()
        print("updated")
    elif choise == 4:
        rollno = int(input("enter student rollno : "))
        cursor.execute("delete from student where rollno = %s",(rollno,))
        con.commit()
        print('student deleted: ')

    elif choise == 5:
        break
    else :
        print("invalid choise: ")
    

