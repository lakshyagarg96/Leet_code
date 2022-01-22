# Write your MySQL query statement below
select e_1.name as Employee
from employee as e_1
left join employee as e_2
on e_1.managerId = e_2.id
where e_1.salary > e_2.salary
and e_1.managerid is not null;

