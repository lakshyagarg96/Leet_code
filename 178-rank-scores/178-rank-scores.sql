# Write your MySQL query statement below


select a.score,
a.rank_2 as 'rank'
from
(
select s.id,
s.score,
dense_rank() over (order by s.score desc) as rank_2
from scores as s
) as a
order by a.score desc
