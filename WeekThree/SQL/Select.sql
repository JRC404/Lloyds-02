SELECT * FROM Employees;
-- * means everything... show me everything!

SELECT EmployeeID FROM Employees;

SELECT EmployeeID, FullName FROM Employees;

SELECT * FROM Employees
WHERE Location = 'Manchester';

SELECT * FROM Employees
WHERE Salary < 50000;

SELECT EmployeeID, FullName FROM Employees
WHERE Employed = 1;