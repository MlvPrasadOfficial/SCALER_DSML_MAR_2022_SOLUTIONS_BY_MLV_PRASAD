1821. Find Customers With Positive Revenue this Year
Easy

28

18

Add to List

Share
SQL Schema
Table: Customers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| customer_id  | int  |
| year         | int  |
| revenue      | int  |
+--------------+------+
(customer_id, year) is the primary key for this table.
This table contains the customer ID and the revenue of customers in different years.
Note that this revenue can be negative.
 

Write an SQL query to report the customers with postive revenue in the year 2021.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Customers table:
+-------------+------+---------+
| customer_id | year | revenue |
+-------------+------+---------+
| 1           | 2018 | 50      |
| 1           | 2021 | 30      |
| 1           | 2020 | 70      |
| 2           | 2021 | -50     |
| 3           | 2018 | 10      |
| 3           | 2016 | 50      |
| 4           | 2021 | 20      |
+-------------+------+---------+
Output: 
+-------------+
| customer_id |
+-------------+
| 1           |
| 4           |
+-------------+
Explanation: 
Customer 1 has revenue equal to 30 in the year 2021.
Customer 2 has revenue equal to -50 in the year 2021.
Customer 3 has no revenue in the year 2021.
Customer 4 has revenue equal to 20 in the year 2021.
Thus only customers 1 and 4 have positive revenue in the year 2021.








/* Write your T-SQL query statement below */
select customer_id
from Customers
where year = '2021' and revenue > 0






