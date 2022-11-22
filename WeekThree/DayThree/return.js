const addition = (numberOne, numberTwo) => {
    let answer = numberOne + numberTwo;
    // console.log(answer);
    return answer; // boxing up the variable and allowing it to be passed on to anywhere that wants it
}
const subtraction = (numberOne, numberTwo) => {
    let answer = numberOne - numberTwo;
    return answer; 
}

// TODO: Please recreate sub, div, and mul functions
// TODO: Save the value from the return and then console log the value

// reuse is going to become the value that the addition function returns
let reuse = addition(200, 500); // 70, undefined, or nothing?
let additionAnswer = addition(20, 50);
let subtractionAnswer = subtraction(50, 20);
let divisionAnswer = division(10, 2);
let multiplicationAnswer = multiplication(10, 20);

// let reuse = addition(10, 20);
console.log(`Reuse has a value of ${reuse}`);

const myName = (name) => {
    // console.log(name); // print to the console
    return name; // allow the value to be stored
}

let storeName = myName("Halle Ewan");
console.log(`My name is: ${storeName}`);
storeName = myName("Bob Dylan")
console.log(`My name is: ${storeName}`); // 