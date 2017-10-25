import abc


class Storage(abc.ABC):

    @abc.abstractmethod
    def has(self, name: str) -> bool:
        pass

    @abc.abstractmethod
    def get(self, name: str):
        pass

    @abc.abstractmethod
    def set(self, name: str, value):
        pass
