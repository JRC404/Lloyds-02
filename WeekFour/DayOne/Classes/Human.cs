namespace Practice
{
    public class Human 
    {
        public string firstName = "Sally";
        string lastName = "Bobbington";
        int age = 30;

        public void display()
        {
            Console.WriteLine($"Hello, I am {firstName}");
        }
    }

    public class Child : Human // C#
    // Child extends Human - JS
    // Child(Adult) - Python
    {
        public void cry() 
        {
            Console.WriteLine("I am crying.");
        }
    }
}