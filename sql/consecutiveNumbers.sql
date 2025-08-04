-- Write your PostgreSQL query statement below
select distinct
    num as ConsecutiveNums
from (
    select
        id,
        num,
        lead(num, 1) over(order by id) as second,
        lead(num, 2) over(order by id) as third
    from
        logs
)
where 
    second = num
    and third = num
;
