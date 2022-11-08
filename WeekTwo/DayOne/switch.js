let favouriteColour = "orange";

// if (favouriteColour == "blue") {
//     console.log("WooHoo. That's blue.")
// }
// else if (favouriteColour == "pink") {
//     console.log("On the brink, that's pink.")
// }
// else if (favouriteColour == "yellow") {
//     console.log("Don't be mellow, that's yellow.")
// }
// else if (favouriteColour == "green") {
//     console.log("Sean Bean, he likes green.")
// }
// else if (favouriteColour == "orange") {
//     console.log("Orange.")
// }
// else {
//     console.log("Ummm, this is awkward?")
// }

switch (favouriteColour) {
    case "blue":
        console.log("Blue");
        break; // break ends the check if the case matches the variable
    case "pink":
        console.log("Pink");
        break;
    case "orange":
        console.log("Orange");
        break;
    case "yellow":
        console.log("Yellow");
        break;
    case "green":
        console.log("Green");
        break;
    default:
        console.log("Don't know, pal.");
        break;
}

favouriteColour = "blue";

switch (favouriteColour) {
    case "blue":
    case "pink":
    case "yellow":
    case "green":
        console.log("Wrong choice. Orange is the only one.");
        break;
    case "orange":
        console.log("Orange is the correct answer.");
    default:
        console.log("Ummm... wrong again?");
        break;
}

let carMake = "Audi";

switch (carMake) {
    case "VW":
    case "Audi":
    case "BMW":
        console.log("German Cars");
        break;
    case "Mazda":
    case "Lexus":
        console.log("Japanes Cars");
    default:
        console.log("Ummm... don't know that make?");
        break;
}

// Volkswagen, Audi, BMW - German Cars
// Mazda, Toyota, Lexus - Japanese Cars
// Mini, Aston Martin, Rolls-Royce - British

// Create a switch case that shows the country of origin for the car chosen
// if Mazda is the option, say Japanese Car, if Mini, say British?