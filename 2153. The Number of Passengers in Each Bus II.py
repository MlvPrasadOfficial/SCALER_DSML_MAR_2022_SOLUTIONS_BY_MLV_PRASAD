2153. The Number of Passengers in Each Bus II
Hard

32

15

Add to List

Share
SQL Schema
Table: Buses

+--------------+------+
| Column Name  | Type |
+--------------+------+
| bus_id       | int  |
| arrival_time | int  |
| capacity     | int  |
+--------------+------+
bus_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a bus at the LeetCode station and its capacity (the number of empty seats it has).
No two buses will arrive at the same time and all bus capacities will be positive integers.
 

Table: Passengers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| passenger_id | int  |
| arrival_time | int  |
+--------------+------+
passenger_id is the primary key column for this table.
Each row of this table contains information about the arrival time of a passenger at the LeetCode station.
 

Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at a time tbus and a passenger arrived at a time tpassenger where tpassenger <= tbus and the passenger did not catch any bus, the passenger will use that bus. In addition, each bus has a capacity. If at the moment the bus arrives at the station there are more passengers waiting than its capacity capacity, only capacity passengers will use the bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.

The query result format is in the following example.

 

Example 1:

Input: 
Buses table:
+--------+--------------+----------+
| bus_id | arrival_time | capacity |
+--------+--------------+----------+
| 1      | 2            | 1        |
| 2      | 4            | 10       |
| 3      | 7            | 2        |
+--------+--------------+----------+
Passengers table:
+--------------+--------------+
| passenger_id | arrival_time |
+--------------+--------------+
| 11           | 1            |
| 12           | 1            |
| 13           | 5            |
| 14           | 6            |
| 15           | 7            |
+--------------+--------------+
Output: 
+--------+----------------+
| bus_id | passengers_cnt |
+--------+----------------+
| 1      | 1              |
| 2      | 1              |
| 3      | 2              |
+--------+----------------+
Explanation: 
- Passenger 11 arrives at time 1.
- Passenger 12 arrives at time 1.
- Bus 1 arrives at time 2 and collects passenger 11 as it has one empty seat.

- Bus 2 arrives at time 4 and collects passenger 12 as it has ten empty seats.

- Passenger 12 arrives at time 5.
- Passenger 13 arrives at time 6.
- Passenger 14 arrives at time 7.
- Bus 3 arrives at time 7 and collects passengers 12 and 13 as it has two empty seats.









/* Write your T-SQL query statement below */
with a as (
  -- count total number of passenger for each bus and create a link between
  -- each bus and the next based on arrival time
  select
    ntot = count(passenger_id),
    B.arrival_time,
    B.bus_id,
    B.capacity,
    next_bus_id = lead(B.bus_id, 1, 0) over (order by B.arrival_time),
    bus_order = rank() over (order by b.arrival_time)
  from Passengers
    right join Buses B on Passengers.arrival_time <= B.arrival_time
  group by B.arrival_time, B.bus_id, b.capacity
), b as (
  -- calculate number of new passengers as ntot[i] - ntot[i-1]
  select a.*,
    new = ntot - lag(ntot, 1, 0) over(order by arrival_time)
  from a
), prev as (
  -- Anchor statement (initial result stored in 'prev')
  select
    bus_id,
    next_bus_id,
    new,
    passengers_cnt = iif(capacity >= new, new, capacity),
    remains = iif(capacity >= new, 0, new-capacity)
  from b
  where bus_order = 1
    union all
  -- Recursive statement (refers to previous result in 'prev')
  -- Executes until the result set is empty (no more next buses)
  select
    b.bus_id,
    b.next_bus_id,
    b.new,
    passengers_cnt = iif(b.capacity >= b.new+prev.remains, b.new+prev.remains, b.capacity),
    remains = iif(b.capacity >= b.new+prev.remains, 0, b.new+prev.remains-b.capacity)
  from b
  inner join prev on b.bus_id = prev.next_bus_id
)
select bus_id, passengers_cnt
from prev
order by bus_id asc;









