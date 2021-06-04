import unittest
from optimal_change import optimal_change
from optimal_change import determine_change
from optimal_change import print_change
from optimal_change import change_string
from optimal_change import check_non_zeros

class OptimalChangeTests(unittest.TestCase):

    maxDiff = None

    def test_case_negative_number_input(self):
        output = optimal_change(-1, 1)
        self.assertEqual(output, "Invalid inputs - amount less than zero.")

    # def test_case_non_number_input(self):
    #     output = optimal_change("foo", 1)
    #     print(type("foo"), type(1))
    #     self.assertEqual(output, "Invalid inputs - non-number passed to function")

    def test_case_no_money_owed(self):
        output = optimal_change(4, 4)
        self.assertEqual(output, "We're even steven.")

    def test_case_money_still_owed(self):
        output = optimal_change(6, 4)
        self.assertEqual(output, "You owe more money.")

    def test_case_float_and_int_input(self):
        output = optimal_change(4.0, 4)
        self.assertEqual(output, "We're even steven.")
    
    def test_determine_change(self):
        output = determine_change(100.00, 112.12)
        self.assertEqual(output, [0, 0, 0, 1, 0, 2, 0, 1, 0, 2])
    
    def test_determine_change2(self):
        output = determine_change(62.13, 63)
        self.assertEqual(output, [0, 0, 0, 0, 0, 0, 3, 1, 0, 2])

    def test_change_str(self):
        output = change_string(9, 2)
        self.assertEqual(output, "2 pennies")

    def test_change_str2(self):
        output = change_string(9, 1)
        self.assertEqual(output, "1 penny")

    def test_change_str3(self):
        output = change_string(2, 3)
        self.assertEqual(output, "3 $20 bills")

    def test_change_str4(self):
        output = change_string(2, 1)
        self.assertEqual(output, "1 $20 bill")

    def test_check_non_zero1(self):
        output = check_non_zeros([0, 1, 2, 3, 0])
        self.assertEqual(output, 3)
    
    def test_check_non_zero2(self):
        output = check_non_zeros([0, 0, 0])
        self.assertEqual(output, 0)

    def test_output_change_string(self):
        output = print_change([0, 0, 0, 1, 0, 2, 0, 1, 0, 2], 100.00, 112.12)
        self.assertEqual(output, "The optimal change for an item that costs $100.00 with an amount paid of $112.12 is 1 $10 bill, 2 $1 bills, 1 dime, and 2 pennies.")

    def test_out_change_string2(self):
        output = print_change([0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 10, 20)
        self.assertEqual(output, "The optimal change for an item that costs $10.00 with an amount paid of $20.00 is 1 $10 bill.")

    def test_optimal_change(self):
        output = optimal_change(10, 20)
        self.assertEqual(output, "The optimal change for an item that costs $10.00 with an amount paid of $20.00 is 1 $10 bill.")

    def test_optimal_change2(self):
        output = optimal_change(100, 112.12)
        self.assertEqual(output, "The optimal change for an item that costs $100.00 with an amount paid of $112.12 is 1 $10 bill, 2 $1 bills, 1 dime, and 2 pennies.")
    
    def test_optimal_change3(self):
        output = optimal_change(31.51, 50)
        self.assertEqual(output, "The optimal change for an item that costs $31.51 with an amount paid of $50.00 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_optimal_change4(self):
        output = optimal_change(62.13, 100)
        self.assertEqual(output, "The optimal change for an item that costs $62.13 with an amount paid of $100.00 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")


if __name__ == '__main__':
    unittest.main()
