# Write your MySQL query statement below
select b.id,
case when b.id % 2 = 0 then b.prev_name else b.next_name end as student
from
(

select s1.id,
s1.student,
Lag(s1.student) over (order by id ) as prev_name,
case when (Lead(s1.student) over (order by id )) is null then s1.student else (Lead(s1.student) over (order by id )) end as next_name
from 
seat as s1
) as b