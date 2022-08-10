613. Shortest Distance in a Line
Easy

265

36

Add to List

Share
SQL Schema
Table: Point

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
 

Write an SQL query to report the shortest distance between any two points from the Point table.

The query result format is in the following example.

 

Example 1:

Input: 
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+
Output: 
+----------+
| shortest |
+----------+
| 1        |
+----------+
Explanation: The shortest distance is between points -1 and 0 which is |(-1) - 0| = 1.











SELECT MIN(ABS(f.x - s.x)) as shortest
FROM point f, point s
WHERE f.x != s.x