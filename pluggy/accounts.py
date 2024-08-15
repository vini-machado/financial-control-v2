from pluggy.api import PluggyAPI


class AccountsAPI(PluggyAPI):
    BASE_ENDPOINT = 'accounts'

    def __init__(self) -> None:
        super().__init__()

    def list_accounts(self, **kwargs):
        return self.call(
            endpoint = self.BASE_ENDPOINT,
            query_params = kwargs
        )

    def retrieve(self, account_id: int, **kwargs):
        endpoint = f'{self.BASE_ENDPOINT}/{account_id}'
        return self.call(
            endpoint = endpoint,
            query_params = kwargs
        )