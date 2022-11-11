// prompt.js

console.log(15);
console.log("15");

let userInput;

const options = () => {
    userInput = prompt("Which option would you like to select?\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n");
    if(userInput == 1) {
        console.log(userInput)
    }
    else {
        console.log("Computer says no")
    }
}

options()

// userInput = prompt("Please tell me your age:");
// console.log(userInput);

// // If statement for < 18 - go away
// // else - welcome them
// if (userInput < 18) {
//     console.log("Go away");
// }
// else {
//     console.log("Welcome");
// }

// // userInput = prompt("What's your name?");
// // console.log(userInput);

// // // if statement for your name - hello
// // // else - go away
// if (userInput == "Jacob") {
//     console.log(`Hello ${userInput}`);
// } else {
//     console.log("Go away");
// }

// userInput = prompt("Where do you live?");
// console.log(userInput);

// // if statement for your location - nice choice
// // else - go away

// if (userInput == "Manchester") {
//     console.log("Nice choice");
// } else {
//     console.log("Go away");
// }