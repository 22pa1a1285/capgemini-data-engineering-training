
-- Day3 Window Functions

drop table employees;

CREATE TABLE employees (
emp_id INT,
emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
join_date DATE
);

INSERT INTO employees VALUES
(1, 'Amit', 'Chennai', 2000, '2023-01-01'),
(2, 'Ravi', 'Hyderabad', 1500, '2023-01-02'),
(3, 'Sneha', 'Chennai', 3000, '2023-01-03'),
(4, 'Kiran', 'Bangalore', 2500, '2023-01-04'),
(5, 'Priya', 'Chennai', 2000, '2023-01-05'),
(6, 'Arjun', 'Hyderabad', 1800, '2023-01-06'),
(7, 'Neha', 'Bangalore', 2200, '2023-01-07'),
(8, 'Vikas', 'Chennai', 3000, '2023-01-08'),
(9, 'Anjali', 'Hyderabad', 1700, '2023-01-09'),
(10, 'Rahul', 'Bangalore', 2600, '2023-01-10'),
(11, 'Suresh', 'Chennai', 2800, '2023-01-11'),
(12, 'Pooja', 'Hyderabad', 1600, '2023-01-12'),
(13, 'Manoj', 'Bangalore', 2400, '2023-01-13'),
(14, 'Divya', 'Chennai', 2100, '2023-01-14'),
(15, 'Karthik', 'Hyderabad', 1900, '2023-01-15'),
(16, 'Meena', 'Bangalore', 2300, '2023-01-16'),
(17, 'Raj', 'Chennai', 2700, '2023-01-17'),
(18, 'Simran', 'Hyderabad', 2000, '2023-01-18'),
(19, 'Deepak', 'Bangalore', 2500, '2023-01-19'),
(20, 'Nisha', 'Chennai', 2600, '2023-01-20');

-- Row Number()
-- 1.	Assign a unique row number to all employees based on salary (highest first).

select *, row_number() over(order by salary desc) as row_number from employees;

-- 2.	Assign row numbers to employees within each department based on salary descending. 

select *, row_number() over(Partition by(department) order by salary desc) as rn from employees;

-- 3.	Assign row numbers based on employee joining date (latest first). 

select *,row_number() over(order by join_date desc) as latest_join from employees;

-- 4.	Assign row numbers within each department based on earliest joining date. 

select *,row_number() over(Partition by(department) order by join_date desc) as earliest_join from employees;

-- 5.	Assign row numbers to orders based on order date. 

-- 6.	Assign row numbers to orders within each city based on order amount (highest first). 
-- 7.	Assign row numbers to employees based on salary (lowest first). 
select *,row_number() over(order by salary) as emp_salary from employees;

-- 8.	Assign row numbers within department for employees based on name alphabetically. 
select *,row_number() over(partition by(department) order by emp_name) as employee_name from employees;

-- 🔹RANK() ONLY Questions
-- 9.	Rank all employees based on salary (highest first). 

select *,rank() over(order by salary desc) as highest_salary from employees;

-- 10.	Rank employees within each department based on salary. 

select *,rank() over(partition by(department) order by salary desc) as dept_salary from employee;

-- 11.	Rank employees based on joining date (latest gets rank 1). 


select *,rank() over(order by join_date) as earliest_join from employee;

-- 12.	Rank orders based on order amount (highest first). 

-- 13.	Rank orders within each city based on order amount. 

-- 14.	Rank employees within department based on salary (lowest first). 
select *,rank() over(order by salary) as dept_salary from employees;

-- 15.	Rank employees based on name alphabetically. 

select *,rank() over(order by emp_name) as name_alphabetically from employees;

-- 16.	Rank orders within each city based on order date. 





-- DENSE_RANK() ONLY Questions
-- 17.	Assign dense rank to employees based on salary (highest first). 
select *,dense_rank() over(order by salary desc) as higest_salary from employees;

-- 18.	Assign dense rank within each department based on salary. 
select *,dense_rank() over(partition by department order by salary desc) as ex from employees;

-- 19.	Assign dense rank to employees based on joining date. 
select *,dense_rank() over(order by join_date) as joining_date from employees;

-- 20.	Assign dense rank to orders based on order amount. 
select *,dense_rank() over(order by )

-- 21.	Assign dense rank within each city based on order amount. 

-- 22.	Assign dense rank to employees based on salary (lowest first). 
select *,dense_rank() over(order by salary) as lowest_salary from employees;

-- 23.	Assign dense rank within department based on joining date. 
select *,dense_rank() over(partition by(department) order by join_date) as dept_joining_date from employees;

-- 24.	Assign dense rank to orders based on order date.
