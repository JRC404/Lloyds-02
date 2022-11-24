namespace Inherit
{
    class Worker : People
    {
        public string jobRole;
        public int salary;

        public Worker(string FirstName, string LastName, int Age, string JobRole, int Salary) : base(FirstName, LastName, Age)
        {
            jobRole = JobRole;
            salary = Salary;
        }
    }
}