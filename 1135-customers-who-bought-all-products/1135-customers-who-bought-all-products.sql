# Write your MySQL query statement below
select customer_id from Customer
group by customer_id
having Count(distinct product_key)= (select COUNT(*) From Product);