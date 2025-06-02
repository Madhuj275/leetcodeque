# Write your MySQL query statement below
Select d.name as Department,e.name as Employee,e.salary as Salary
From employee e
Join department d on e.departmentId=d.id
WHERE
    (
        SELECT COUNT(DISTINCT e2.salary)
        FROM employee e2
        WHERE e2.departmentId = e.departmentId
          AND e2.salary > e.salary
    ) < 3
order By Department,salary desc;