# try.py

hogwart_houses = {"Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"}

try:
    hogwart_houses.remove("Random House")
except KeyError:
    print("Looks like a Key Error")
except:
    print("An error has occured.")

try:
    print(my_age)
except NameError:
    print("The variable is not defined.")
except:
    print("Something went wrong.")

print("Hello World")