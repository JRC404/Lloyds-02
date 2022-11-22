# C# 

* C# is a strongly-typed language
    * This means we have to declare the data type we are going to be using
    * Dotnet in 2019, brought in the var keyword to replace the data types... we'll look at that too
* C# is a strict language... semi-colons are needed at the end of each statement (this doesn't mean the end of each line)
* C# is a compiled language

* Normally, we use Visual Studio for C#. We are going to use Visual Studio Code:
    * Why? It is faster, we are only creating console applications... and it's familiar

## Data Types

* int -> integer 0-9
    * -2,147,483,648 to 2,147,483,647
* long -> long integer 0-9
    * -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
* float -> decimal number
    * Accurate to 6 / 7 decimal places
* double -> decimal number
    * Accurate to 15 decimal places
* decimal -> decimal number
    * Accurate to 28 / 29 decimal places
* bool -> boolean value
    * true or false
* string -> string of text
    * "" -> you must use double quotes in C# for strings
    * String has 2 bytes of meory per character
* char -> single character
    * '' -> you must use single quotes in C# for a char

### Int

* int -> int32: 32-bit
* long -> int64: 64-bit

* byte -> 8-bit (0 - 255)
* short -> int16: 16-bit

#### Signed and unsigned integers

* Signed integers can be both negative and positive in value
* Unsigned integers are only positive in value

* int by default is signed
* long by default is signed

* uint & ulong are the unsigned versions
* uint has a range of 0 to 4,294,967,295

## Variables.cs
```csharp
int myFirstInteger = 14;
long myFirstLong = 14;
Console.WriteLine(myFirstLong.GetType());

float myFirstFloat = 14.0f;
double myFirstDouble = 14.0; // 14.0d;
decimal myFirstDecimal = 14.0m;

bool myfirstBool = true;

string myFirstString = "Hello, World";

char myFirstChar = '+';

int wholeNumber = 10;
double decimalNumber = 45.67;

wholeNumber = (int)decimalNumber;

Console.WriteLine(wholeNumber.GetType()); // what will be the answer?

wholeNumber = 50;
decimalNumber = wholeNumber;

Console.WriteLine(decimalNumber);

Console.WriteLine(decimalNumber.GetType());

decimalNumber = 45.67;

Console.WriteLine(Convert.ToInt32(decimalNumber));
```

## Operators

* Arithmetic - same as JavaScript and Python
* Assignment - same as JavaScript and Python
* Comparison - same as JavaScript and Python
* Logical
    * && = AND
    * || = OR
    * ! = NOT