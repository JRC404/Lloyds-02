using System;
using System.Collections.Generic;

namespace DataStructures
{
    class Program
    {
        static void Main(string[] args)
        {
            // lists in c# allow us to add, remove, find, sort, reverse sort and much more in our application
            List<string> favouriteArtists = new List<string>();

            favouriteArtists.Add("Miley Cyrus");
            favouriteArtists.Add("Lady Gaga");
            favouriteArtists.Add("James Blunt");
            favouriteArtists.Add("Cher");
            favouriteArtists.Add("Chris Stapleton");
            favouriteArtists.Add("Lewis Capaldi");

            // favouriteArtists[0] = "Bob Bobbington";

            favouriteArtists.Insert(1, "Hannah Montana");
            favouriteArtists.Insert(7, "Queen"); // what will happen here?
            // favouriteArtists.Insert(10, "Queen"); //! Index must be within the bounds of the List

            // remove at an index value
            favouriteArtists.RemoveAt(1); // Hannah Montana

            favouriteArtists.Remove("Cher"); // I wonder what we removed here?
           

            // for (int i = 0; i < favouriteArtists.Count; i++)
            // {
            //     Console.WriteLine(favouriteArtists[i]);
            // }

            foreach (string artist in favouriteArtists)
            {
                Console.WriteLine(artist);
            }

            Console.WriteLine("-------");

            favouriteArtists.Sort();

            foreach (string artist in favouriteArtists)
            {
                Console.WriteLine(artist);
            }

            Console.WriteLine("-------");

            favouriteArtists.Reverse();

            foreach (string artist in favouriteArtists)
            {
                Console.WriteLine(artist);
            }

            // TODO: Create an integer list with 10 items to start
            // TODO: Add 3 items
            // TODO: Insert 3 items
            // TODO: Remove 2 specific items
            // TODO: Remove 2 index values
            // TODO: Sort the list
        }
    }
}