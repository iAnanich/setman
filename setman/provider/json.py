import json

from ._abc import Provider


class JSONProvider(Provider):

    def __init__(self, json_string: str, **kwargs):
        self._original = json_string
        self._decoded = json.loads(json_string, **kwargs)

    def get(self, name):
        return self._decoded[name]
