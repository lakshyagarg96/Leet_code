# Write your MySQL query statement below

select a.id,
a.visit_date,
a.people
from
(
select id, 
visit_date, 
people,
Lead(people) over (order by id ) as next_people,
Lead(people,2) over (order by id ) as next_next_people,
Lag(people) over (order by id ) as prev_people,
Lag(people,2) over (order by id ) as prev_prev_people
from Stadium
) as a
where (a.next_people >= 100 and a.next_next_people >= 100 and a.people >= 100)
or (a.prev_people >= 100 and a.prev_prev_people >= 100 and a.people >= 100)
or (a.prev_people >= 100 and a.next_people >= 100 and a.people >= 100)