namespace Logic
{
    public class Return
    {
        public void addition(int numberOne, int numberTwo)
        {
            Console.WriteLine(numberOne + numberTwo);
            // we can just do add.addition(); 
            // this will display the value to the console
        }

        public int subtraction(int numberOne, int numberTwo)
        {

            return numberOne - numberTwo;
            // if we do add.subtraction()... nothing will display
            // we have to do: int sum = add.subtraction();
            // Console.WriteLine(sum);
        }

        public string display(string inputOne) 
        {
            string newValue = $"Hi, I am {inputOne}";
            return newValue;
        }
    }
}