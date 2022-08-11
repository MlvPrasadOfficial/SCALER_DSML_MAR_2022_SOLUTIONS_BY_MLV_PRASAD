1972. First and Last Call On the Same Day
Hard

77

27

Add to List

Share
SQL Schema
Table: Calls

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key for this table.
Each row contains information about the time of a phone call between caller_id and recipient_id.
 

Write an SQL query to report the IDs of the users whose first and last calls on any day were with the same person. Calls are counted regardless of being the caller or the recipient.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Calls table:
+-----------+--------------+---------------------+
| caller_id | recipient_id | call_time           |
+-----------+--------------+---------------------+
| 8         | 4            | 2021-08-24 17:46:07 |
| 4         | 8            | 2021-08-24 19:57:13 |
| 5         | 1            | 2021-08-11 05:28:44 |
| 8         | 3            | 2021-08-17 04:04:15 |
| 11        | 3            | 2021-08-17 13:07:00 |
| 8         | 11           | 2021-08-17 22:22:22 |
+-----------+--------------+---------------------+
Output: 
+---------+
| user_id |
+---------+
| 1       |
| 4       |
| 5       |
| 8       |
+---------+
Explanation: 
On 2021-08-24, the first and last call of this day for user 8 was with user 4. User 8 should be included in the answer.
Similarly, user 4 on 2021-08-24 had their first and last call with user 8. User 4 should be included in the answer.
On 2021-08-11, user 1 and 5 had a call. This call was the only call for both of them on this day. Since this call is the first and last call of the day for both of them, they should both be included in the answer.










/* Write your T-SQL query statement below */
/* Write your T-SQL query statement below */

with a as (SELECT caller_id id1, recipient_id id2, call_time FROM Calls
UNION ALL
SELECT recipient_id id1, caller_id id2, call_time FROM Calls
           )
,first_last_call as (select id1, max(call_time) max_call, min(call_time) min_call from a 
            GROUP BY id1, format(call_time,'yyyy-MM-dd')
                    )
                    
   select distinct a.id1 as user_id
           from first_last_call c 
           join a on a.id1 = c.id1 and a.call_time in (max_call,min_call)
           group by a.id1, format(call_time,'yyyy-MM-dd')
           having max(id2) = min(id2)