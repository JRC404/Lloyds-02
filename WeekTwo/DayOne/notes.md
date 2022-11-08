# Content for Week 02

## JavaScript

* Fundamentals of JavaScript
* The differences between JavaScript and Python
* Arrays in JavaScript
* Classes and Objects
* Functions -> lots of functions

### Variables

* To declare a variable in JavaScript, we have to use 1 of 3 keywords:
    * let (since 2016)
    * var (pre 2016)
    * const (since forever)

```js
let myName = "Jacob";
var myAge = 57;
const dateOfBirth = "01/01/1965";
```

* Constants are variables and structures that will never change

* We have the ability to declare and define our variables
```js
let myName; // this is a declaration
myName = "Jacob"; // this is a definition

let myFavouriteSinger = "Miley Cyrus"; // the declaration and definition
```

* Naming Conventions in JavaScript:
    * Camel Casing for everything except Classes and Objects
        * myFirstVariable = "Cheese"
    * Classes and objects use Pascal Casing
        * class MyClass = {}

* Data Types in JavaScript
    * string
    * number (both integer and float numbers)
    * boolean
    * null -> nothing
    * undefined -> it doesn't know what it is

```js
// undefined vs null
let myVariable; // no definition
console.log(myVariable) // undefined

myVariable = null; // there is a definition and that definition is null!
console.log(myVariable) // null
```
* The beauty and the pain of JavaScript is we can be flexible / loose with our variable definitions
```js
let myName = "Jacob";
myName = 57;
myName = true;
myName = "Bob";
myName = undefined;
myName = 57.6;
myName = "Tim";
```

* print in Python is now console.log() in JavaScript

* Semicolons in JavaScript are... not expected but you can use them! 
* If you use them, continue to do so
* If you don't, don't!

### Many Flavours of JavaScript

* Vanilla JavaScript
* React.js, Angular.js, Vue.js, Ember.js, Lightning.js
* Node.js, Express.js, Deno.js
* TypeScript -> a stricter JavaScript
**Not an exhaustive list**

```js
let myAge = 57;

function birthday() {
    myAge++;
}

const birthday = () => {
    myAge++;
}
```

#### Switch cases

### Objects

* Objects hold key : value pairs
* Objects in JavaScript can have methods / functions
* Objects are defined by {}

## HTML & CSS

## Testing - Thursday and Friday :-) 


## Easy Answer to 0.1 + 0.2 not == 0.3

* The compiler cannot round the number precisely enough

