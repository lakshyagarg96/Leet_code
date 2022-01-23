# Write your MySQL query statement below


select case when max(a.rank_v) < 2 then Null else a.salary end as SecondHighestSalary
from
(
select e.id,
    e.salary,
rank() over (order by salary desc) as rank_v
from employee as e
) as a
where a.rank_v = 2