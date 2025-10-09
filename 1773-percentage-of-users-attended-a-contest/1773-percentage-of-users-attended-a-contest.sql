# Write your MySQL query statement below
Select contest_id,ROUND(COUNT(distinct user_id)*100/(SELECT COUNT(DISTINCT user_id) FROM Users),2) as percentage
FROM Register 
Group by contest_id
Order by percentage desc,contest_id ;