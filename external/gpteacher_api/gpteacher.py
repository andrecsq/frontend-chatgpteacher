import requests

from os import getenv
from dotenv import load_dotenv

from external.gpteacher_api.constants import Endpoint, Method
from external.objects import CorrectionPayload

class GPTeacher:
    def __init__(self) -> None:
        load_dotenv()
        self.base_url = getenv('BASE_URL')

    def get_sentence(self):

        response_text = self.request_from_api(Endpoint.SENTENCE.value)
        
        return response_text

    def post_correction(self, payload: CorrectionPayload):

        response_text = self.request_from_api(
            Endpoint.CORRECTION.value, 
            method=Method.POST.value, 
            data=payload.model_dump()
        )
        
        return response_text
    

    def request_from_api(self, endpoint: str, method: str = Method.GET.value, data: dict = {}):

        full_url = self.base_url + "/" + endpoint

        response = requests.request(method, full_url, json=data)

        response.raise_for_status()

        return response.text
