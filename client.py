import requests

class CmfClient():

    def __init__(self):
        self.host = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/'
        self.params = {
            'apikey': 'b25f76997da7f23f89b73315b32dbc0a9d91a177',
            'formato': 'json'
        }

    def join_path(self, path: str) -> str:
        return f'{self.host}{path}'

    def get(self, path: str, params: dict=None) -> tuple[bool, requests.Response]:
        params_final = params + self.params if params else self.params
        response = requests.get(url=self.join_path(path), params=params_final)
        return response.ok, response.json()
