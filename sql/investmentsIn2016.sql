-- self-join
-- Write your PostgreSQL query statement below
select  
    round(cast(sum(tiv_2016) as decimal), 2) as tiv_2016
from (
select distinct
    ins.*
from
    insurance ins
join
    insurance ins2
on
    ins.pid <> ins2.pid
    and ins.tiv_2015 = ins2.tiv_2015
left join (
    select
        lat, 
        lon
    from
        insurance
    group by 1, 2
    having count(*) > 1 
) same_city
on
    ins.lat = same_city.lat
    and ins.lon = same_city.lon
where
    same_city.lat is null
)
;

-- optimzaed: in/not in clause
select  
    round(sum(tiv_2016)::decimal, 2) as tiv_2016
from 
    insurance
where
    tiv_2015 in (select tiv_2015 from insurance group by 1 having count(*) > 1)
    and (lat, lon) not in (select lat, lon from insurance group by 1, 2 having count(*) > 1)
;
