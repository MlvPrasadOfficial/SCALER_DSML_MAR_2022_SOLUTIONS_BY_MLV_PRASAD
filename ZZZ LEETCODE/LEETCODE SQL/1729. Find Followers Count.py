/* Write your T-SQL query statement below */
 SELECT USER_ID,
         COUNT(*) AS FOLLOWERS_COUNT
    FROM FOLLOWERS
GROUP BY USER_ID






