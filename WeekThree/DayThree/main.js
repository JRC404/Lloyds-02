// let and var -> they allow us to declare variables
// const -> constant

for (let i = 0; i < 10; i++) {
    console.log(i)
}

console.log(`Value of i: ${i}`) // undefined

for (var i = 0; i < 100; i++) {
    console.log(i)
}

console.log(`Value of i: ${i}`) // 100


let myNumber = 10; // global scope variable

const myFunction = () => {
    console.log(myNumber); // 
}

console.log(myNumber); // 10 because of line 17

const mySecondFunction = () => {
    let myNumber = 50;
    console.log(myNumber); // we cannot access the local scoped variable: myNumber
}

console.log(myNumber); // this line can only access GLOBAL variables 

myFunction();
mySecondFunction();