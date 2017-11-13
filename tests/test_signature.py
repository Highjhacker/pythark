import unittest
from pythark import Signature


class TestSignature(unittest.TestCase):
    def test_get_signature_fee(self):
        signature = Signature()
        resp = signature.get_signature_fee()
        self.assertEqual(resp["success"], True)

    def test_get_address_signature_fee(self):
        signature = Signature()
        resp = signature.get_address_signature_fee("Aasu14aTs9ipZdy1FMv7ay1Vqn3jPskA8t")
        self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()