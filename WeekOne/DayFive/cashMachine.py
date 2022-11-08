# cashMachine.py

## variables
user_balance = 1000
user_pin = "1234"
# user_input will be taken shortly
withdrawl_amount = 0
deposit_amount = 0

# Check Pin function
def check_pin():
    user_input = input("Enter your pin:\n")

    # user_input = user_pin # DELETE THIS LINE!
    if user_input == user_pin:
        options() # called the options function
    else:
        print("Wrong pin, buddy.")

def options():
    user_input = input("Which option would you like to select?\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n")

    if user_input == "1": # we are going to add another option to this
        check_balance() 
    elif user_input == "2":
        withdraw()
    elif user_input == "3":
        print("Deposit cash")
    else: 
        print("Wrong choice. Go away.")

# Check Balance Function
def check_balance():
    print(f"Your balance is £{user_balance}")
    options()

def withdraw():
    global user_balance
    withdrawl_amount = int(input("How much would you like to withdraw?\n"))
    user_balance -= withdrawl_amount # local variable referenced before assignment
    print(f"Your new balance is £{user_balance}")
    options()

def deposit():
    pass
    # access the global user_balance
    # take deposit amount
    # make user_balance equal to itself plus the amount deposited
    # print the balance
    # call options again

check_pin()