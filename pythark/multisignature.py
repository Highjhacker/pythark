from .api import API


class MultiSignature:
    """
    Operations for MultiSignatures.
    """
    def __init__(self):
        self.api = API()

    def get_pending(self, publicKey):
        """ Get pending multi signatures transactions.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.api.get("api/multisignatures/pending", publicKey=publicKey)
        return resp.json()

    def get_accounts(self, publicKey):
        # TypeError: NetworkError when attempting to fetch resource.
        """ Get a list of accounts.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.api.get("api/multisignatures/accounts", publicKey=publicKey)
        return resp.json()
