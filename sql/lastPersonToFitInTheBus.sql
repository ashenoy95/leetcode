-- Write your PostgreSQL query statement below
select
    person_name 
from (
    select
        person_name,
        turn
    from (
        select
            person_name,
            turn,
            sum(weight) over(order by turn) as running_weight
        from
            queue
    )
    where 
        running_weight <= 1000
    order by turn desc
    limit 1
)
;
