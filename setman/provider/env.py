import os

from ._abc import Provider


class EnvironmentProvider(Provider):

    def get(self, name: str):
        value = os.environ.get(name, None)
        if value is None:
            raise KeyError
        return value
