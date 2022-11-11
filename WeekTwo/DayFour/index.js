const lightSwitch = document.getElementById("lightSwitch");
const headerOne = document.getElementById("headerOne");

document.title = "Bob"

const body = document.body;

let lightOn = true;

const toggle = () => {
    if(lightOn) { // if(lightOn) is the same as if(lightOn == true)
        console.log("Light is on. Turn it off.");
        body.style.backgroundColor = "black";
        body.style.color = "white";
        headerOne.textContent = "Light is off"
        lightOn = false; // turning the light off
    }
    else {
        console.log("Light is off. Turn it on.");
        body.style.backgroundColor = "white";
        body.style.color = "black";
        headerOne.textContent = "Light is on";
        lightOn = true; // turned the light on
    }
}

lightSwitch.addEventListener("click", () => {
    toggle()
})

// toggle() // turns the switch off
// toggle() // turns the switch on
// toggle() // turns the switch off
// toggle() // turns the switch on