import sys
import requests
from local import CLIENT_ID, CLIENT_SECRET


class PluggyAPI:
    BASE_URL = "https://api.pluggy.ai/"
    BASE_HEADERS = {"accept": "application/json", "content-type": "application/json"}

    def __init__(self) -> None:
        self.api_key = str()
        self.headers = self.BASE_HEADERS

    def _auth(self) -> bool:
        if self.api_key:
            return True

        payload = {"clientId": CLIENT_ID, "clientSecret": CLIENT_SECRET}
        try:
            url = self.BASE_URL + "auth"
            response = requests.post(url, json=payload, headers=self.headers)
            self.api_key = response.json()["apiKey"]
            self.headers = self.BASE_HEADERS | {"X-API-KEY": self.api_key}
            return True

        except Exception as e:
            print(e)
            return False

    def call(
        self,
        endpoint: str,
        query_params: dict = {},
        payload: dict = {},
        method: str = "GET",
    ):
        if not self._auth():
            sys.exit("Authentication failed!")

        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, params=query_params, json=payload
        )
        response.raise_for_status()
        return response.json()

    ################ Endpoints ################

    @property
    def accounts(self):
        from pluggy.accounts import AccountsAPI

        return AccountsAPI()

    @property
    def items(self):
        from pluggy.items import ItemsAPI

        return ItemsAPI()

    @property
    def connectors(self):
        from pluggy.connectors import ConnectorsAPI

        return ConnectorsAPI()

    @property
    def transactions(self):
        from pluggy.transactions import TransactionsAPI

        return TransactionsAPI()
