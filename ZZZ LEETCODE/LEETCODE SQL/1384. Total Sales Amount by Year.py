1384. Total Sales Amount by Year
Hard

169

86

Add to List

Share
SQL Schema
Table: Product

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
+---------------+---------+
product_id is the primary key for this table.
product_name is the name of the product.
 

Table: Sales

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| product_id          | int     |
| period_start        | date    |
| period_end          | date    |
| average_daily_sales | int     |
+---------------------+---------+
product_id is the primary key for this table. 
period_start and period_end indicate the start and end date for the sales period, and both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.
The dates of the sales years are between 2018 to 2020.
 

Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

Return the result table ordered by product_id and report_year.

The query result format is in the following example.

 

Example 1:

Input: 
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | LC Phone     |
| 2          | LC T-Shirt   |
| 3          | LC Keychain  |
+------------+--------------+
Sales table:
+------------+--------------+-------------+---------------------+
| product_id | period_start | period_end  | average_daily_sales |
+------------+--------------+-------------+---------------------+
| 1          | 2019-01-25   | 2019-02-28  | 100                 |
| 2          | 2018-12-01   | 2020-01-01  | 10                  |
| 3          | 2019-12-01   | 2020-01-31  | 1                   |
+------------+--------------+-------------+---------------------+
Output: 
+------------+--------------+-------------+--------------+
| product_id | product_name | report_year | total_amount |
+------------+--------------+-------------+--------------+
| 1          | LC Phone     |    2019     | 3500         |
| 2          | LC T-Shirt   |    2018     | 310          |
| 2          | LC T-Shirt   |    2019     | 3650         |
| 2          | LC T-Shirt   |    2020     | 10           |
| 3          | LC Keychain  |    2019     | 31           |
| 3          | LC Keychain  |    2020     | 31           |
+------------+--------------+-------------+--------------+
Explanation: 
LC Phone was sold for the period of 2019-01-25 to 2019-02-28, and there are 35 days for this period. Total amount 35*100 = 3500. 
LC T-shirt was sold for the period of 2018-12-01 to 2020-01-01, and there are 31, 365, 1 days for years 2018, 2019 and 2020 respectively.
LC Keychain was sold for the period of 2019-12-01 to 2020-01-31, and there are 31, 31 days for years 2019 and 2020 respectively.




















-- Get the year range from the sales
with min_max_year as 
(
    select min(year(period_start)) min_year, max(year(period_end)) max_year
    from Sales
)

-- Generate all years using recursive CTE
, all_years as
(
    select top 1 min_year as year
    from min_max_year
    UNION ALL
    select year + 1 as year
    from all_years a
    join min_max_year b on a.year < b.max_year
)

-- Generate start and end dates for the years for calculating date difference
, years_with_dates as 
(
select year , try_cast('1-1-' + cast(year as varchar(4)) as date) start_date, dateadd(day, -1, dateadd(year, 1, try_cast('1-1-' + cast(year as varchar(4)) as date))) as end_date
from all_years
)

-- Cross join to get all years and dates
, sales_with_all_years as 
(
    select *
    from Sales s
    cross join years_with_dates y 
    where y.year >= year(s.period_start) and y.year <= year(s.period_end)
)

-- Calculate the datedifference and multiply by average_daily_sales to get the results
select s.product_id, p.product_name, cast(s.year as varchar(4)) as report_year
        , average_daily_sales * (datediff(day, case when period_start >= start_date then period_start else start_date end , case when period_end <= end_date then period_end else end_date end ) + 1) as total_amount
from sales_with_all_years s
join Product p on s.product_id = p.product_id
order by s.product_id, s.year
;