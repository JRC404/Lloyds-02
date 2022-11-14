UPDATE Employees
SET Employed = 1
WHERE EmployeeID = 3; 

UPDATE Employees
SET Location = 'Fife', Employed = 1
WHERE EmployeeID = 4;

UPDATE Employees
SET Location = 'Fife', Employed = 1
WHERE Salary < 50000;

SELECT * FROM Employees;

-- PLEASE UPDATE GENDER COLUMN WITH DATA FOR ALL ROWS

-- DANGER ZONE:
-- UPDATE REQUIRES 3 THINGS
-- UPDATE keyword
-- SET keyword
-- WHERE keyword
-- IF we forget the WHERE... have fun. 
-- It will update all of the rows and set all of the Employed values to 0