from client import ApiClient
from libraries.api_functions.API_Typicode_Functions import TypiCodeAPI

class NG_Api(object):
    def __init__(self, api_client: ApiClient):
        self.client = api_client
        self.typicode = TypiCodeAPI(api_client)
