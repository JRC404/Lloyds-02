using System;
using System.Collections.Generic;

namespace DataStructures
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<string> myFirstStack = new Stack<string>();
            // LIFO - Last in, first out

            myFirstStack.Push("Miley Cyrus");
            myFirstStack.Push("Random Podcast");
            myFirstStack.Push("Song 2");
            myFirstStack.Push("Queen");
            myFirstStack.Push("Adele");
            myFirstStack.Push("Dog flapping in the car window");

            myFirstStack.Pop();
            myFirstStack.Pop();
            myFirstStack.Pop();


            Console.WriteLine(myFirstStack.Peek()); // song 2
            
            Console.WriteLine("-----");

            myFirstStack.Push("Adele");
            Console.WriteLine(myFirstStack.Peek()); // adele

            Console.WriteLine("-----");

            myFirstStack.Pop(); // adele removed
            Console.WriteLine(myFirstStack.Peek()); // song 2

            Console.WriteLine("-----");

            Console.WriteLine(myFirstStack.Contains("Adele"));
            Console.WriteLine("-----");

            foreach (var item in myFirstStack)
            {
                Console.WriteLine(item);
            }

            Stack<int> challengeStack = new Stack<int>();

            challengeStack.Push(1); // 1
            challengeStack.Push(8); // 8, 1
            challengeStack.Push(7675); // 7675, 8, 1
            challengeStack.Contains(8); // true
            challengeStack.Pop(); // 7675
            challengeStack.Push(4545); // 4545, 8, 1
            challengeStack.Peek(); // 4545
            challengeStack.Push(43131); // 43131, 4545, 8, 1
            challengeStack.Pop(); // 43131
            challengeStack.Pop(); // 4545
            challengeStack.Push(12345); // 12345, 8, 1
            challengeStack.Peek(); // 12345
            challengeStack.Contains(4545); // false
            // 12345, 8, 1

            //TODO: Line, 52, 55, 60, 61
            // TODO: Order of the stack
            foreach (var item in challengeStack)
            {
                Console.WriteLine(item);
            }
        }
    }
}