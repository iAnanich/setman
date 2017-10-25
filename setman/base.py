import types

from ._abc import AbstractSettingsMaster
from .provider._abc import Provider
from .storage._abc import Storage


class SettingsMaster(AbstractSettingsMaster):

    def __init__(self, providers: types.Tuple(Provider, ...), storage: Storage):
        self._providers = tuple(providers)
        self._storage = storage

    def normalize_name(self, name: str):
        # FIXME: write as needed
        return name

    def list_denormalized_names(self, name: str):
        # FIXME: write as needed
        return [name]

    def get(self, name: str):
        # FIXME: split into smaller methods
        denormalized_names = self.list_denormalized_names(name)
        for provider in self._providers:
            for dn_name in denormalized_names:
                if provider.has(dn_name):
                    return provider.get(name)
