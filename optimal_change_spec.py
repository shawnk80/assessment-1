import unittest
from optimal_change import optimal_change
from optimal_change import determine_change
from optimal_change import print_change
from optimal_change import change_string

class OptimalChangeTests(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
