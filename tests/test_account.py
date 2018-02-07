import unittest
from pythark import Account


class TestAccount(unittest.TestCase):
    def test_getBalance(self):
        account = Account()
        resp = account.get_balance("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9")
        self.assertEqual(resp["success"], True)

    def test_getBalanceDevNetwork(self):
        account = Account("dev")
        resp = account.get_balance("DU8i1HWoaaatLKzoA9FJPvX34FdNPzFkYr")
        self.assertEqual(resp["success"], True)

    def test_getBalanceKapuMainNetwork(self):
        account = Account("kapu")
        resp = account.get_balance("KUQc9hNoG4o81t1gwkYTapPqJrxp8Zxf9Y")
        self.assertEqual(resp["success"], True)

    def test_getPublicKey(self):
        account = Account()
        resp = account.get_public_key("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9")
        self.assertEqual(resp["success"], True)

    def test_get_delegate_fee(self):
        account = Account()
        resp = account.get_delegate_fee()
        self.assertEqual(resp["success"], True)

    def test_get_delegates(self):
        account = Account()
        resp = account.get_delegates("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9", limit=10)
        self.assertEqual(resp["success"], True)

    def test_get_accounts(self):
        account = Account()
        resp = account.get_accounts("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9")
        self.assertEqual(resp["success"], True)

    def test_get_top_accounts(self):
        account = Account()
        resp = account.get_top_accounts(limit=10)
        self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()