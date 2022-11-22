// Polymorphism.cs
namespace Practice
{
    public class Polymorphism
    {
        public void addition(int numberOne, int numberTwo)
        {
            Console.WriteLine(numberOne + numberTwo);
        }

        public void addition(double numberOne, double numberTwo)
        {
            Console.WriteLine(numberOne + numberTwo);
        }

        public void addition(string inputOne, string inputTwo)
        {
            double inputUno = Convert.ToDouble(inputOne);
            double inputDos = Convert.ToDouble(inputTwo);
            Console.WriteLine(inputUno + inputDos);

            // parse
            double sum = Double.Parse(inputOne) + Double.Parse(inputTwo);

            double answer = Convert.ToDouble(inputOne) + Convert.ToDouble(inputTwo);
            Console.WriteLine(answer);

            Console.WriteLine(Convert.ToDouble(inputOne) + Convert.ToDouble(inputTwo));
        }
        // TODO: inside of the string addition...
        // TODO: convert the sum of inputOne + inputTwo to be 6.4 instead of 1.05.4 (Double)
        // TODO: demo.addition("1.0", "5.4");

        // TODO: What if it can't be converted? Try this? Console.WriteLine the answer...
    }
}