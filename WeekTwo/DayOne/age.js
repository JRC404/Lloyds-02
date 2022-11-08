myAge = 50
if (myAge < 18) {
    console.log("You are not allowed in the club.")
}
else if (myAge <= 23){
    console.log("You are eligible for the Young Person discount.")
}
else if (myAge <= 60){
    console.log("Full price as you are middle aged.")
}
else if (myAge <= 65){
    console.log("Senior discount applied for you.")
}
else if (myAge <= 100){
    console.log("You get in for free. Well done.")
}
else {
    console.log("You are too old. Sorreh.")
}