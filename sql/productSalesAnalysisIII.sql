with first_sale as 
(
    select
        product_id,
        min(year) as first_year
    from 
        sales 
    group by 1
)
select
    fs.product_id,
    fs.first_year,
    s.quantity,
    s.price
from 
    sales s
join
    first_sale fs
on
    s.product_id = fs.product_id
    and s.year = fs.first_year
;
