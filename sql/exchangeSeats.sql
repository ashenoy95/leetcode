select
    id,
    case
        when id%2 <> 0 then coalesce(lead(student, 1) over(order by id), student)
        else lag(student, 1) over(order by id)
    end as student
from
    seat
;
