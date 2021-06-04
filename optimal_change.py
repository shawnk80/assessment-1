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
# NOTE: I noticed rounding errors in floating point % floating point
# so amount_owed and amount_paid are *100 so calculations are in integers

def determine_change(amount_owed, amount_paid):
    # these amounts are all *100 from monetary amounts and represent
    # the correspoding currency amounts in order
    denomination_list = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
    change = (amount_paid - amount_owed) * 100
    #this store the change amount broken down by denomination
    change_list = []
    # case were no change is owed
    if change == 0:
        return []
    
    # case where more money is owed
    if change < 0:
        return None

    # case where change is owed, check the amount of each
    # of each denomination owed and add it to change_list
    for index, amount in enumerate(denomination_list):
        number_of_denom = change // amount
        change_list.append(number_of_denom)
        change -= number_of_denom * amount

    return change_list


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