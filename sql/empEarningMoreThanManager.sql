# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1 
where e1.Salary>(select e2.Salary from Employee e2 where e2.Id=e1.ManagerId)