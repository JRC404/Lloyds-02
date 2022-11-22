// Console.WriteLine("What is your name?");

// string userInput = Console.ReadLine();
// Console.WriteLine($"Hello, {userInput}.");

// Console.WriteLine("How old are you?");

// userInput = Console.ReadLine();
// Console.WriteLine($"You are {userInput} years old.");

// Console.WriteLine("Where are you based?"); // Manchester
// // take user input and write it to the console
// userInput = Console.ReadLine();
// Console.WriteLine($"You are based in {userInput}");

// Console.WriteLine("Do you know Caz from Countdown? (Y / N)"); // Yes or no
// userInput = Console.ReadLine();

// if(userInput == "Y" || userInput == "y" || userInput == "yes" || userInput == "Yes")
// {
//     Console.WriteLine("You do know Caz. Nice.");
// }
// else {
//     Console.WriteLine("Oh. Shame.");
// }

// ask the user... would they like to play a game?
// if yes, great. if no, unlucky, you're playing anyway.

// ask the user which direction they'd like to go in? (N, E, S, W)
// if north, say something
// else if east, say something
// else if south, say something
// else if west, say something

// else... you died.

int userHealth = 100;
Console.WriteLine("Wanna play a game?");
string userInput = Console.ReadLine();

if (userInput == "Yes")
{
    Console.WriteLine("That's a silly choice");
}

Console.WriteLine("Which direction? (N, E, S, W)");

userInput = Console.ReadLine();

if (userInput == "N")
{
    Console.WriteLine("It's cold up here. Did you bring a coat? (Yes / No)");
    userInput = Console.ReadLine();

    if(userInput == "Yes") {
        Console.WriteLine("Good. Did you bring a hat? (Yes / No)");
        userInput = Console.ReadLine();

        if(userInput == "Yes") {
            Console.WriteLine("You're a smart person. I like you.");
        }
        else {
            Console.WriteLine("You died. You kinda deserved it. It's -40c");
        }
    }
    else {
        userHealth -= 10;
        Console.WriteLine($"Stupid.Your health is now {userHealth}");
    }
}
else if(userInput == "S") 
{
    Console.WriteLine("It's warm down here. Did you bring sunscreen?");
    userInput = Console.ReadLine();

    if(userInput == "Yes") {
        Console.WriteLine("Good.");
    }
    else {
        userHealth -= 20;
        Console.WriteLine($"Stupid. You look like a tomataaa. Your health is now {userHealth}");
    }
}