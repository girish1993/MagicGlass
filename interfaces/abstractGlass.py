from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractGlass(ABC):

    @abstractmethod
    def fill_water(self, water_volume):
        pass

    @abstractmethod
    def reset(self):
        pass
