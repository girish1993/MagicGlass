from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractGlassFactory(ABC):

    @abstractmethod
    def setup_glass_stack(self):
        pass

    @abstractmethod
    def pour_water(self):
        pass
