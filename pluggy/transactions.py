from typing import Optional
from pluggy.api import PluggyAPI


class TransactionsAPI(PluggyAPI):
    BASE_ENDPOINT = "transactions"

    def __init__(self) -> None:
        super().__init__()

    def list(
        self,
        account_id: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page_size: int = 20,
        page: int = 1,
    ):
        # TODO: check `from_date` and `to_date` format. yyyy-mm-dd
        query_params = {
            "accountId": account_id,
            "from": from_date,
            "to": to_date,
            "pageSize": page_size,
            "page": page,
        }
        return self.call(endpoint=self.BASE_ENDPOINT, query_params=query_params)
