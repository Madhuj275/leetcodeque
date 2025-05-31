# Write your MySQL query statement below
select c.name as Customers From customers c
Left Join Orders o on o.customerId=c.id
where o.customerId is NULL;