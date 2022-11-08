class Student {
    constructor(studentID, fullName, role) {
        this.studentID = studentID
        this.fullName = fullName
        this.role = role
        this.enrolled = false
    }

    enrol() {
        this.enrolled = true
    }

    expelled() {
        this.enrolled = false
    }

    printDetails() {
        console.log(`Hello, I am ${this.fullName}. My student ID is ${this.studentID}.`)
    }
}

let bob = new Student(1, "Bob Bobbington", "Engineer")
let sally = new Student(2, "Sally Bobbington", "Engineer")
let jimbob = new Student(3, "Jimbob Bobbington", "Developer")
let wallace = new Student(4, "Wallace Bobbington", "Developer")

console.log(bob)
console.log(sally)
console.log(jimbob)
console.log(wallace)

jimbob.enrol() // jimbob is the only one enrolled
console.log(jimbob)

// class Student:
// def __init__(self, student_id, full_name, role, enrolled):
//     self.student_id = student_id
//     self.full_name = full_name
//     self.role = role
//     self.enrolled = enrolled

// def enrol(self):
//     self.enrolled = True

// def expelled(self):
//     self.enrolled = False

// def print_details(self):
//     print(f"Hi, I am {self.full_name}. My Student ID is {self.student_id}. My role at my company is {self.role}.")

class Bunny {
    constructor(name, health, strength, speed, energy) {
        this.name = name
        this.health = health
        this.strength = strength
        this.speed = speed
        this.energy = energy
    }

    sleep() {
        this.energy += 10
    }

    train() {
        this.strength += 10
        this.energy -= 15
    }
}

let buggs = new Bunny("Buggs", 100, 100, 100, 100)
let dylan = new Bunny("Dylan", 20, 20, 20, 20)

if(buggs.strength > dylan.strength)
{
    console.log("Buggs wins")
}