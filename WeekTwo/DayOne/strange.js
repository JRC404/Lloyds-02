let value = "10";
let number = 50;
let cheese = "cheese"

console.log(value - number); // -40
console.log(value * number); // 500
console.log(value / number); // 0.2
console.log(value + number); // "1050"

console.log(number - value); // 40
console.log(number * value); // 500
console.log(number / value); // 5
console.log(number + value); // "5010"

console.log(cheese + number); // error? nope. cheese50
console.log(cheese - number); // NaN (Not A Number) - no maths to be done here
console.log(cheese + number); // error? nope. cheese50

if(0.2 + 0.1 == 0.3) {
    console.log("you are correct")
}
else {
    console.log("Dummy.")
}

console.log(0.2 + 0.1); // 