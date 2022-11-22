namespace Logic
{
    public class Mathematics
    {
        // public - accessibility levels
        // void - type for the method
        // data type - type for the variables inside of the method
        public void addition(int numberOne, int numberTwo)
        {
            int sum = numberOne + numberTwo;
            Console.WriteLine(sum);
        }
        public void subtraction(int numberOne, int numberTwo)
        {
            int sum = numberOne - numberTwo;
            Console.WriteLine(sum);
        }
        public void multiplication(int numberOne, int numberTwo)
        {
            int sum = numberOne * numberTwo;
            Console.WriteLine(sum);
        }
        public void division(double numberOne, double numberTwo)
        {
            double sum = numberOne / numberTwo;
            // double: 3.3333333333333335
            // float: 3.3333333
            // decimal: 3.3333333333333333333333333333
            Console.WriteLine(sum);
        }
    }
}