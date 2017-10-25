from ._abc import Storage


class DictStorage(Storage):

    def __init__(self):
        self._dictionary = {}

    def has(self, name: str) -> bool:
        return name in self._dictionary.keys()

    def set(self, name: str, value):
        self._dictionary[name] = value

    def get(self, name: str):
        return self._dictionary[name]
