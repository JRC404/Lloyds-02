# Create a function that uses the AND logic. If the first parameter and second are both true, print "True". If they aren't, print "False"

# NB: And(True, False) # Would print False
# NB: And(True, True) # Would print True

# Create a function - DONE
# Take two parameters - DONE
# if first_value and second_value are true... print True
# else... print False

def and_logic(first_value, second_value):
    if first_value == True and second_value == True:
        print("True")
    else: 
        print("False")

and_logic(True, False) # False
and_logic(True, True) # True
and_logic(False, True) # False
and_logic(False, False) # False

def or_logic(day_of_the_week):
    if(day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"):
        print("WooHoo. A call with Jacob. I am so lucky.")
    else: 
        print("Oh. That's a shame. Who will I speak to now?")

or_logic("Monday")
or_logic("Sunday")

# Create a function that takes your age and prints the age in days
# NB: Year is 365 days, no leap years

# Create a function
# Take age as a parameter

def age_to_days(age):
    days = 365 * age
    print(f"{days}")

age_to_days(57)

# Create a function that shows how many points you have scored in Basketball when using 3 points and 2 points.

# NB: points(1, 2) shows 7 as 1 x 3 points and 2 * 2 points
# points(3, 1) shows 11 as 3 x 3 points and 1 x 2 points

def points_scored(three_pointers, two_pointers):
    three_total = three_pointers * 3
    two_total = two_pointers * 2
    full_score = three_total + two_total
    print(f"Three total: {three_total}")
    print(f"Two total: {two_total}")
    print(f"Full score: {full_score}")

points_scored(1, 2)
points_scored(3, 1)
points_scored(30, 12)