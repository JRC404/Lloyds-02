# input.py

first_name = input("What is your name?\n")
# \n puts the input box on a new line
print(f"Your name is {first_name}")

your_age = input("How old are you?\n")
print(f"You are {your_age} years old")

# TODO: Create the age check if statement
# under 18, under 30 young person, under 50 middle aged, under 70 distinguished, else get in for free

your_age = int(your_age)

if your_age < 18:
    print("You are not allowed in.")
elif your_age < 30:
    print("Under 30 discount")
elif your_age < 50:
    print("Middle aged.")
elif your_age < 70:
    print("Distinguished.")
else:
    print("Come in for free.")

#! TypeError: '<' not supported between instances of 'str' and 'int'


# if first_name == "Jehcub":
#     print(f"Hello, {first_name}")
# elif first_name == "Jacob":
#     print(f"Hello, {first_name}")
# else:
#     print("COLON.")