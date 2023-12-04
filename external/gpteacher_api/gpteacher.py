import requests

from os import getenv
from dotenv import load_dotenv

from external.gpteacher_api.constants import Endpoint

class GPTeacher:
    def __init__(self) -> None:
        load_dotenv()
        self.base_url = getenv('BASE_URL')

    def get_sentence(self):

        response_text = self.request_from_api(Endpoint.SENTENCE)
        
        return response_text

    def get_correction(self, data: dict):

        response_text = self.request_from_api(Endpoint.CORRECTION, data=data)
        
        return response_text
    

    def request_from_api(self, endpoint: Endpoint, data: dict = {}):

        full_url = self.base_url + "/" + endpoint.value

        print(f"url requested: {full_url}")

        response = requests.get(full_url, json=data)

        response.raise_for_status()

        return response.text
