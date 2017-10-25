import abc


class AbstractSettingsMaster(abc.ABC):

    @abc.abstractmethod
    def get(self, name: str):
        pass

    @abc.abstractmethod
    def normalize_name(self, name: str) -> str:
        pass

    @abc.abstractmethod
    def list_denormalized_names(self, name: str) -> list:
        pass
