class Vechicle {
    constructor(colour, make, year, lights) {
        this.colour = colour
        this.make = make
        this.year = year
        this.lights = lights
    }

    honk_horn() {
        if (this.lights == true) {
            console.log("Your lights are on so I am honking my horn")
        }
        else {
            console.log("Your lights are off there is no need for me to honk")
        }
    }
}

const car = new Vechicle("red", "honda", 2014, true)
car.honk_horn()

class Truck extends Vechicle {
    constructor(colour, make, year, lights, name) {
        super(colour, make, year, lights)
        this.name = name
    }

    popWheelie() {
        console.log("This is dangerous.")
    }
}

const truck = new Truck("green", "Volvo", 2020, true, "Betsy")
console.log(truck.name)