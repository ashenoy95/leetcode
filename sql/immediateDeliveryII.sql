-- Write your PostgreSQL query statement below
select 
    round(100.0*count(immediate_order)/count(*), 2) as immediate_percentage
from
(
    select
        customer_id,
        case 
            when order_date = customer_pref_delivery_date 
                then delivery_id 
        end as immediate_order,
        row_number() over(partition by customer_id order by order_date) as order_num
    from
        delivery
)
where
    order_num = 1
;
