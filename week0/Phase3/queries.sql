 --Business Pipeline Exercises

----------------- 1. Read sales data -> clean nulls -> calculate daily sales


CREATE TABLE customers (
2
    customer_id INT,
3
    first_name VARCHAR(100),
4
    last_name VARCHAR(100),
5
    email VARCHAR(150),
6
    phone_number VARCHAR(20),
7
    address VARCHAR(200),
8
    city VARCHAR(100),
9
    state VARCHAR(50),
10
    zip_code VARCHAR(20)
11
);
12
​
13
CREATE TABLE sales (
14
    sale_id INT,
15
    customer_id INT,
16
    product_id INT,
17
    sale_date DATE,
18
    quantity INT,
19
    total_amount DOUBLE
20
);
21
​
22
​
23
INSERT INTO customers VALUES
24
(1,'John','Smith','john.smith@domain.com','555-0001','123 Elm St','Springfield','IL','62701'),
25
(2,'Emma','Jones','emma.jones@webmail.com','555-0002','456 Oak St','Centerville','OH','45459'),
26
(3,'Olivia','Brown','olivia.brown@outlook.com','555-0003','789 Pine St','Greenville','SC','29601'),
27
(4,'Liam','Johnson','liam.johnson@mail.com','555-0004','321 Maple St','Austin','TX','73301'),
28
(5,'Noah','Williams','noah.williams@mail.com','555-0005','654 Cedar St','Dallas','TX','75001');
29
​
30
​
31
INSERT INTO sales VALUES
32
(1,1,101,'2024-01-15',2,39.98),
33
(2,1,102,'2024-01-20',1,29.99),
34
(3,2,103,'2024-01-16',1,25.00),
35
(4,2,104,'2024-01-22',3,89.97),
36
(5,3,105,'2024-01-17',2,49.98),
37
(6,1,106,'2024-01-25',1,19.99),
38
(7,4,107,'2024-01-18',2,59.98),
39
(8,5,108,'2024-01-19',1,15.00),
40
(9,5,109,'2024-01-21',2,30.00),
41
(10,5,110,'2024-01-23',1,20.00);

SELECT sale_date, ROUND(SUM(total_amount),2) AS daily_sales
FROM sales
WHERE total_amount IS NOT NULL
GROUP BY sale_date;

----------------- 2. Read customer data -> clean invalid rows -> city-wise revenue



----------------- 3. Find repeat customers (>2 orders)

----------------- 4. Find highest spending customer in each city

----------------- 5.. Build final reporting table with customer, city, total spend, order count
