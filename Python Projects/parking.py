import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="pms")
mycursor=mydb.cursor()
def Add_Record():
    L=[]
    pid1=int(input("Enter the parking number : "))
    L.append(pid1)
    pname1=input("Enter the Parking Name: ")
    L.append(pname1)
    level1=input("Enter level of parking : ")
    L.append(level1)
    freespace1=input("Is there any freespace or not :YES/NO ")
    L.append(freespace1)
    vehicleno1=input("Enter the Vehicle Number : ")
    L.append(vehicleno1)
    nod1=int(input("Enter total number of days for parking: "))
    L.append(nod1)
    payment1=int(input("Enter total payment : "))
    L.append(payment1)
    stud=(L)
    sql="insert into parkmaster11 (pid,pnm,level,freespace,vehicleno,nod,payment) values (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    print("Parking details inserted successfully")
def RecView():
    print("Select the search criteria : ")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter Parking no : "))
        rl=(s,)
        sql="select * from parkmaster11 where pid=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        print("Details about Parking are as follows : ")
        print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
        for x in res:
            print(x)
    elif ch==2:
        s=input("Enter Parking Name : ")
        rl=(s,)
        sql="select * from parkmaster11 where pnm=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        print("Details about Parking are as follows : ")
        print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
        for x in res:
            print(x)
    elif ch==3:
        s=int(input("Enter Level of Parking : "))
        rl=(s,)
        sql="select * from parkmaster11 where level=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        print("Details about Parking are as follows : ")
        print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
        for x in res:
            print(x)
    elif ch==4:
        sql="select * from parkmaster11"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print("Details about Parking are as follows : ")
        print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
        for x in res:
            print(x)
def Vehicle_Detail():
    L=[]
    vid1=int(input("Enter Vehicle No : "))
    L.append(vid1)
    vnm1=input("Enter Vehicle Name/Model Name : ")
    L.append(vnm1)
    dateofpur1=input("Enter Date of purchase : ")
    L.append(dateofpur1)
    vdt=(L)
    sql="insert into vehicle (vid,vnm,dateofpur) values (%s,%s,%s)"
    mycursor.execute(sql,vdt)
    mydb.commit()
def Vehicle_View():
    vid=int(input("Enter the vehicle number of the vehicle whose details is to be viewed : "))
    sql="Select parkmaster11.pid,parkmaster11.pnm,parkmaster11.level,vehicle.vid,vehicle.vnm,vehicle.dateofpur from parkmaster11,vehicle where parkmaster11.pid=vehicle.vid "
    rl=(vid,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def remove():
    vid1=int(input("Enter the vehicle number of the vehicle to be deleted : "))
    rl=(vid1,)
    sql="Delete from vehicle where vid=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    print("Record has been deleted")
def Menu():
    print("Enter 1 : To Add Parking Detail")
    print("Enter 2 : To View Parking Detail ")
    print("Enter 3 : To Add Vehicle Detail ")
    print("Enter 4 : To Remove Vehicle Record")
    print("Enter 5 : To see the details of Vehicle")
    print("Enter 6 : Exit")
    input_dt = int(input("Please Select An Above Option: "))
    if(input_dt== 1):
        Add_Record()
    elif(input_dt==2):
        RecView()
    elif(input_dt==3):
       Vehicle_Detail()
    elif(input_dt==4):
       remove()
    elif(input_dt==5):
       Vehicle_View()
    elif(input_dt==6):
           runAgain()
    else:
       print("Enter correct choice. . . ")
       Menu()
def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menu()
    print("good Bye")
    quit()
#runAgn= input("\nwant To Run Again Y/n: ")
#runAgain()
Menu()
runAgain()

