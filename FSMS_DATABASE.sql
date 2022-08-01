/*
CREATE TABLE Stems
(
Name varchar(255) PRIMARY KEY,
Price float, 
Quantity int,
Image varbinary(MAX)
) 
*/

/*
INSERT INTO Stems(Name, Price, Quantity, Image)

SELECT 'Rose', 2.0, 200, BulkColumn FROM openrowset
(Bulk 'C:\Users\hp\Desktop\rose.jpg', SINGLE_BLOB) as image



INSERT INTO Stems(Name, Price, Quantity, Image)

SELECT 'Tulip', 3.0, 200, BulkColumn FROM openrowset
(Bulk 'C:\Users\hp\Desktop\tulip.jpg', SINGLE_BLOB) as image



INSERT INTO Stems(Name, Price, Quantity, Image)

SELECT 'Hydrangea', 3.0, 200, BulkColumn FROM openrowset
(Bulk 'C:\Users\hp\Desktop\hydrangea.jpg', SINGLE_BLOB) as image



INSERT INTO Stems(Name, Price, Quantity, Image)

SELECT 'Sunflower', 5.0, 200, BulkColumn FROM openrowset
(Bulk 'C:\Users\hp\Desktop\sunflower.jpg', SINGLE_BLOB) as image



INSERT INTO Stems(Name, Price, Quantity, Image)

SELECT 'Carnation', 2.5, 200, BulkColumn FROM openrowset
(Bulk 'C:\Users\hp\Desktop\carnation.jpg', SINGLE_BLOB) as image
*/

--SELECT * FROM Stems

/*
CREATE TABLE Customers
(
Cust_ID int PRIMARY KEY IDENTITY(1,1), 
Name varchar(255), 
Address varchar(255), 
Contact varchar(255)
) 
*/

/*
INSERT INTO Customers
VALUES ('Jack Soloff', 'House no. 14, Mulberry St. London', '486486468'),
		('Crimson Countess', 'Swan Road, Cherry St. Kansas City', '181866186'),
		('Graham Norton', 'Dexter County, Pheonix Building, Apartment 4', '2515135'), 
		('Major Maverick', 'Air Base 1, Holiday Resort, Room 20', '8344541531')
*/

--SELECT * FROM Customers

/*
CREATE TABLE Orders
(
Order_ID int PRIMARY KEY IDENTITY(1,1), 
Order_datetime datetime, --YYYY-MM-DD
Order_details varchar(255),
Total_Cost float,
Cust_ID int,
FOREIGN KEY(Cust_ID) REFERENCES Customers(Cust_ID)
) 

INSERT INTO Orders
VALUES (SYSDATETIME(), 'Bouquet contains x10 Carnations, x5 Roses, x2 Hydrangeas', 25.2, 4),
		(SYSDATETIME(), 'Bouquet contains x2 Roses, x5 Tulips, x3 Sunflowers', 14.3, 2),
		(SYSDATETIME(), 'Bouquet contains x1 Rose, x1 Carnation, x1 Tulip', 9, 2)
*/

--SELECT * FROM Orders

/*
CREATE TABLE Employees
(
Employee_ID int PRIMARY KEY IDENTITY(100, 1),
Employee_name varchar(255),
Address varchar(255),
Designation varchar(255)
)
*/

/*
INSERT INTO Employees 
VALUES ('Eugene Thacter', 'House no. 255, Gulberg III, Lahore', 'Business Operations Manager'),
		('Isaac Gardener', 'House no. 124, Cantt, Lahore', 'Supply Chain Manager'),
		('Ali Haider', 'House no. 174, DHA, Lahore', 'Cashier')
*/

--SELECT * FROM Employees

/*
CREATE TABLE Hours_Worked 
(
Employee_ID int, 
Month varchar(255),
Hours int
FOREIGN KEY(Employee_ID) REFERENCES Employees(Employee_ID)
)



INSERT INTO Hours_Worked
VALUES (100, 'January', 65),
		(101, 'January', 54),
		(102, 'January', 25)
*/

--SELECT * FROM Hours_Worked

/*
SELECT Hours_Worked.Employee_ID, Employees.Employee_name, Hours_Worked.Month, Hours_Worked.Hours
FROM Hours_Worked, Employees
WHERE Hours_Worked.Employee_ID = 101 AND Hours_Worked.Month = 'January' AND Employees.Employee_ID = 101
*/

/*
CREATE TABLE Login_Credentials 
(
employee_ID int,
login_id varchar(255), 
password varchar(255)
FOREIGN KEY(Employee_ID) REFERENCES Employees(Employee_ID)
)
*/

/*
INSERT INTO Login_Credentials
VALUES (100, 'eugene@blossoms.flowers', 'eugene123'),
		(101, 'isaac@blossoms.flowers', 'isaaclikestodance'),
		(102, 'alih@blossoms.flowers', 'coffeelover453')
*/

/*
SELECT Employees.Employee_name, Hours_worked.Employee_ID, Hours_Worked.Hours
FROM Employees
INNER JOIN Hours_Worked 
ON Employees.Employee_ID = Hours_Worked.Employee_ID WHERE Hours_Worked.Month = 'January'
*/

/*
SELECT Customers.Name, Orders.Order_ID, Orders.Order_date, Orders.Order_details, Orders.Total_Cost
FROM Customers
INNER JOIN Orders
ON Customers.Cust_ID = Orders.Cust_ID WHERE Orders.Cust_ID = 2
*/

/*
CREATE TABLE Packaging
(
package_code int PRIMARY KEY IDENTITY(200,1),
type varchar(255),
cost float,
units int
)



INSERT INTO Packaging
VALUES ('Cellophane', 2.5, 50),
		('Ribbons', 1.0, 200),
		('Paper', 0.5, 300)
*/

/*
INSERT INTO Stems (Name, Price, Quantity)
VALUES ('Orchids', 4, 55)
*/

SELECT * FROM Stems

