CREATE DATABASE IF NOT EXISTS company;
USE company;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
); 

DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

INSERT INTO departments (dept_name, location) VALUES
('HR', 'Hyderabad'),
('Finance', 'Mumbai'),
('IT', 'Bangalore'),
('Marketing', 'Delhi'),
('R&D', 'Chennai');

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12'),
('Sonia', 'Verma', 'Finance', 70000, '2021-06-01');

SELECT * FROM employees;
SELECT first_name, last_name, department FROM employees;
SELECT DISTINCT department FROM employees;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees WHERE hire_date > '2020-12-31';
SELECT * FROM employees ORDER BY salary ASC;
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;
SELECT COUNT(*) AS total_employees FROM employees;



