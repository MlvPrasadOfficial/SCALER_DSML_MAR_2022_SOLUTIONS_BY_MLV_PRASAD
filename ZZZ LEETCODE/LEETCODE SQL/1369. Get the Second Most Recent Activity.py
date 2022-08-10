1369. Get the Second Most Recent Activity
Hard

120

11

Add to List

Share
SQL Schema
Table: UserActivity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| username      | varchar |
| activity      | varchar |
| startDate     | Date    |
| endDate       | Date    |
+---------------+---------+
There is no primary key for this table. It may contain duplicates.
This table contains information about the activity performed by each user in a period of time.
A person with username performed an activity from startDate to endDate.
 

Write an SQL query to show the second most recent activity of each user.

If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
UserActivity table:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Travel       | 2020-02-12  | 2020-02-20  |
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Alice      | Travel       | 2020-02-24  | 2020-02-28  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
Output: 
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
Explanation: 
The most recent activity of Alice is Travel from 2020-02-24 to 2020-02-28, before that she was dancing from 2020-02-21 to 2020-02-23.
Bob only has one record, we just take that one.









/* Write your T-SQL query statement below */
SELECT  username, 
        activity, 
        startDate, 
        endDate 
 FROM 
(select  username,
         activity, 
         startDate, 
         endDate, 
         row_number() over (partition by username order by startDate desc) rn, 
         row_number() over (partition by username order by startDate ) rn2 
  FROM UserActivity 
    ) AS sub 
    where (rn = 1 and rn2 =1 ) or rn = 2
