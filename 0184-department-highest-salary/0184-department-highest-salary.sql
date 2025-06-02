# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary 
from employee e
Right Join department d on e.departmentid=d.id 
where e.salary=(select MAX(salary) from employee
                WHERE departmentId = e.departmentId);