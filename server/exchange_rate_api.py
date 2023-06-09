import requests


class ExchangeApiRequest:

    def __init__(self, base_url):
        self.base_url = base_url

    def exchange(self, from_currency, to_currency, amount):
        endpoint = f"/convert?from={from_currency}&to={to_currency}&amount={amount}"
        url = self.base_url + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_supported_currencies(self):
        endpoint = f"/symbols"
        url = self.base_url + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None