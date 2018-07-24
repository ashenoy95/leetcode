# Write your MySQL query statement below
select 
    d.Name as Department,
    e.Name as Employee, 
    e.Salary as Salary
from Employee e 
inner join Department d 
on d.Id=e.DepartmentId 
where e.Salary>=all(select e2.Salary from Employee e2 where e2.DepartmentId=e.DepartmentId)