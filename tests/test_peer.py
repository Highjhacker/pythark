import unittest
from pythark import Peer


class TestPeer(unittest.TestCase):
    def test_get_peer(self):
        peer = Peer()
        resp = peer.get_peer("45.76.30.14", 4001)
        self.assertEqual(resp["success"], True)

    def test_get_peers(self):
        peer = Peer()
        resp = peer.get_peers()
        self.assertEqual(resp["success"], True)

    def test_get_peer_version(self):
        peer = Peer()
        resp = peer.get_peer_version()
        self.assertEqual(resp["success"], True)


if __name__ == '__main__':
    unittest.main()