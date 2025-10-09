# Write your MySQL query statement below
Select query_name,
ROUND(AVG(rating/position),2) as quality,
ROUND(
    sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2
) as poor_query_percentage
FROM Queries
Group by query_name;