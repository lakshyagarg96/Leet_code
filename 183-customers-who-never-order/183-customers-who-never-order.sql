# Write your MySQL query statement below

select c.name as customers 
from customers as c
left join
(
select customerid, count(id) as times_order
    from orders
    group by customerid
) as d
on c.id = d.customerid
where d.times_order is null
