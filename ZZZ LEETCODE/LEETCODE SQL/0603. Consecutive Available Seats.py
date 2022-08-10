603. Consecutive Available Seats
Easy

510

48

Add to List

Share
SQL Schema
Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment primary key column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
 

Write an SQL query to report all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.

The query result format is in the following example.

 

Example 1:

Input: 
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
Output: 
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+










with cte as (select seat_id, case when lag(free) over( order by seat_id) = 1 
                          and lag(free) over( order by seat_id) = free
                          then 0 else 1 end as flag
                          from cinema
)

,accumulated_sum as (
select seat_id, sum(flag) over (order by seat_id) as same_free from cte
)

select seat_id from accumulated_sum
where same_free in (select 
same_free from accumulated_sum
group by same_free
having count(*) > 1)