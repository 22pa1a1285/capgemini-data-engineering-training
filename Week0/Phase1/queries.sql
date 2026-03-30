
--created customers table
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    age INT
);

--inserted values into customers table
INSERT INTO customers (customer_id, customer_name, city, age) VALUES
(1, 'Ravi', 'Hyderabad', 25),
(2, 'Sita', 'Chennai', 32),
(3, 'Arun', 'Hyderabad', 28),
(4, 'Meena', 'Bengaluru', 35),
(5, 'Kiran', 'Chennai', 22);

---- 1. Show all customers

SELECT * from customers;

----- 2.Show customers from Chennai

SELECT * from customers WHERE city = "hyderabad";

---- 3. Show customers with age > 25

SELECT * from customers WHERE age > 25;

---- 4.  Show only customer_name and city

SELECT customer_name,city from customers;

---- 5 . Count customers city-wise

SELECT city,count(*) As total_count from customers GROUP BY city; 



