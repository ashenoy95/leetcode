# Write your MySQL query statement below
select max(e1.Salary) as SecondHighestSalary
from Employee e1
where e1.Salary<(select max(e2.Salary) from Employee e2)
