using System;

namespace Inherit
{
    class Program
    {
        static void Main(string[] args)
        {
            People reece = new People("Reece", "Morgan", 45);
            Worker bob = new Worker("Bob", "Bobbington", 44, "Worker", 10000);

            Console.WriteLine(reece);
            Console.WriteLine(bob);
        }
    }
}