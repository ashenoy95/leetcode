-- Write your PostgreSQL query statement below
with conf as 
(
select
    user_id,
    sum(
        case
            when action = 'confirmed' then 1
            else 0
        end
    )*1.0/count(*) as confirmation_rate
from
    confirmations
group by 1
)

select distinct
    s.user_id,
    round(coalesce(c.confirmation_rate, 0), 2) as confirmation_rate
from    
    signups s
left join
    conf c
on
    s.user_id = c.user_id
;
