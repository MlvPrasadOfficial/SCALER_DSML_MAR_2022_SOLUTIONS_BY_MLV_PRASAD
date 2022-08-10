618. Students Report By Geography
Hard

130

143

Add to List

Share
SQL Schema
Table: Student

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
+-------------+---------+
There is no primary key for this table. It may contain duplicate rows.
Each row of this table indicates the name of a student and the continent they came from.
 

A school has students from Asia, Europe, and America.

Write an SQL query to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.

The test cases are generated so that the student number from America is not less than either Asia or Europe.

The query result format is in the following example.

 

Example 1:

Input: 
Student table:
+--------+-----------+
| name   | continent |
+--------+-----------+
| Jane   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jack   | America   |
+--------+-----------+
Output: 
+---------+------+--------+
| America | Asia | Europe |
+---------+------+--------+
| Jack    | Xi   | Pascal |
| Jane    | null | null   |
+---------+------+--------+
 

Follow up: If it is unknown which continent has the most students, could you write a query to generate the student report?














/* Write your T-SQL query statement below */
with pivot_student as(
select name, continent, row_number() over(partition by continent order by name) as rnk from student
    )
select America, Asia, Europe from pivot_student
pivot(min(name) for continent in ([America], [Asia], [Europe] )) as my_pvt