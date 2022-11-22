namespace Practice
{
    public class Vehicle
    {
        public string make;
        public string colour;
        public int year;

        public Vehicle(string Make, string Colour, int Year)
        {
            make = Make;
            colour = Colour;
            year = Year;
        }

        public void display()
        {
            Console.WriteLine($"My car make is {make}. My car colour is {colour}. I am honking my horn.");
        }
    }

    // public class Truck : Vehicle
    // {
    //     // public Truck() : base(Make, Colour, Year)
    //     // {
    //     //     make = Make;
    //     //     colour = color
    //     // }
    // }
}