
select
distinct(a.num) as ConsecutiveNums
from
(
select id,
num,
Lead(num) over (order by id ) as next_value,
Lag(num) over (order by id ) as prev_value
from logs as l
) as a
where a.prev_value = a.next_value 
and a.prev_value = a.num
# group by a.num
# having count(a.num) > 1