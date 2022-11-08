# politicians.py

class Politician:
    def __init__(self, name, constituency, party, ability_to_lie):
        self.name = name
        self.constituency = constituency
        self.party = party
        self.ability_to_lie = ability_to_lie


michael = Politician("Michael", "A place", "Conservatives", True)
print(michael.name)

## create a class and use the () to say which parent class we are taking from
class PrimeMinister(Politician):
    def __init__(self, name, constituency, party, ability_to_lie, more_power):
        super().__init__(name, constituency, party, ability_to_lie)
        # super takes the values from Politician and allows PrimeMinister to use them
        self.more_power = more_power

    def general_election(self):
        print(f"I am {self.name} and I call a General Election")

  

boris = Politician("Boris", "Uxbridge", "Conservatives", True)
rishi = PrimeMinister("Rishi", "Richmond", "Conservatives", True, True)

boris.name # name, party, constituency, ability_to_lie
rishi.name # name, party, constituency, ability_to_lie, more_power and general_election()

rishi.general_election()

# Chancellor -> know_maths and budget()

##? variables: name, constituency, party, ability_to_lie, know_maths
## methods: budget() -> I am name and I am presenting the budget

## variables go in the init method
## methods go below the init method

class Chancellor(Politician):
    def __init__(self, name, constituency, party, ability_to_lie, know_maths):
        super().__init__(name, constituency, party, ability_to_lie)
        self.know_maths = know_maths

    def budget(self):
         print(f"I am {self.name} and I am presenting the budget")

jeremy = Chancellor("Jeremy", "South West Surrey", "Conservatives", True, True)

jeremy.budget()
