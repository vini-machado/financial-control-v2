from pluggy.api import PluggyAPI


class ConnectorsAPI(PluggyAPI):
    BASE_ENDPOINT = 'connectors'

    def __init__(self) -> None:
        super().__init__()

    def list_connectors(self, **kwargs):
        return self.call(
            endpoint = self.BASE_ENDPOINT,
            query_params = kwargs
        )

    def retrieve(self, connector_id: int, **kwargs):
        endpoint = f'{self.BASE_ENDPOINT}/{connector_id}'
        return self.call(
            endpoint = endpoint,
            query_params = kwargs
        )
    
    def validate(self, connector_id: int, **kwargs):
        endpoint = f'{self.BASE_ENDPOINT}/{connector_id}/validate'
        return self.call(
            endpoint = endpoint,
            method='POST',
            query_params = kwargs
        )