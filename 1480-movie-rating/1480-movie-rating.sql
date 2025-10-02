# Write your MySQL query statement below
(
    select u.name as results
    from users u
    JOIN MovieRating m on u.user_id=m.user_id
    GROUP BY u.user_id 
    ORDER BY COUNT(m.rating) DESC,u.name 
    LIMIT 1
)
UNION ALL
(
    SELECT mo.title AS results
    FROM movies mo
    JOIN movierating mr ON mo.movie_id = mr.movie_id
    WHERE mr.created_at LIKE '2020-02%'
    GROUP BY mo.movie_id
    ORDER BY AVG(mr.rating) DESC, mo.title 
    LIMIT 1
);