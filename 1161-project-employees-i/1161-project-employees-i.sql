# Write your MySQL query statement below
select p.project_id, ROUND(AVG(e.experience_years),2) as average_years
From Project p
Join Employee e on e.employee_id=p.employee_id
Group by p.project_id;