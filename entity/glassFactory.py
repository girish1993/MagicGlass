import logging as LOGGER
from interfaces.abstractGlassFactory import AbstractGlassFactory


class GlassFactory(AbstractGlassFactory):

    def __init__(self):
        self._rows = 0
        self._poured_water = 0
        self._all_glasses = []

    def get_rows(self):
        return self._rows

    def set_rows(self, rows):
        self._rows = rows

    def get_poured_water(self):
        return self._poured_water

    def set_poured_water(self, poured_water):
        self._poured_water = poured_water

    def get_all_glasses(self):
        return self._all_glasses

    def can_setup(self):
        can_setup = True
        try:
            if type(self.get_rows()) is not int:
                LOGGER.error("Rows should be of type INT only")
                raise TypeError("Rows should be of type INT only")
            if self.get_rows() <= 0 or self.get_rows() > 10:
                LOGGER.error("Rows cannot be negative and cannot be more than 10")
                can_setup = False
            return can_setup
        except TypeError as e:
            raise TypeError(e)

    def setup_glass_stack(self):
        pass

    def pour_water(self):
        pass

    def find_water_in_glass(self):
        pass
