# Write your MySQL query statement below
select distinct email as Email from person
Group By email
Having Count(email) > 1;

