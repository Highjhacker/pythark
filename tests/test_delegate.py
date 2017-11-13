import unittest
from pythark import Delegate


class TestDelegate(unittest.TestCase):
    def test_get_delegates_count(self):
        delegate = Delegate()
        resp = delegate.get_delegates_count("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9")
        self.assertEqual(resp["success"], True)

    def test_search_delegates(self):
        delegate = Delegate()
        resp = delegate.search_delegates(query="dr", limit=2)
        self.assertEqual(resp["success"], True)

    def test_get_voters(self):
        delegate = Delegate()
        resp = delegate.get_voters("031641ff081b93279b669f7771b3fbe48ade13eadb6d5fd85bdd025655e349f008")
        self.assertEqual(resp["success"], True)

    def test_get_delegate(self):
        delegate = Delegate()
        resp = delegate.get_delegate("jarunik")
        self.assertEqual(resp["success"], True)

    def test_get_delegate_public_key(self):
        delegate = Delegate()
        resp = delegate.get_delegate_publickey("031641ff081b93279b669f7771b3fbe48ade13eadb6d5fd85bdd025655e349f008")
        self.assertEqual(resp["success"], True)

    def test_get_delegates(self):
        delegate = Delegate()
        resp = delegate.get_delegates(limit=5, orderBy="username")
        self.assertEqual(resp["success"], True)

    def test_get_delegate_fee(self):
        delegate = Delegate()
        resp = delegate.get_delegate_fee("Aasu14aTs9ipZdy1FMv7ay1Vqn3jPskA8t")
        self.assertEqual(resp["success"], True)

    def test_get_forged_by_account(self):
        delegate = Delegate()
        resp = delegate.get_forged_by_account("02c7455bebeadde04728441e0f57f82f972155c088252bf7c1365eb0dc84fbf5de")
        self.assertEqual(resp["success"], True)

    def test_get_next_forgers(self):
        delegate = Delegate()
        resp = delegate.get_next_forgers("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9")
        self.assertEqual(resp["success"], True)

if __name__ == '__main__':
    unittest.main()