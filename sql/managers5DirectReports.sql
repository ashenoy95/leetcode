with manager as 
(
select
    e.managerId
from
    employee e
group by 1
having count(distinct e.id) >= 5
)

select
    e.name
from 
    employee e
join
    manager m
on
    e.id = m.managerId
;
