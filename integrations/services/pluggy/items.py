import re
from pluggy.api import PluggyAPI


class ItemsAPI(PluggyAPI):
    BASE_ENDPOINT = "items"

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _validate_user_data(user_data: dict, credentials_validator: list[dict]) -> None:
        for field in credentials_validator:
            name = field["name"]
            validation_pattern = field["validation"]
            validation_message = field["validationMessage"]
            value = user_data.get(name, "")

            if not field.get("optional") and not value:
                raise ValueError(f"{field['label']} é obrigatório.")

            if value:
                if not re.match(validation_pattern, value):
                    raise ValueError(validation_message)

    def create_items(self, connector_id: int, credentials: dict):
        credentials_validator: list[dict] = self.connectors.retrieve(connector_id).get(
            "credentials", {}
        )

        self._validate_user_data(
            user_data=credentials, credentials_validator=credentials_validator
        )

        payload = {"connectorId": connector_id, "parameters": credentials}

        return self.call(endpoint=self.BASE_ENDPOINT, method="POST", payload=payload)

    def retrieve(self, item_id: str = None):
        endpoint = f"{self.BASE_ENDPOINT}/{item_id}"
        return self.call(endpoint=endpoint)

    def send_mfa(self, item_id: str, mfa_token):
        endpoint = f"{self.BASE_ENDPOINT}/{item_id}/mfa"
        payload = {"token": mfa_token}
        return self.call(endpoint=endpoint, method="POST", payload=payload)
