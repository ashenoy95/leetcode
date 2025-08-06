select results from (
select 
    u.name as results
from
    MovieRating mr
join
    users u
on
    mr.user_id = u.user_id
group by u.user_id, u.name
order by count(mr.*) desc, u.name 
limit 1
)

union all

select * from (
select
    m.title
from 
    MovieRating mr
join
    movies m
on
    mr.movie_id = m.movie_id
where
    mr.created_at >= '2020-02-01' and mr.created_at < '2020-03-01'
group by m.movie_id, m.title
order by avg(mr.rating) desc, m.title
limit 1
)
;
