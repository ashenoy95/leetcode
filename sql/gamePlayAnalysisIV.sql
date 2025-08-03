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

-- method 2: join (optimized)
with first_login as 
(
select
    player_id, 
    min(event_date) as event_date
from
    activity
group by 1
)

select  
    round(1.0*sum(
        case
            when a.player_id is not null then 1 
            else 0
        end
    )/count(fl.player_id), 2) as fraction
from 
    first_login fl
left join
    activity a
on
    fl.player_id = a.player_id
    and a.event_date = fl.event_date+1
;
