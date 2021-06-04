import unittest
from optimal_change import optimal_change

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
    
    


if __name__ == '__main__':
    unittest.main()
