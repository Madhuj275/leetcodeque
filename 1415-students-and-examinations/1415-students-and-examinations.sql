# Write your MySQL query statement below
SELECT s.student_id,s.student_name,sub.subject_name,
    COALESCE((
        SELECT COUNT(*)
        FROM Examinations e
        WHERE e.student_id = s.student_id
          AND e.subject_name = sub.subject_name
    ), 0) AS attended_exams
FROM Students s
JOIN Subjects sub
ORDER BY s.student_id, sub.subject_name;
