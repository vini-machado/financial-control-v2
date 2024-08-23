from typing import Optional
from pluggy.api import PluggyAPI


class ConnectorsAPI(PluggyAPI):
    BASE_ENDPOINT = "connectors"

    def __init__(self) -> None:
        super().__init__()

    def list(
        self,
        countries: Optional[list[str]] = None,
        types: Optional[list[str]] = None,
        name: Optional[str] = None,
        sandbox: Optional[bool] = None,
        health_details: Optional[bool] = None,
        is_open_finance: Optional[bool] = None,
        supports_payment_initiation: Optional[bool] = None,
    ):
        query_params = {
            "countries": countries,
            "types": types,
            "name": name,
            "sandbox": sandbox,
            "healthDetails": health_details,
            "isOpenFinance": is_open_finance,
            "supportsPaymentInitiation": supports_payment_initiation,
        }
        return self.call(endpoint=self.BASE_ENDPOINT, query_params=query_params)

    def retrieve(self, connector_id: int, health_details: Optional[bool] = None):
        endpoint = f"{self.BASE_ENDPOINT}/{connector_id}"

        query_params = {
            "healthDetails": health_details,
        }
        return self.call(endpoint=endpoint, query_params=query_params)

    def validate(self, connector_id: int, **kwargs):
        endpoint = f"{self.BASE_ENDPOINT}/{connector_id}/validate"
        return self.call(endpoint=endpoint, method="POST", query_params=kwargs)
