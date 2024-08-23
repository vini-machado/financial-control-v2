from typing import Optional
from pluggy.api import PluggyAPI


class AccountsAPI(PluggyAPI):
    BASE_ENDPOINT = "accounts"

    def __init__(self) -> None:
        super().__init__()

    def list(self, item_id: str, type: Optional[str] = None):
        query_params = {"itemId": item_id, "type": type}
        return self.call(endpoint=self.BASE_ENDPOINT, query_params=query_params)

    def retrieve(self, account_id: int):
        endpoint = f"{self.BASE_ENDPOINT}/{account_id}"
        return self.call(endpoint=endpoint)
