using System;

namespace DataStructures
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] favouriteArtists = {"Miley Cyrus", "Lady Gaga", "Jimmy Blunt"};
            // all arrays start counting at 0

            Console.WriteLine(favouriteArtists[0]);
            // .Length
            for (int i = 0; i < favouriteArtists.Length; i++)
            {
                Console.WriteLine(favouriteArtists[i]);
            }

            favouriteArtists[2] = "James Blunt";
            // favouriteArtists[3] = "Queen"; //! the index you've tried to access doesn't exist. Index was outside the bounds of the array

            // creating a new string array
            string[] favouriteFood = new string[5];
            favouriteFood[0] = "Cheese";
            favouriteFood[1] = "Cheese";
            favouriteFood[2] = "Cheese";
            favouriteFood[3] = "Cheese";
            favouriteFood[4] = "Cheese";
            // favouriteFood[5] = "Cheese";

            for (int i = 0; i < favouriteFood.Length; i++)
            {
                Console.WriteLine(favouriteFood[i]);
            }

            string[] employers;

            employers = new string[] {"Lloyds", "Firebrand", "Halifax", "Black Horse"};
        
        
        }
    }
}