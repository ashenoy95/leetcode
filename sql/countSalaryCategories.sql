-- Write your PostgreSQL query statement below
select 
    cat.category,
    coalesce(count(bank.account_id), 0) as accounts_count
from (
    select 'Low Salary' as category
    union all
    select 'Average Salary'
    union all
    select 'High Salary'
) cat
left join(
    select
        case
            when income < 20000 then 'Low Salary'
            when income >= 20000 and income <= 50000 then 'Average Salary'
            when income > 50000 then 'High Salary'
        end as category,
        account_id
    from 
        accounts
) bank
on
    cat.category = bank.category
group by 1
;
