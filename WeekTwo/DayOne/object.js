// Person is a terrible variable name
const Jacob = {
    name: "Jacob",
    age: 57,
    location: "Manchester",
    employer: "Firebrand",

    birthday() {
        this.age++;
    },

    relocate() {
        this.location = "London"
    }
}

Jacob.birthday();
Jacob.birthday();
console.log(Jacob.age);
console.log(Jacob.employer);
console.log(Jacob.location);

const Dave = {
    name: "Dave",
    age: 60,
    location: "Chester",
    employer: "Unemployed",

    birthday() {
        this.age++;
    },

    relocate() {
        this.location = "London";
    }
}
if (60 > 59){
// if(Dave.age > Jacob.age) {
    console.log("Dave is older.")
}