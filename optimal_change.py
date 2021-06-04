# Input to optimal change is two numbers AMOUNT_PAID and AMOUNT_OWED
# Output is a string stating the optimal change (fewest number of bills and coins)
# OPTIMAL_CHANGE calls two sub functions DETERMINE_CHANGE and PRINT_CHANGE


def optimal_change(amount_owed, amount_paid):

    # verify both inputs are greater than zero

    if amount_owed < 0 or amount_paid < 0:
        return "Invalid inputs - amount less than zero."

    optimal_change_list = determine_change(amount_owed, amount_paid)

    optimal_change_str = print_change(optimal_change_list, amount_owed, amount_paid)
    
    return optimal_change_str

# DETERMINE_CHANGE returns a list of OPTIMAL_CHANGE with each element in
# [DENOMINATION, AMOUNT] format
# If no change is DUE (AMOUNT_PAID = AMOUNT_OWED) it returns []
# IF AMOUNT_PAID < AMOUNT_OWED it returns None
# NOTE: I noticed rounding errors in floating point % floating point
# and floating point +- integer
# so amount_owed and amount_paid are *100 so calculations are strictly in integers

def determine_change(amount_owed, amount_paid):
    # these amounts are all *100 from monetary amounts and represent
    # the correspoding currency amounts in order
    denomination_list = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
    change = int(amount_paid*100) - int(amount_owed*100)

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
        number_of_denom = int(change // amount)
        change_list.append(number_of_denom)
        change -= number_of_denom * amount

    return change_list


# PRINT_CHANGE takes an array of elements format [DENOMINATION, AMOUNT]
# and returns a string CHANGE_STR stating the optimal change
# if no change is due it returns "We're even steven."
# if money is still owed (IF AMOUNT_PAID < AMOUNT_OWED) it returns 
# "You owe more money."
# iterates over the list and appends the correct denomination text
# to the amount owed from CHANGE_LIST for that denomination

def print_change(change_list, amount_owed, amount_paid):
    # format amount_owed and amount_paid so they always show 2 decimal places
    amount_owed = "{:.2f}".format(amount_owed)
    amount_paid = "{:.2f}".format(amount_paid)
    
    # case where no change due
    if change_list == []:
        return "We're even steven."
    
    # case where you owe more money
    if change_list == None:
        return "You owe more money."

    # record the total number of denominations owed
    total_num_denoms_owed = check_non_zeros(change_list)

    output_change_str = f"The optimal change for an item that costs ${amount_owed} with an amount paid of ${amount_paid} is "

    for index, amount in enumerate(change_list):
        if amount > 0:
            # case more than 1 change amounts remain to append
            if check_non_zeros(change_list) > 1:
                output_change_str += change_string(index, amount) + ", "
            # indicate no more change at the current denomination is owed
                change_list[index] = 0
            # case where 1 change denomination remains
            else:
                output_change_str += f"{'and ' if total_num_denoms_owed > 1 else ''}" + change_string(index, amount) + "."
                break

    return output_change_str


# change string takes in two arguments - the DENOMINATION_INDEX and AMOUNT
# denomination indices map to their index in DENOM_STR_LIST
# CHANGE_STRING returns a string of the format f"{amount} {denom_str}?"s"}
def change_string(denomination_index, amount):

    # penny is a special case as the plural of penny is pennies
    denom_str_list = ["$100 bill", "$50 bill", "$20 bill", "$10 bill", "$5 bill", "$1 bill", "quarter", "dime", "nickel", "penn"]
    type_change_owed_str = denom_str_list[denomination_index]

    #check if denomination_index is for a penny
    if type_change_owed_str == "penn":
        return f"{amount} {type_change_owed_str}{'ies' if amount > 1 else 'y'}"

    # return
    return f"{amount} {type_change_owed_str}{'s' if amount > 1 else ''}"


# CHECK_NON_ZEROS takes a number INPUT list and returns the number of non-zero elements
def check_non_zeros(input):

    non_zeros = 0
    for elem in input:
        if elem != 0:
            non_zeros += 1
    
    return non_zeros
