# Write your MySQL query statement below

select a.id
from 
(
select *,
Lag(temperature) over (order by recordDate asc) as prev_temp,
Lag(recordDate) over (order by recordDate asc) as prev_date
from weather
    ) as a
where a.temperature > a.prev_temp and DATEDIFF(recordDate,prev_date) = 1 ;
