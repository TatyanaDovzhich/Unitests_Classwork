import unittest
import account


class Test_Account(unittest.TestCase):
    def test_add_money(self):
        self.assertEqual(account.monobank.add_money(100), 1100)

    def test_my_pin(self):
        self.assertEqual(account.monobank.my_pin(), 777)

    def test_my_attempts(self):
        self.assertEqual(account.monobank.attempts, 2)

    def test_count_attempts(self):
        my_attempts_1 = account.monobank.my_attempts(111)
        my_attempts_2 = account.monobank.my_attempts(222)
        self.assertEqual(account.monobank.attempts, 0)

