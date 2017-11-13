import requests

BASE_URL = "https://api.arknode.net/"


class API:
    """
    Class allowing us to interact with the API.
    """
    def get(self, endpoint, **kwargs):
        """ Do a HTTP get request to a specified endpoint (with optionnal parameters).

        :param endpoint: The endpoint we want to reach.
        :param kwargs: Optionnal parameters of the query.
        :return: Request response if HTTP code is equal to 200.
        """
        headers = {
            "nethash": "6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988",
            "version": "1.0.1",
            "port": "4001"
        }
        payload = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        r = requests.get("{0}{1}".format(BASE_URL, endpoint), headers=headers, params=payload)
        if r.status_code == 200:
            return r
        else:
            print("Error")
