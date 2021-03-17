from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractGlassFactory(ABC):

    @abstractmethod
    def can_setup(self):
        pass

    @abstractmethod
    def setup_glass_stack(self):
        pass

    @abstractmethod
    def pour_water(self, poured_water):
        pass

    @abstractmethod
    def find_water_in_glass(self):
        pass
