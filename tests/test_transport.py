import unittest
from pythark import Transport


class TestTransport(unittest.TestCase):
    def test_get_peers(self):
        transport = Transport()
        resp = transport.get_peers()
        self.assertEqual(resp["success"], True)

    def test_get_common_blocks(self):
        transport = Transport()
        resp = transport.get_common_blocks("5807533976636630922, 7191952529633383827")
        self.assertEqual(resp["success"], True)

    def test_get_blocks(self):
        transport = Transport()
        resp = transport.get_blocks("AJbmGnDAx9y91MQCDApyaqZhn6fBvYX9iJ")
        self.assertEqual(resp["success"], True)

    #def test_get_block(self):
    #    # Doesn't work, even the curl from Swagger, need to be checked.
    #    transport = Transport()
    #    resp = transport.get_block("AJbmGnDAx9y91MQCDApyaqZhn6fBvYX9iJ")
    #    self.assertEqual(resp["success"], True)

    def test_get_transactions(self):
        transport = Transport()
        resp = transport.get_transactions()
        self.assertEqual(resp["success"], True)

    #def test_post_new_transaction(self):
    #    print("Not implemented")

    def test_get_transactions_from_ids(self):
        transport = Transport()
        resp = transport.get_transactions_from_ids("e9f1ff96ccaf9ebcadb0e1c0827c606a71a88c258c6a3ec1a880be000996dd25")
        self.assertEqual(resp["success"], True)

    def test_get_height(self):
        transport = Transport()
        resp = transport.get_height()
        self.assertEqual(resp["success"], True)

    def test_get_status(self):
        transport = Transport()
        resp = transport.get_status()
        self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()