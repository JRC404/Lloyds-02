-- Max.sql

SELECT MAX(Salary) FROM Employees
WHERE Location = 'Fife';

-- Min.sql

SELECT MIN(Salary) FROM Employees
WHERE Location = 'Fife';

-- Average.sql

SELECT AVG(Salary) FROM Employees
WHERE Location = 'Fife';

-- Sum.sql

SELECT SUM(Salary) FROM Employees
WHERE Location = 'Fife';

-- Count.sql

SELECT COUNT(Salary) FROM Employees
WHERE Location = 'Fife';