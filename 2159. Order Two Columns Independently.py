2159. Order Two Columns Independently
Medium

27

13

Add to List

Share
SQL Schema
Table: Data

+-------------+------+
| Column Name | Type |
+-------------+------+
| first_col   | int  |
| second_col  | int  |
+-------------+------+
There is no primary key for this table and it may contain duplicates.
 

Write an SQL query to independently:

order first_col in ascending order.
order second_col in descending order.
The query result format is in the following example.

 

Example 1:

Input: 
Data table:
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 4         | 2          |
| 2         | 3          |
| 3         | 1          |
| 1         | 4          |
+-----------+------------+
Output: 
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 1         | 4          |
| 2         | 3          |
| 3         | 2          |
| 4         | 1          |
+-----------+------------+











/* Write your T-SQL query statement below */


SELECT A.first_col
     , B.second_col
  FROM (
        SELECT first_col
             , ROW_NUMBER() OVER (ORDER BY first_col) AS F
          FROM Data
  ) A
  JOIN (
        SELECT second_col
             , ROW_NUMBER() OVER (ORDER BY second_col DESC) AS S
          FROM Data
  ) B
    ON A.F = B.S
 ORDER BY A.F








