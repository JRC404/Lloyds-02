using System;
using System.Collections.Generic;

namespace DataStructures
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<string> myFirstQueue = new Queue<string>();
            // FIFO - First in, first out

            // add to our queue
            myFirstQueue.Enqueue("Miley Cyrus");
            myFirstQueue.Enqueue("Random Podcast");
            myFirstQueue.Enqueue("Lady Gaga");
            myFirstQueue.Enqueue("Atmosphere");
            myFirstQueue.Enqueue("Brother Ali");

            myFirstQueue.Dequeue(); // which will leave?

            Console.WriteLine(myFirstQueue.Peek()); // displays Random Podcast

            Console.WriteLine(myFirstQueue.Contains("Brother Ali")); // what do we think this would say?
            // number, true / false, 

            myFirstQueue.Clear();

            Queue<int> challengeQueue = new Queue<int>();

            challengeQueue.Enqueue(1);
            challengeQueue.Enqueue(8);
            challengeQueue.Enqueue(7675);
            challengeQueue.Enqueue(4545);
            challengeQueue.Peek();
            challengeQueue.Enqueue(43131);
            challengeQueue.Dequeue();
            challengeQueue.Dequeue();
            challengeQueue.Enqueue(12345);
            challengeQueue.Peek();
            challengeQueue.Contains(4545);

            // TODO: The order of the queue at the end
            // TODO: Value of line 35, 40 & 41

               foreach (var item in challengeQueue)
               {
                Console.WriteLine(item);
               }
        }
    }
}