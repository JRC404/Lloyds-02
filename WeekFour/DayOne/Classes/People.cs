class Person
{ 
    public string FirstName;

    public string LastName;

    public int Age;

    public Person(string firstName, string lastName, int age)
    {
        FirstName = firstName;
        LastName = lastName;
        Age = age;
    }
   
}

class Employee : Person
{

    public string JobTitle;
    public decimal Salary;

    public Employee(string firstName, string lastName, int age, string jobTitle, decimal salary)
        : base(firstName, lastName, age)
    {
        JobTitle = jobTitle;
        Salary = salary;
    }

}