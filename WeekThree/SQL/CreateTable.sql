CREATE TABLE Employees (
	EmployeeID int PRIMARY KEY, -- Unique column that we will use to ID staff
    FullName varchar(255), -- 255 is the limit of characters
    Location varchar(255),
    Salary int,
    Employed bit -- binary value 1 OR 0 (Boolean)
)