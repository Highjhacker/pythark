import requests
import random

BASE_URL = "http://37.59.129.164:4001/" #"https://api.arknode.net/"
BASE_URL_DEV = "http://167.114.29.52:4002/"
FALLBACKS_MAIN_ADDRESSES = []
BASE_URL_KAPUMAIN = "https://walletapi.kapu.one/"
FALLBACKS_DEV_ADDRESSES = []


def populate_fallback(fallback, network):
    from . import Peer
    if network == 'dev':
        p = Peer("dev")
    else:
        p = Peer()
    r = p.get_peers()
    for peer in r["peers"]:
        if peer["delay"] <= 50:
            fallback.append(peer)
    return fallback


def select_random_ip(fallback):
    rand = random.choice(fallback)
    return rand['ip']


class API:
    """
    Class allowing us to interact with the API.
    """
    def __init__(self, network="main"):
        self.network = network

    def get(self, endpoint, **kwargs):
        """ Do a HTTP get request to a specified endpoint (with optionnal parameters).

        :param endpoint: The endpoint we want to reach.
        :param kwargs: Optionnal parameters of the query.
        :return: Request response if HTTP code is equal to 200.
        """
        headers_main = {
            "nethash": "6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988",
            "version": "1.0.1",
            "port": "4001"
        }
        headers_dev = {
            "nethash": "578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23",
            "version": "1.1.1",
            "port": "4002"
        }
        headers_kapu_main = {
            "nethash": "313ea34c8eb705f79e7bc298b788417ff3f7116c9596f5c9875e769ee2f4ede1",
            "version": "0.3.0",
            "port": "9700"
        }
        payload = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        try:
            if self.network == 'main':
                r = requests.get("{0}{1}".format(BASE_URL, endpoint), headers=headers_main, params=payload)
                if r.status_code == 200:
                    return r
            if self.network == 'dev':
                r = requests.get("{0}{1}".format(BASE_URL_DEV, endpoint), headers=headers_dev, params=payload)
                if r.status_code == 200:
                    return r
            if self.network == 'kapu':
                r = requests.get("{0}{1}".format(BASE_URL_KAPUMAIN, endpoint), headers=headers_kapu_main, params=payload)
                if r.status_code == 200:
                    return r
        except requests.exceptions.Timeout:
            if self.network == "dev":
                populate_fallback(FALLBACKS_DEV_ADDRESSES)
                url = select_random_ip(FALLBACKS_DEV_ADDRESSES) + "/"
            else:
                populate_fallback(FALLBACKS_MAIN_ADDRESSES)
                url = select_random_ip(FALLBACKS_MAIN_ADDRESSES) + "/"
            r = requests.get("{0}{1}".format(url, endpoint), headers=headers_dev if self.network == 'dev' else headers_main, params=payload)
            if r.status_code == 200:
                return r

