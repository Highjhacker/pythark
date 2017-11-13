import unittest
from pythark import MultiSignature


class TestMultiSignature(unittest.TestCase):
    def test_get_pending(self):
        multisig = MultiSignature()
        resp = multisig.get_pending("02c7455bebeadde04728441e0f57f82f972155c088252bf7c1365eb0dc84fbf5de")
        self.assertEqual(resp["success"], True)

    #def test_get_accounts(self):
    #    # Throw a TypeError: NetworkError when attempting to fetch resource. even in the Swagger API.
    #    multisig = MultiSignature()
    #    resp = multisig.get_accounts("02ff171adaef486b7db9fc160b28433d20cf43163d56fd28fee72145f0d5219a4b ")
    #    self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()