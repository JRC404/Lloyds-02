favourite_colour = "pink"
# TODO: Create a name check if statement that will say hello to the person
# TODO: 1 if, 10 elif, 1 else
if(favourite_colour == "purple"):
    print("Nice colour choice. Purple is cool.")
    favourite_colour = "blue"

elif(favourite_colour == "red"):
    print("Red is bold. Avoid the bulls.")
    favourite_colour = "yellow"

elif(favourite_colour == "green"):
    print("Green is christmassy... It's almost Christmas. Wear it.")
    favourite_colour = "pink"

elif(favourite_colour == "orange"):
    print("The best colour. Great choice.")
    favourite_colour = "maroon"

else: # any condition that isn't the above... use the else
    print("I don't have that colour stored.")

print(favourite_colour)

# expectation?

# elif(favourite_colour = "orange"): invalid syntax
# single = means make the left equal to the right
# that isn't a condition... that's assignment

my_name = "Bob"

if(my_name == "Bob"):
    print("Ello, Bob")
elif(my_name == "Steve"):
    print("Ello.")
elif(my_name == "Ryan"):
    print("Ello.")
elif(my_name == "Dave"):
    print("Ello.")
elif(my_name == "Alan"):
    print("Ello.")
elif(my_name == "Andy"):
    print("Ello.")
elif(my_name == "Richard" or my_name == "Andy" or my_name == "Dave"):
    print("Ello.")
elif(my_name == "Susan"):
    print("Ello.")
else:
    print("Oh. Get out of my house.")