class Adult {
    constructor(name, age, working, height, gender) {
        this.name = name
        this.age = age
        this.working = working
        this.height = height
        this.gender = gender
    }

    work() {
        console.log(`I am working. My name is ${this.name}`)
    }

}

const bob = new Adult("Bob", 57, true, 185, "Male")
// bob will ALWAYS be an instance of the Adult class
// the values can change but Bob the instance will always remain that
// bob = "cheese"
console.log(bob)
// bob.height = 186
// console.log(bob.height)
// bob.work()


class Child extends Adult {
    constructor(name, age, working, height, gender, bottle) {
        super(name, age, working, height, gender)
        this.bottle = bottle
    }

    use_bottle() {
        if (this.bottle == true) {
            console.log("Using bottle")
        }
        else {
            console.log("You don't have a bottle.")
        }
    }
}

// class Baby extends Child {
//     constructor(name, age, working, height, gender, bottle, burb) {
//         super(name, age, working, height, gender, bottle)
//         this.burb = burb
//     }
// }

// const tim = new Baby()

const jimbob = new Child("Jimbob", 16, true, 170, "Male", false)


//TODO: VEHICLE class with your own variables and 2 methods (functions)
//TODO: two inherited classes, that could be car and truck or car and plane with thir own methods too