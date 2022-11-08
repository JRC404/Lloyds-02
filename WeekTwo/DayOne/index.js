// let myAge = 57;

// function birthday() {
//     myAge++;
//     console.log(myAge);
// }

const birthday = (myAge) => {
    // let birthday = () => {
    myAge++;
    console.log(myAge);
}

// birthday = 6; // using let birthday will allow me to change birthday to the value of 6... kinda annoying if we want to age
// console.log(birthday)

birthday(); // running the function
birthday(40); // running the function
birthday(30); // running the function

// we need to be in the folder where our file is
// WeekTwo > DayOne > index.js
// node index.js

// pwd will show us where we are

const namePrinter = (myName) => {
    console.log('Hello, ' + myName);
    console.log(`Hello, ${myName}`);
}

namePrinter("Jehcub");

let myEmployer = "Firebrand Training LTD";

if (myEmployer == "Lloyds Banking Group") {
    console.log("Welcome to Lloyds");
}
else if (myEmployer == "Halifax") {
    console.log("Welcome to Halifax");
}
else if (myEmployer == "Firebrand Training LTD") {
    console.log("Welcome to Firebrand")
}
else {
    console.log("Who do you work for?")
}

// the age calculator from last week... please build that in JavaScript