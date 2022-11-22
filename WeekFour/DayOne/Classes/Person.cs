namespace Practice
{
    public class Person
    {
        string firstName = "Jacob";
        string lastName = "Reilly-Cooper";
        int age = 57;

        public void details()
        {
            Console.WriteLine(firstName);
            Console.WriteLine(lastName);
            Console.WriteLine(age);
            // firstName is inaccessible to other classes due to it's protection level
        }
    }
}