from enum import Enum

class Endpoint(Enum):
    SENTENCE = "sentence"
    CORRECTION = "correction"

class Method(Enum):
    GET = "GET"
    POST = "POST"
