-- Method 1: LEAD()
select 
    round(1.0*sum(
        case 
            when second_login - first_login = 1 then 1
            else 0
        end
    )/count(distinct player_id), 2) as fraction
from 
(
select
    player_id,
    event_date as first_login,
    lead(event_date, 1) over(partition by player_id order by event_date) as second_login,
    row_number() over(partition by player_id order by event_date) as login_order
from
    activity
)
where
    login_order = 1
;
