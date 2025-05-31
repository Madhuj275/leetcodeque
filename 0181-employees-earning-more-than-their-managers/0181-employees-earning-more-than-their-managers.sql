# Write your MySQL query statement below
Select e1.name as employee 
from employee e1
Join employee e2 on e1.managerId=e2.id
Where e1.salary> e2.salary;

