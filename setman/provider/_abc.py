import abc


class Provider(abc.ABC):

    @abc.abstractmethod
    def get(self, name: str):
        pass
