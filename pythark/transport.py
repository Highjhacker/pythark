from .api import API


class Transport:
    """
    Operations for Transports.
    """
    def __init__(self):
        self.api = API()

    def get_peers(self):
        """ Get a list of peers.

        :return:
        """
        resp = self.api.get("peer/list")
        return resp.json()

    def get_common_blocks(self, ids):
        """ Get a list of blocks by ids

        :param ids: List of Block ids.
        :return:
        """
        resp = self.api.get("peer/blocks/common", ids=ids)
        return resp.json()

    def get_blocks(self, address):
        """ Get all blocks.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.api.get("peer/blocks", address=address)
        return resp.json()

    def get_block(self, address):
        # Doesn't work, even the curl from Swagger, need to be checked.
        """ Get a single block.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.api.get("peer/block", address=address)
        return resp.json()

    def get_transactions(self):
        """ Get a list of transactions.

        :return:
        """
        resp = self.api.get("peer/transactions")
        return resp.json()

    def post_transaction(self):
        """ Post a new transaction.

        :return:
        """
        print("Not yet implemented.")

    def get_transactions_from_ids(self, ids):
        """ Get a list of transactions by ids.

        :param ids: A list of valid Transaction id
        :return:
        """
        resp = self.api.get("peer/transactionsFromIds", ids=ids)
        return resp.json()

    def get_height(self):
        """ Get the blockchain height.

        :return:
        """
        resp = self.api.get("peer/height")
        return resp.json()

    def get_status(self):
        """ Get the blockchain status.

        :return:
        """
        resp = self.api.get("peer/status")
        return resp.json()
