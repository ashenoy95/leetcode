-- Write your PostgreSQL query statement below
select 
    id,
    count(*) as num
from (
select requester_id as id from RequestAccepted

union all

select accepter_id from RequestAccepted
)
group by 1
order by count(*) desc
limit 1
;
