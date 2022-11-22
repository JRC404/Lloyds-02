using System;
using Logic; // use the namespace logic and allow the class to access the namespace

namespace Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Polymorphism demo = new Polymorphism();

            demo.addition(1, 5);
            demo.addition(1.0, 5.4);
            demo.addition("1.0", "5.4"); // I want it to say 6.4
            
        }
    }
}