SELECT s.user_id,
    COALESCE(
        ROUND(
            SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)  
            / NULLIF(COUNT(c.user_id), 0), 
            2
        ),
        0
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON c.user_id = s.user_id
GROUP BY s.user_id;
