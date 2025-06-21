# Write your MySQL query statement below
Select * From Cinema
where description != "boring"
AND id % 2 != 0
Order By rating DESC;