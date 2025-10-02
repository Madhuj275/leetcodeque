# Write your MySQL query statement below
SELECT a1.machine_id , ROUND(avg(a2.timestamp-a1.timestamp),3) as processing_time
From Activity a1
JOIN activity a2 on a2.machine_id = a1.machine_id and a2.process_id=a1.process_id
AND a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id;