// equality operator

let value = "10";

if(value === 10) {
    console.log("Both the value and the type matched.");
}
else if(value == 10) {
    console.log("The value matched, but the type didn't.")
}
else {
    console.log("Else statement activated.");
}

// 10 and "10" are the same value?
// == soft equality -> comparing the value of two variables, not the type
// if the value matches, great. Proceed.

// === strict equality -> comparing the value AND the type of the two variables
// if the value matches, but the type doesn't... it is not a match.

// OR, AND, XOR
// || or - if the left OR the right is true OR BOTH
// && and - if the left AND the right are true
// ^ exclusive or - if the left OR the right is true BUT NOT both

let numberOne = 10;
let numberTwo = 20;

if(numberOne < 20 || numberOne == 10) {
    console.log("WooHoo."); // will this say WooHoo? True
}

if(numberOne < 15 && numberTwo == 20) {
    console.log("Great stuff.");
}

if(numberOne < 15 ^ numberTwo == 20) {
    console.log("Awesome."); // what will happen here?
}
else {
    console.log("Oh.");
}

if(!(numberOne < 15 ^ numberTwo == 20)) {
    console.log("Awesome."); // the not operator reverses the original result
    //* ! instead of the keyword not :-)
}
else {
    console.log("Oh.");
}