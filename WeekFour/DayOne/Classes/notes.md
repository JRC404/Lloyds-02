# C#

## Brackets

- {} are for namespaces, classes and opening up methods / functions
- () are for parameters, arguments and Console stuff
- [] are for arrays, collections of items

## Main method

- Entry to our program
- Everything, and I mean everything, will go through the main method... one way or another - directly or indirectly... everything will go through it

# Object-Oriented Principles

- Inheritance
- Polymorphism
- Encapsulation - public / private
- Abstraction

## Person demo

```csharp
Person jacob = new Person();
// what have we done here? We've seen it before. We've done it before. What do we call it? Instance of a class being created

// Console.WriteLine(jacob.firstName);
// firstName is private. Private means only the class and its inherited classes can access the variable
jacob.details(); // jacob

// Console.WriteLine(jacob.age);
// Console.WriteLine(jacob.firstName);
// Console.WriteLine(jacob.lastName);

// jacob.age = 405;
// jacob.firstName = "Bob";
// jacob.lastName = "Tim";
```

## Methods

* Camel or Pascal casing for Method names
* public - accessibility level
* void - type for the method
    * void = the method can return no value
    * void means you do not have to use the return keyword in your method
    * if you declare a type for your method
    ```cs
    public int addition(int numberOne, int numberTwo)
    {
        return numberOne + numberTwo;
        // this method HAS to return an integer
    }
    ```
* data types in the parameters - type for the variables inside of the method

## Return keyword Program.cs
```cs
Return demo = new Return();

demo.addition(10, 10); // this is Console.WriteLine()
int sum = demo.subtraction(20, 10); // this is return
Console.WriteLine(sum);

string name = demo.display("Bob");
Console.WriteLine(name);
```

## Vehicle - Program.cs

```cs
 Employee bob = new Employee(100, "Bob", "Manchester", "Engineer", 10000);
            bob.displayID();

Vehicle deanna = new Vehicle("Audi", "white", 2014);
deanna.display();
//    deanna.colour = "pink";
//    Console.WriteLine(deanna.colour);
//    bob.employeeID = 10; // this shouldn't be allowed
//    Console.WriteLine(bob.employeeID);
```

## Inheritance - Program.cs
```cs
Human sally = new Human();
sally.display();
//    sally.cry();

Child bob = new Child();
bob.cry();

Console.WriteLine($"Hiya, {bob.firstName}"); // what will the value be?
// sally, nothing? Error? 
// child?
bob.firstName = "Bob";
Console.WriteLine($"Hiya, {bob.firstName}"); // what will the value be?
```