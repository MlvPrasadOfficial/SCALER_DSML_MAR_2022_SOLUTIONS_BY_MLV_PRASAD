2173. Longest Winning Streak
Hard

52

2

Add to List

Share
SQL Schema
Table: Matches

+-------------+------+
| Column Name | Type |
+-------------+------+
| player_id   | int  |
| match_day   | date |
| result      | enum |
+-------------+------+
(player_id, match_day) is the primary key for this table.
Each row of this table contains the ID of a player, the day of the match they played, and the result of that match.
The result column is an ENUM type of ('Win', 'Draw', 'Lose').
 

The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.

Write an SQL query to count the longest winning streak for each player.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Matches table:
+-----------+------------+--------+
| player_id | match_day  | result |
+-----------+------------+--------+
| 1         | 2022-01-17 | Win    |
| 1         | 2022-01-18 | Win    |
| 1         | 2022-01-25 | Win    |
| 1         | 2022-01-31 | Draw   |
| 1         | 2022-02-08 | Win    |
| 2         | 2022-02-06 | Lose   |
| 2         | 2022-02-08 | Lose   |
| 3         | 2022-03-30 | Win    |
+-----------+------------+--------+
Output: 
+-----------+----------------+
| player_id | longest_streak |
+-----------+----------------+
| 1         | 3              |
| 2         | 0              |
| 3         | 1              |
+-----------+----------------+
Explanation: 
Player 1:
From 2022-01-17 to 2022-01-25, player 1 won 3 consecutive matches.
On 2022-01-31, player 1 had a draw.
On 2022-02-08, player 1 won a match.
The longest winning streak was 3 matches.

Player 2:
From 2022-02-06 to 2022-02-08, player 2 lost 2 consecutive matches.
The longest winning streak was 0 matches.

Player 3:
On 2022-03-30, player 3 won a match.
The longest winning streak was 1 match.
 

Follow up: If we are interested in calculating the longest streak without losing (i.e., win or draw), how will your solution change?











/* Write your T-SQL query statement below */
with greatTable AS (
select m1.player_id,m1.match_day,m1.result
,(select count(*) from matches m2 
where m2.result='Win' and m2.player_id = m1.player_id and m1.result='Win'
		and m2.match_day between
		ISNULL(
		(select max(m3.match_day) from matches m3 where m3.player_id = m1.player_id and 
		m3.match_day<=m1.match_day and m3.result!='Win'),'1100-1-1')
	
	and m1.match_day
	)
AS win_count
from  matches m1)
select player_id,max(win_count) longest_streak  from greatTable group by player_id;
















