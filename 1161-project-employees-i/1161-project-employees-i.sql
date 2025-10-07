# Write your MySQL query statement below
select p.project_id,ROUND((SUM(e.experience_years)/COUNT(p.project_id)),2) as average_years
From Project p
join Employee e on p.employee_id=e.employee_id
group by p.project_id;