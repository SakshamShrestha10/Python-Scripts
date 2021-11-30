#myfile = open("file.txt", "w+")

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="saksham", passwd="saksham", database="Office", auth_plugin="mysql_native_password")
cursor = mydb.cursor()

while(True):
    uName = input("Enter your name: ")
    if uName == 'quit':
        exit()
    uAge= input("Enter your age: ")
    uRole = input("Enter your role: ")

    sql = "INSERT INTO Employee (name, age, role) VALUES (%s, %s, %s) "
    vals = (uName, uAge, uRole)
    cursor.execute(sql, vals)
    mydb.commit() 

    #myfile.write("\r\nName: "+uName+" \r\n")
    #myfile.write("Age: "+uAge+" \r\n")
    #myfile.write("Role: "+uRole+" \r\n")
    print("\r\n Data saved to database")

