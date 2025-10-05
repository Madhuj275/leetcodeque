# Write your MySQL query statement below
select p.product_id,COALESCE(ROUND(SUM(u.units * p.price) / NULLIF(SUM(u.units), 0), 2), 0) as average_price
From Prices p
LEFT JOIN UnitsSold u on u.product_id=p.product_id
AND u.purchase_date >= p.start_date
AND u.purchase_date <= p.end_date
group by p.product_id;