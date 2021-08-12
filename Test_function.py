import unittest
import functions as fun

import functions
import Tax_calculator as tc

class MyTestCase(unittest.TestCase):
    def test_something(self):
        """test net pay"""
        net_pay = tc.calc_tax(100, 10)
        self.assertEqual(90, net_pay)


def test_tax_net_pay_45(self):
    """test tax with the bthe age bracket of less than 46"""
    net_pay_age = tc.total_calc_tax(100, 45)
    self.assertEqual(91, net_pay_age)


def test_tax_net_pay_65(self):
    """test tax with the bthe age bracket of greater than 45 less than 66 years"""
    net_pay_age = tc.total_calc_tax(100, 65)
    self.assertEqual(95, net_pay_age)


def test_tax_net_pay_65(self):
    """test tax with the between age bracket of greater than 65 years"""
    net_pay_age = tc.total_calc_tax(100, 66)
    self.assertEqual(97, net_pay_age)


if __name__ == '__main__':
    unittest.main()
