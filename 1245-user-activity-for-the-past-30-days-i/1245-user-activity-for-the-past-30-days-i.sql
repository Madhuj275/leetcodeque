# Write your MySQL query statement below
select activity_date as day , COUNT( distinct user_id) as active_users
from Activity
where activity_date > '2019-06-27' and activity_date <= '2019-07-27'
group by activity_date;
