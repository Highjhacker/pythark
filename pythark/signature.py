from .api import API


class Signature:
    """
    Operations for Signatures.
    """
    def __init__(self):
        self.api = API()

    def get_signature_fee(self):
        """ Get the fee for a signature.

        :return:
        """
        resp = self.api.get("api/signatures/fee")
        return resp.json()

    def get_address_signature_fee(self, address):
        """ Get the fee for a signature on a specified address.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.api.get("api/signatures/fee", address=address)
        return resp.json()
