-- Operators.sql

SELECT * FROM Employees;

-- AND --
SELECT * FROM Employees
WHERE Location = 'Fife' AND Salary < 30000;

-- OR --
SELECT * FROM Employees
WHERE Salary < 40000 OR Location = 'Manchester';

-- NOT --
SELECT * FROM Employees
WHERE NOT Location = 'Manchester';