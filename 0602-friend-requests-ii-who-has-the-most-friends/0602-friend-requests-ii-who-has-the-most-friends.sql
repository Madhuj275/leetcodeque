# Write your MySQL query statement below
Select id,COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS combined_ids
GROUP BY id
Order by num desc
LIMIT 1;
