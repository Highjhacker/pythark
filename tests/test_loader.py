import unittest
from pythark import Loader


class TestLoader(unittest.TestCase):
    def test_get_status(self):
        loader = Loader()
        resp = loader.get_status()
        self.assertEqual(resp["success"], True)

    def test_get_sync(self):
        loader = Loader()
        resp = loader.get_sync()
        self.assertEqual(resp["success"], True)

    def test_autoconfigure(self):
        loader = Loader()
        resp = loader.autoconfigure()
        self.assertEqual(resp["success"], True)

if __name__ == '__main__':
    unittest.main()