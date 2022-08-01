#!/usr/bin/env python
# coding: utf-8

# In[132]:


import pyodbc 
import matplotlib.pyplot as plt 
from datetime import datetime

connection = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-I3MDHVE;''Database=FSMS;''Trusted_Connection = yes;')

cursor = connection.cursor()

class select_stem():
    #this is a helper method for create_bouquet
    def __init__(self, flower_name, quantity):
        self.flower_name = flower_name 
        self.quantity = int(quantity)
    
    def get_stem(self):
        query = "SELECT Name, Price, Quantity FROM Stems"
        
        cursor.execute(query)

        result = cursor.fetchall()
        
        for i in result:
            if i[0] == self.flower_name:
                return i[0]
            
    def update_quantity(self):
        query = "UPDATE Stems                 SET Quantity = Quantity - ?                 WHERE Name = ?"
        
        count = cursor.execute(query, self.quantity, self.flower_name).rowcount
        cursor.commit()
        
        print('Rows updated: ' + str(count))
        
        query = "SELECT Name, Price, Quantity FROM Stems"
        
        cursor.execute(query)

        result = cursor.fetchall()
        
        for i in result:
            if i[0] == self.flower_name:
                return i[2]
            
class purchase_packaging():
    def __init__(self, package_code, units_used):
        self.package_code = int(package_code) 
        self.units_used = int(units_used)
        
    def purchase(self):
        query = "UPDATE Packaging                 SET units = units - ?                 WHERE package_code = ?"
        
        count = cursor.execute(query, self.units_used, self.package_code).rowcount
        cursor.commit()
        
        print('Rows updated: ' + str(count))
        
class create_bouquet():
    def __init__(self):
        self.container = {} #dictionary that contains the flowers and quantities that make up this bouquet
    
    def add_stems(self, flower_name, quantity):
        obj = select_stem(flower_name, quantity) #using composition here
        temp = obj.get_stem()
        obj.update_quantity() 
        temp2 = quantity
        self.container[temp] = temp2 
        
        return self.container
    
class purchase_bouquet(create_bouquet):
    def __init__(self, bouquet_obj): #using both inheritance and aggregation here
        super().__init__() #calling the constructor of the superclass
        self.bouquet_obj = bouquet_obj
        self.total = 0
    
    def get_price(self):
        #uses the values in dictionary to get the total price
        query = "SELECT ?, Price FROM Stems WHERE Name = ?"
        
        for i, j in self.bouquet_obj.container.items():
            cursor.execute(query, i, i)
            result = cursor.fetchone()
            self.total += j * result[1]
        
        return self.total 
    
    def insert_customer_record(self, name, address, contact):
    
        query = "INSERT INTO Customers(Name, Address, Contact) VALUES (?,?,?)"


        count = cursor.execute(query, name, address, contact).rowcount #using rowcount to identify the number of rows inserted
        cursor.commit()
        
        query = "SELECT Cust_ID FROM Customers WHERE Name = ?"
        
        cursor.execute(query, name)
        
        result = cursor.fetchall()
        
        global cust_id 
        cust_id = result[-1][0]
        
        print('Rows inserted: ' + str(count))
        
    def insert_order_record(self):
        #cust_id used here is of latest customer
        query = "INSERT INTO Orders(Order_datetime, Order_details, Total_Cost, Cust_ID) VALUES (?,?,?,?)"
        
        
        res = ""
        for i, j in self.bouquet_obj.container.items():
            res = res + str(i) + "  x" + str(j) + " "
            
        order_datetime = datetime.now()
        
        count = cursor.execute(query, order_datetime, res, self.total, cust_id).rowcount
        cursor.commit()
        
        print('Rows inserted: ' + str(count))
        
    def generate_invoice(self):
        #Takes in cust_id and returns order details as (cust_name, order_id, order_date, order_details, total_cost)

        query = "SELECT Customers.Name, Orders.Order_ID, Orders.Order_datetime, Orders.Order_details, Orders.Total_Cost FROM Customers INNER JOIN Orders ON Customers.Cust_ID = Orders.Cust_ID WHERE Orders.Cust_ID = ?"

        cursor.execute(query, cust_id)

        result = cursor.fetchall()
        return result[-1] #getting the latest order
        
class access_database():
    def __init__(self):
        pass
    
    def get_customer_record(self, name):
        #takes in customer name as parameter
        query = "SELECT * FROM Customers WHERE Name= ?" 

        cursor.execute(query, name)

        result = cursor.fetchone()
        return result
    
    def get_employee_record(self, ID):
        #takes in employee_ID as parameter
        query = "SELECT * FROM Employees WHERE Employee_ID= ?" 

        cursor.execute(query, ID)

        result = cursor.fetchone()
        return result
    
    def get_employee_hours(self, ID, Month):
        #takes in employee_ID and month as parameters as (employee_ID, employee_name, month, hours)
        query = "SELECT Hours_Worked.Employee_ID, Employees.Employee_name, Hours_Worked.Month, Hours_Worked.Hours FROM Hours_Worked, Employees WHERE Hours_Worked.Employee_ID = ? AND Hours_Worked.Month = ? AND Employees.Employee_ID = ?" 

        cursor.execute(query, ID, Month, ID)

        result = cursor.fetchone()
        return result
    
    def get_stems(self):
        #returns all the stems stored in the database as (stem_name, stem_price, stem_quantity)

        cursor.execute("SELECT Name, Price, Quantity FROM Stems")

        result = cursor.fetchall()
        return result
    
    def generate_notification(self):
        #generates notification whenever the stock for a particular flower < 60 stems 
        query = "SELECT * FROM Stems WHERE Quantity < 60"
    
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        for i in result: 
            return 'The stock for ' + i[0] + ' is running low!'
    
class login():
    def __init__(self, login_id, password):
        self.login_id = login_id
        self.password = password
        
    def validate(self):
        cursor.execute("SELECT login_id, password FROM Login_Credentials")
    
        result = cursor.fetchall()

        flag = None

        for i in result:
            if self.login_id == i[0] and self.password == i[1]:
                flag = True
                return flag
            else:
                continue

        if not flag:
            return False
        
class visualize_data():
    def __init__(self, month):
        self.month = month
        
    def barchart(self):
        #displays the number of monthly working hours of each employee in the form of a bar graph
        query = "SELECT Employees.Employee_name, Hours_worked.Employee_ID, Hours_Worked.Hours FROM Employees INNER JOIN Hours_Worked ON Employees.Employee_ID = Hours_Worked.Employee_ID WHERE Hours_Worked.Month = ?"
    
        cursor.execute(query, self.month)

        result = cursor.fetchall()

        employee_names = []
        hours_worked = []

        for i in result: 
            employee_names.append(i[0])
            hours_worked.append(i[2])

        plt.bar(employee_names, hours_worked)
        plt.title('Employee monthly working hours')
        plt.xlabel('Employee name')
        plt.ylabel('Hours worked')
        plt.show()
    
class manage_inventory():
    def __init__(self):
        pass
    
    def add_stock(self, flower_name, amount):
        
        query = "UPDATE STEMS SET                 Quantity = Quantity + ?                WHERE Name = ?"
        
        count = cursor.execute(query, amount, flower_name).rowcount
        cursor.commit()
        
        print('Rows updated: ' + str(count))

    
if __name__ == '__main__':
    
    
#     package_obj = purchase_packaging(200, 1)
#     package_obj.purchase()
         
#     stem_obj = select_stem('Rose', 5)
#     x = stem_obj.get_stem()
#     y = stem_obj.update_quantity()
#     print(x)
#     print(y)
    
#     bouquet_obj = create_bouquet()
#     bouquet_obj.add_stems('Rose', 5)
#     z = bouquet_obj.add_stems('Tulip', 10)
#     print(z)

#     purchase_bouquet_obj = purchase_bouquet(bouquet_obj)
#     var = purchase_bouquet_obj.get_price()
#     print(var)
#     purchase_bouquet_obj.insert_customer_record('Michael Myers', 'Commotion St. Windenburg, Germany', 51561568)
#     purchase_bouquet_obj.insert_order_record()
#     invoice = purchase_bouquet_obj.generate_invoice()
#     print(invoice)

#     database_obj = access_database()
#     var1 = database_obj.get_customer_record('Major Maverick')
#     print(var1)
#     var2 = database_obj.get_employee_record(100)
#     print(var2)
#     var3 = database_obj.get_employee_hours(101, 'January')
#     print(var3)
#     var4 = database_obj.get_stems()
#     print(var4)
#     var5 = database_obj.generate_notification()
#     print(var5)

#     login_obj = login('isaac@blossoms.flowers', 'isaaclikestodance')
#     var6 = login_obj.validate()
#     print(var6)

#     visualize_obj = visualize_data('January')
#     visualize_obj.barchart()

#     inventory_obj = manage_inventory()
#     inventory_obj.add_stock('Carnation', 50)
    


# In[95]:


alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

res  = ""

for i, j in alien_0.items():
    res = res + str(i) + str(j)
    res 
    
print(res)


# In[ ]:




