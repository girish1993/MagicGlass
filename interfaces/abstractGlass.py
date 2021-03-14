from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractGlass(ABC):
    """
    This abstract class sets up the minimal operations one could perform with regards to a GLASS. We are looking at
    basically 2 operations:
    <ol>
        <li>Filling water into the glass</li>
        <li>Resetting(Emptying) the glass to its default state</li>
    </ol>
    """

    @abstractmethod
    def fill_water(self, water_volume):
        """
        The action of filling water into the glass
        :param water_volume: number indicating the volume of the water being poured into the glas
        :type water_volume: int
        :return: None
        :rtype: None
        """
        pass

    @abstractmethod
    def reset(self):
        """
        The action of resetting the state of the glass to the defaults
        :return: None
        :rtype: None
        """
        pass
