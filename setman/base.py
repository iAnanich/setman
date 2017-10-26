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

        normalized_name = self.normalize_name(name)

        if self._storage.has(normalized_name):
            return self._storage.get(name)

        denormalized_names = self.list_denormalized_names(normalized_name)
        for provider in self._providers:
            for dn_name in denormalized_names:
                try:
                    return provider.get(denormalized_names)
                except KeyError:
                    pass
                except Exception as exc:
                    raise RuntimeError from exc
