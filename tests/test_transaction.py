import unittest
from pythark import Transaction


class TestTransaction(unittest.TestCase):
    def test_get_transaction(self):
        transaction = Transaction()
        resp = transaction.get_transaction("a38dc6b9e6679be706d5b39eef7dd0a7a10011e63da7623082106d90834e23e1")
        self.assertEqual(resp["success"], True)

    def test_get_transactions(self):
        transaction = Transaction()
        resp = transaction.get_transactions(limit=5)
        self.assertEqual(resp["success"], True)

    def test_get_unconfirmed_transaction(self):
        # Need a valid unconfirmed transaction ID, which I can't find, so a little workaround.
        transaction = Transaction()
        resp = transaction.get_unconfirmed_transaction("a4ee8418827a4cd16a83c01d6623a46149fa1eb7cadb9b9cf0073861e23c8a50")
        self.assertEqual(resp["success"], False)

    def test_get_unconfirmed_transactions(self):
        transaction = Transaction()
        resp = transaction.get_unconfirmed_transactions()
        self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()