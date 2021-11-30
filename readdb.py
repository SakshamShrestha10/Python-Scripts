import mysql.connector
mydb = mysql.connector.connect(host= "localhost", user= "saksham", passwd= "saksham", database= "Office", auth_plugin= "mysql.native.paddword")
cursor = mydb.cursor()

sql = "SELECT * from Employee"
cursor.execute(sql)

data = cursor.fetchall()
count = cursor.rowcount

print("\r\n We have "+str(count)+" Employee \r\n")

for i in data:
    print("\r\n Employee ID: "+str(i[0])+"\r\n")
    print("Emloyee Name: "+i[1]+"\r\n")
    print("Employee Age: "+str(i[2])+"\r\n")
    print("Employee Role: "+i[3]+"\r\n")
