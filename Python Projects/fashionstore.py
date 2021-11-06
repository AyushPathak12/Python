import os
import platform
import mysql.connector
#import pandas as pd
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="fashion")
mycursor=mydb.cursor()
def AddProduct():
    L=[]
    stk=[]
    pid=input("Enter the Product ID : ")
    L.append(pid)
    IName=input("Enter the Product Name : ")
    L.append(IName)
    brnd=input("Enter the Product Brand Name : ")
    L.append(brnd)
    fr=input("Enter Male/Female/Kids : ")
    L.append(fr)
    sn=input("Enter Winter/Summer : ")
    L.append(sn)
    rate=int(input("Enter the Rates for Product :"))
    L.append(rate)
    product=(L)
    sql="Insert into product (product_id,PName,brand,Product_for,Season,rate)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,product)
    mydb.commit()
    stk.append(pid)
    stk.append(0)
    stk.append("No")
    st=(stk)
    sql="insert into stock(item_id, Instock, status) values(%s,%s,%s)"
    mycursor.execute(sql,st)
    mydb.commit()
    print("One Product inserted ")
def EditProduct():
    pid=input("Enter product ID to be edited : ")
    sql="select * from product where product_id=%s"
    ed=(pid,)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    for x in res:
        print(x)
        print("")
        fld=input("Enter the field which you want to edit : ")
        val=input("Enter the value you want to set : ")
        sql="Update product set " + fld +"='" + val + "' where product_id='" + pid + "'"
        sq=sql
        print(sq)
        mycursor.execute(sql)
        print("Editing Don : ")
        print("After correction the record is : ")
        sql="select * from product where product_id=%s"
        ed=(pid,)
        mycursor.execute(sql,ed)
        res=mycursor.fetchall()
        for x in res:
            print(x)
            mydb.commit()
def DelProduct():
    pid=input("Enter the Product)id to be deleted : ")
    sql="delete from sales where item_id=%s"
    id=(pid,)
    mycursor.execute(sql,id)
    mydb.commit()
    sql="delete from purchase where item_id=%s"
    mycursor.execute(sql,id)
    mydb.commit()
    sql="delete from stock where item_id=%s"
    mycursor.execute(sql,id)
    mydb.commit()
    sql="delete from product where product_id=%s"
    mycursor.execute(sql,id)
    mydb.commit()
    print("One Item Deleted")
def ViewProduct():
    print("Display Menu: Select the category to display the data")
    print("1. All Details")
    print("2. Product Name:")
    print("3. Product Brand:")
    print("4. Product For:")
    print("5. Product Season:")
    print("6. Product ID:")
    #x=0
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        sql="select * from product"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print(x)
            #x=1
    elif ch==2:
        var='PName'
        val=input("Enter the name of Product : ")
    elif ch==3:
        var='brand'
        val=input("Enter the name of Brand : ")
    elif ch==4:
        var='Product_for'
        val=input("Enter Male/Femal/Kids : ")
    elif ch==5:
         var='season'
         val=input("Enter the Season : ")
    elif ch==6:
        var='product_id'
        val=input("Enter the Product_id : ")
    if x==0:
        sql="select * from product where " + var + " = %s"
        sq=sql
        tp=(val,)
        mycursor.execute(sq,tp)

        res=mycursor.fetchall()
        for x in res:
            print(x)
def PurchaseProduct():
    mn=""
    dy=""
    now=datetime.datetime.now()
    purchaseID="P"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    L=[]
    Lst=[]
    L.append(purchaseID)
    itemId=input("Enter Product ID : ")
    L.append(itemId)
    itemNo=int(input("Enter the number of Items : "))
    L.append(itemNo)
    sql="select rate from product where product_id=%s"
    pid=(itemId,)
    mycursor.execute(sql,pid)
    res=mycursor.fetchone()
    for x in res:
        print("rate is : ", x)
        amount=x*itemNo
        print("Amount is :", amount)
        L.append(amount)
        mnth=now.month
        #print(datetime.date.today())
        dt1=datetime.date.today()
        L.append(dt1)
        tp=(L)
        sql="insert into purchase(purchase_id,item_id,no_of_items,amount,Purchase_date)values(%s,%s,%s,%s,%s)"
                       
        mycursor.execute(sql,tp)
        mydb.commit()
        sql="Select Instock from stock where item_id=%s"
        mycursor.execute(sql,pid)
        res=mycursor.fetchall()
        status="No"
        for x in res:
            print(x)
            instock=x[0]+itemNo
            if instock>0:
                status="Yes"
                Lst.append(instock)
                Lst.append(status)
                Lst.append(itemId)
                tp=(Lst)
                sql="update stock set instock=%s,status=%s where item_id=%s"
                mycursor.execute(sql,tp)
                mydb.commit()
                print("1 Item purchased and saved in Database")
        
##        if mnth<=9:
##            mn="0"+str(mnth)
##        else:
##            mn=str(mnth)
##            day=now.day
##            print(day)
##            if day<=9:
##                dy="0"+str(day)
##            else:
##               dy=str(day)
##               dt=str(now.year)+"-"+mn+"-"+dy
##               dt1=datetime.date.today()
##               L.append(dt1)
##               tp=(L)
##               sql="insert into purchase(purchase_id,item_id,no_of_items,amount,Purchase_date)values(%s,%s,%s,%s,%s)"
##               #sql="insert into purchase(purchase_id,item_id,no_of_items,amount)values(%s,%s,%s,%s)"
##               print(sql)
##               mycursor.execute(sql,tp)
##               mydb.commit()
##               sql="Select Instock from stock where item_id=%s"
##               mycursor.execute(sql,pid)
##               res=mycursor.fetchall()
##               status="No"
##               for x in res:
##                   print(x)
##                   instock=x[0]+itemNo
##
##                   if instock>0:
##                       status="Yes"
##                       Lst.append(instock)
##
##                       Lst.append(status)
##
##                       Lst.append(itemId)
##
##                       tp=(Lst)
##                       sql="update stock set instock=%s,status=%s where item_id=%s"
##                       mycursor.execute(sql,tp)
##                       mydb.commit()
##                       print("1 Item purchased and saved in Database")
def ViewPurchase():
    item=input("Enter Product Name : ")
    sql="select product.product_id, product.PName,product.brand,purchase.no_of_items,purchase.purchase_date,purchase.amount from product INNER JOIN purchase ON product.product_id=purchase.item_id and product.PName=%s"
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def ViewStock():
    item=input("Enter Product Name : ")
    sql="select product.product_id,product.PName,stock.Instock,\
    stock.status from stock, product where \
    product.product_id=stock.item_id and product.PName=%s"
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def SaleProduct():
    now=datetime.datetime.now()
    saleID="S"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    L=[]
    L.append(saleID)
    itemId=input("Enter Product ID : ")
    L.append(itemId)
    itemNo=int(input("Enter the number of Items : "))
    L.append(itemNo)
    sql="select rate from product where product_id=%s"
    pid=(itemId,)
    mycursor.execute(sql,pid)
    res=mycursor.fetchall()
    for x in res:
        print("The rate of item is :",x)
        dis=int(input("Enter the discount : "))
        saleRate=x[0]-(x[0]*dis/100)
        L.append(saleRate)
        amount=itemNo*saleRate
        #print(amount)
        L.append(amount)
##        mnth=now.month
##        if mnth<=9:
##            mn="0"+str(mnth)
##        else:
##            mn=str(mnth)
##            day=now.day
##            print(day)
##            if day<=9:
##                dy="0"+str(day)
##            else:
##               dy=str(day)
##               dt=str(now.year)+"-"+mn+"-"+dy
        dt=datetime.date.today()
        L.append(dt)
        tp=(L)
        
        sql="insert into sales(sale_id,item_id,no_of_item_sold,sale_rate,amount,date_of_sale) values(%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql,tp)
        mydb.commit()
        sql="Select Instock from stock where item_id=%s"
        mycursor.execute(sql,pid)
        res=mycursor.fetchall()
        for x in res:
            print("Total Items in Stock are : ",x)
            instock=x[0]-itemNo
            if instock>0:
                status="Yes"
                tp=(instock,status,itemId)
                sql="update stock set instock=%s,status=%s where item_id=%s"
                print("Remaining Items in Stock are : ",instock)
                mycursor.execute(sql,tp)
                mydb.commit()
def ViewSales():
    item=input("Enter Product Name : ")
    sql="select product.product_id, product.PName,product.brand,sales.no_of_item_sold,sales.date_of_sale,sales.amount \
     from sales, product where product.product_id=sales.item_id and product.PName=%s"
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def MenuSet():
    #Function For The SFashion Store System
    print("Enter 1 : To Add Product ")
    print("Enter 2 : To Edit Product ")
    print("Enter 3 : To Delete Product ")
    print("Enter 4 : To View Product ")
    print("Enter 5 : To Purchase Product")
    print("Enter 6 : To View Purchases")
    print("Enter 7 : To View Stock Detials")
    print("Enter 8 : To Sale the item")
    print("Enter 9 : To View Sales Detials")
    print("Enter 10 : Exit")
    
    try:
       #Using Exceptions For Validation
       userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
       exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") #Print New Line
    if(userInput == 1):
        AddProduct()
    elif(userInput == 2):
        EditProduct()
    elif (userInput==3):
       DelProduct()
    elif(userInput==4):
       ViewProduct()
    elif(userInput==5):
        PurchaseProduct()
    elif(userInput==6):
        ViewPurchase()
    elif(userInput==7):
        ViewStock()
    elif(userInput==8):
        SaleProduct()
    elif(userInput==9):
        ViewSales()
    elif(userInput==10):
        runAgain()
    else:
        print("Enter correct choice. . . ")
        print("*"*80)
        print("* * * * * * * Welcome to the Project of Fashion Store * * * * * * * ")
        print("*"*80)
        print("")
        MenuSet()
def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
    print("good Bye")
    quit()
MenuSet()
runAgain()


#runAgn = input("\nwant To Run Again Y/n: ")
#runAgain()
