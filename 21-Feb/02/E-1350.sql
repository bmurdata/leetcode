--2/2/21
--Question https://leetcode.com/problems/students-with-invalid-departments/

# Write your MySQL query statement below

SELECT s.id, s.name
FROM Students as S LEFT JOIN Departments as D ON S.department_id=D.id
WHERE D.id IS null