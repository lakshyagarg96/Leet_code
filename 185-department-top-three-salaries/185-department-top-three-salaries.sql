

    
select e.deparmtent_name as Department,
e.name as Employee,
e.salary as Salary
# min(e.salary) as min_salary
from
(
select e.name,
    e.salary,
    e.departmentid,
    d.name as deparmtent_name,
    d.id,
dense_rank() over ( partition by d.name order by e.salary desc) as rank_2
from employee as e
left join 
department as d
on e.departmentid = d.id 
) as e
where e.rank_2 < 4
