from utils.api_client import ApiClient
from apis import *


class VenmoApi(object):

    def __init__(self, access_token: str):
        """
        VenmoAPI Client
        :param access_token: <str> Need access_token to work with the API.
        """
        super().__init__()
        self.__access_token = access_token
        self.__api_client = ApiClient(access_token=access_token)
        self.user = UserApi(self.__api_client)
        self.payment = PaymentApi(self.__api_client)

    @staticmethod
    def get_access_token(username: str, password: str, device_id: str = None) -> str:
        """
        Log in using your credentials and get an access_token to use in the API
        :param username: <str> Can be username, phone number (without +1) or email address.
        :param password: <str> Account's password
        :param device_id: <str> [optional] A valid device-id.

        :return: <str> access_token
        """
        authn_api = AuthenticationApi(api_client=ApiClient(), device_id=device_id)
        return authn_api.login_using_credentials(username=username, password=password)

    @staticmethod
    def log_out(access_token) -> bool:
        """
        Revoke your access_token. Log out, in other words.
        :param access_token:
        :return: <bool>
        """
        return AuthenticationApi.log_out(access_token=access_token)
