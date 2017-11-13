import unittest
from pythark import Block


class TestBlock(unittest.TestCase):
    def test_get_block(self):
        block = Block()
        resp = block.get_block("570934191207974498")
        self.assertEqual(resp["success"], True)

    def test_get_blocks(self):
        block = Block()
        resp = block.get_blocks(limit=5)
        self.assertEqual(resp["success"], True)

    def test_get_height(self):
        block = Block()
        resp = block.get_height()
        self.assertEqual(resp["success"], True)

    def test_get_epoch(self):
        block = Block()
        resp = block.get_epoch()
        self.assertEqual(resp["success"], True)

    def test_get_nethash(self):
        block = Block()
        resp = block.get_nethash()
        self.assertEqual(resp["success"], True)

    def test_get_fee(self):
        block = Block()
        resp = block.get_fee()
        self.assertEqual(resp["success"], True)

    def test_get_fees(self):
        block = Block()
        resp = block.get_fees()
        self.assertEqual(resp["success"], True)

    def test_get_milestone(self):
        block = Block()
        resp = block.get_milestone()
        self.assertEqual(resp["success"], True)

    def test_get_reward(self):
        block = Block()
        resp = block.get_reward()
        self.assertEqual(resp["success"], True)

    def test_get_supply(self):
        block = Block()
        resp = block.get_supply()
        self.assertEqual(resp["success"], True)

    def test_get_status(self):
        block = Block()
        resp = block.get_status()
        self.assertEqual(resp["success"], True)

if __name__ == '__main__':
    unittest.main()