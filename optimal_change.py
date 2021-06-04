# Input to optimal change is two numbers AMOUNT_PAID and AMOUNT_OWED
# Output is a string stating the optimal change (fewest number of bills and coins)
# OPTIMAL_CHANGE calls two sub functions DETERMINE_CHANGE and PRINT_CHANGE


def optimal_change(amount_owed, amount_paid):
    # verify both inputs are type NUMBER
    # if type(amount_owed) != "int" or type(amount_owed) != "float" or type(amount_paid) != "int" or type(amount_paid) != "float":
    #     return "Invalid inputs - non-number passed to function"
 
    # verify both inputs are greater than zero
    if amount_owed < 0 or amount_paid < 0:
        return "Invalid inputs - amount less than zero."

    optimal_change_list = determine_change(amount_owed, amount_paid)

    optimal_change_str = print_change(optimal_change_list)
    
    return optimal_change_str

# DETERMINE_CHANGE returns a list of OPTIMAL_CHANGE with each element in
# [DENOMINATION, AMOUNT] format
# If no change is DUE (AMOUNT_PAID = AMOUNT_OWED) it returns []
# IF AMOUNT_PAID < AMOUNT_OWED it returns None

def determine_change(amount_owed, amount_paid):
    # case were no change is owed
    if amount_paid == amount_owed:
        return []
    
    # case where more money is owed
    if amount_paid < amount_owed:
        return None

    return []


# PRINT_CHANGE takes an array of elements format [DENOMINATION, AMOUNT]
# and returns a string CHANGE_STR stating the optimal change
# if no change is due it returns "We're even steven."
# if money is still owed (IF AMOUNT_PAID < AMOUNT_OWED) it returns 
# "You owe more money."

def print_change(change_list):
    
    # case where no change due
    if change_list == []:
        return "We're even steven."
    
    if change_list == None:
        return "You owe more money."
    
    return ""