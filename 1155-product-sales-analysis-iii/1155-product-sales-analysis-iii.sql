# Write your MySQL query statement below
Select product_id,year as first_year,quantity,price from sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year) 
    FROM sales
    GROUP BY product_id
);