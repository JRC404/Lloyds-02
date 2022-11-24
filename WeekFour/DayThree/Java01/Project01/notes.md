# Java


## First look at Java
```java
// First App.java file
import java.text.MessageFormat;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        int myInt = 10;
        long myLong = 10;
        float myFloat = 10.5f;
        double myDouble = 10.5;
        boolean myBool = true;
        String myString = "Jacob";

        System.out.println("Hello, " + myString);
        System.out.println(String.format("Hello, %s", myString));

        System.out.println(MessageFormat.format("Hello, {0}", myString));

        if (myInt < 20) {
            System.out.println("WooHoo. Less than 20");
        } else {
            System.out.println("Not less than 20 then?");
        }

        switch (myString) {
            case "Jehcub":
                System.out.println("Hi, Jehccuuuub");
                break;
            case "Jacob":
                System.out.println("Hi, Jacob");
                break;
            default:
                System.out.println("Don't know who you are.");
                break;
        }

        while (myInt < 100) {
            System.out.println(myInt);
            myInt++;
        }

        do {
            System.out.println(myLong);
            myLong++;
        } while (myLong < 500);

        // whilst myInt is less than 100... sout myInt
        // do sout myLong whilst myLong is less than 100
        // for loop - try and see what happens

        for(int i = 0; i < 1000; i++)
        {
            System.out.println(i);
        }
    }
}

```

## Try-Catch in App.java
```java
try {
    String[] myFirstArray = { "Random", "Array", "Values" };
    System.out.println(myFirstArray[50]);
} catch (Exception err) {
    System.out.println("Uh oh.");
    System.out.println(err);
    System.out.println(err.getMessage()); // focused error message
}
```