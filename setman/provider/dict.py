from ._abc import Provider


class DictProvider(Provider):

    def __init__(self, dictionary: dict):
        self._dictionary = dictionary

    def get(self, name: str):
        return self._dictionary[name]
