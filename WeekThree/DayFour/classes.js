class Person {
    constructor(name, location, employer, drivingLicense) {
        this.name = name;
        this.location = location;
        this.employer = employer;
        this.drivingLicense = drivingLicense;
        this.favouriteTeam = "Leeds United Football Club";
        this.age = 0;
    }

    // speak method that simply logged "Hello" to the console
    speak() {
        console.log(`Hello, I am ${this.name}`);
    }

    birthday() {
        this.age++;
        console.log(`I am ${this.age} years old.`);
    }

    moveToLondon() {
        if (this.location == "London") {
            console.log("Why are you trying to move, you idiot?")
        } else {
            this.location = "London";
        }
    }
}

//? Please have a condition that checks if the location is london... if it is, say "why would you want to move to london, if you live in london, stupid?"... else... move them to london!

// TODO: Please create a vehicle class with 3 constructor values and 1 defined value: like this.favouriteTeam = "Leeds";
// TODO: 2 of the values = colour and speed
// TODO: Have 3 methods: honk, changeColour, speedLimit
// TODO: In the speedLimit method, let me know the road we are on...
// TODO: If speed is 30 = normal road, 60 = Country road, 70 = Motorway

const bob = new Person("Bob", "Leeds", "LUFC", true);


console.log(bob.name)


console.log(bob.favouriteTeam)

bob.speak()
bob.birthday()
bob.birthday()
bob.birthday()

console.log(bob.location)
bob.moveToLondon()
console.log(bob.location)



// DO NOT CREATE STANDALONE OBJECTS LIKE BELOW IF THEY HAVE THE SAME TRAITS. USE A CLASS, SILLY.

const myObject = {
    name: "Jehcub",
    location: "Manchesta",
    employer: "Firebrand Training Limited",
    drivingLicense: true
}

const myOtherObject = {
    name: "Steve",
    location: "Manchesta",
    employer: "Firebrand Training Limited",
    drivingLicense: true
}

const myOtherOtherObject = {
    name: "Billy",
    location: "Manchesta",
    employer: "Firebrand Training Limited",
    drivingLicense: true
}
const myOtherOtherOtherObject = {
    name: "Bob",
    location: "Manchesta",
    employer: "Firebrand Training Limited",
    drivingLicense: true
}