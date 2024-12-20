-- Part 1: Database Design (SQL)
-- Schema Design: Design an SQL table to store employee information with the following fields:

-- employee_id (Primary Key, Auto Increment).
-- first_name (String, required).
-- last_name (String, required).
-- email (String, must be unique).
-- department (String, e.g., 'HR', 'Engineering', 'Marketing').
-- joining_date (Date, required).
-- salary (Decimal, required).
-- Write the SQL script to create this table.

create database if not exists arshil_test;
use arshil_test;

CREATE TABLE Employee (
    employee_id int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    department varchar(50) check(department in('HR', 'Engineering', 'Marketing')),
    joining_date date not null,
    salary decimal(10, 2) not null
);


show tables;
select * from employee;

