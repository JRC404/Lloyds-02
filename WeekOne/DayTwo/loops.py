# loops.py

#? while loop

age = 0
# while age is less than 65... run the code below
# the code below is adding 1 to age each time it is ran
while age < 65:
    # is 0 less than 65? Why, yes, yes it is.
    print(f"You are {age} years old")
    age += 1 # birthday!
    # age -= 1 # infinite loop... going the wrong way!!!

# ALWAYS REMEMBER TO INCREMENT OR DECREMENT

logged_in = True

while logged_in == True:
    print("LOGGED IN.")
    logged_in = False
    print("LOGGED OUT. GO HOME.")

# infinite loops require: 'ctrl c' to close the program

#? for loop

banks = ["Lloyds Banking Group", "RBS", "Monzo", "Starling"]
#                   0               1       2         3

banks.append("Santander")

print(banks)

for item in banks:
    print(f"You bank with {item}")
    # item is a name I have chosen. You can choose cheese, if you'd like?

# TODO: Create a numbers list with 10 favourite numbers and use a for loop to display all of the numbers

numbers = [1, 256, 32, 1244, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

# TODO: Create a while loop that counts up to 100
counter = 0

while counter <= 100:
    print(counter)
    counter += 1

# TODO: Create a while loop that counts down to 0

counter = 50

while counter >= 0:
    print(counter)
    counter -= 1