import requests
from django.conf import settings


class ApproversAPI:
    def __init__(self):
        self.url = settings.APPROVERS_API_URL
        self.client = requests.session()
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }

    def get_approvers(self):
        try:
            return self.client.get(self.url, headers=self.headers)
        except Exception as error:
            raise error


approvers_api_wrapper = ApproversAPI()
