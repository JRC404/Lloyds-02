my_age = 95

if my_age < 18:
    print("You are not allowed in the club.")
elif my_age <= 23:
    print("You are eligible for the Young Person discount.")
elif my_age <= 60:
    print("Full price as you are middle aged.")
elif my_age <= 65:
    print("Senior discount applied for you.")
elif my_age <= 100:
    print("You get in for free. Well done.")
else:
    print("You are too old. Sorreh.")