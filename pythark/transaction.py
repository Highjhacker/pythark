from .api import API


class Transaction(API):
    """
    Operations for Transactions.
    """

    def get_transaction(self, id):
        """ Get a single transaction.

        :param id: A valid Transaction id.
        :return:
        """
        resp = self.get("api/transactions/get", id=id)
        return resp.json()

    def get_transactions(self, **kwargs):
        """ Get all transactions.

        :param kwargs: Optionnal parameters. blockId, limit, orderBy, offset, senderPublicKey, vendorField, ownerPublicKey,
        ownerAddress, senderId, recipientId, amount, fee
        :return:
        """
        resp = self.get("api/transactions", **kwargs)
        return resp.json()

    def get_unconfirmed_transaction(self, id):
        """ Get a single unconfirmed transaction.

        :param id: A valid Transaction id.
        :return:
        """
        resp = self.get("api/transactions/unconfirmed/get", id=id)
        return resp.json()

    def get_unconfirmed_transactions(self, **kwargs):
        """ Get all unconfirmed transactions.

        :param kwargs: Optionnal parameters. senderPublicKey, address
        :return:
        """
        resp = self.get("api/transactions/unconfirmed", **kwargs)
        return resp.json()