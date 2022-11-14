-- ALTER TABLE Employees
-- ADD Gender varchar(255);

ALTER TABLE Employees
DROP COLUMN Gender;

SELECT * FROM Employees;