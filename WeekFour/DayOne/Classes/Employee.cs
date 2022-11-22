// Inheritance.cs
namespace Practice
{
    public class Employee
    {
        //TODO: Vehicle class with a honk method that says something...
        int employeeID;
        public string fullName;
        public string location;
        public string role;
        public int salary;

        public Employee(int employee_ID, string full_Name, string Location, string Role, int Salary) // constructor
        {
            employeeID = employee_ID;
            fullName = full_Name;
            location = Location;
            role = Role;
            salary = Salary;
        }


        public void displayID() 
        {
            Console.WriteLine($"My Employee ID is {employeeID}");
        }
    }
}