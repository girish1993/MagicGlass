import logging as LOGGER
from interfaces.abstractGlassFactory import AbstractGlassFactory
from entity.glass import Glass


class GlassFactory(AbstractGlassFactory):

    @staticmethod
    def is_pour_water_valid(poured_water):
        if poured_water <= 0:
            LOGGER.error("Poured Water cannot be negative or 0")
            return False
        return True

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

    def put_glass(self, glass):
        self._all_glasses.append(glass)

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
        try:
            if self.can_setup():
                rows = self.get_rows()
                for i in range(rows):
                    for j in range(0, i + 1):
                        glass = Glass()
                        glass.set_row(i)
                        glass.set_column(j)
                        self.put_glass(glass)
                LOGGER.info("Glass Stack has been setup for use")
            else:
                raise ValueError("Glass Stack cannot be setup with the given row settings")
        except ValueError as v:
            raise ValueError(v)
        except TypeError as e:
            raise TypeError(e)

    def pour_water(self, poured_water):
        try:
            if len(self.get_all_glasses()):
                if self.is_pour_water_valid(poured_water):
                    all_glasses = self.get_all_glasses()
                    index = 0
                    capacity = all_glasses[index].get_capacity()
                    all_glasses[index].set_filled_water(poured_water)
                    # Traversing through the stack from 2 row onwards
                    for row in range(1, self.get_rows()):
                        for col in range(1, row + 1):
                            remaining_water = all_glasses[index].get_filled_water()
                            while remaining_water != 0.0:
                                all_glasses[index].fill_water(remaining_water)
                                if remaining_water >= capacity:
                                    remaining_water -= capacity
                                else:
                                    remaining_water = 0.0

                                left_water_value = all_glasses[index + row].get_filled_water() + (remaining_water / 2)
                                right_water_value = all_glasses[index + row + 1].get_filled_water() + (remaining_water / 2)

                                all_glasses[index + row].set_filled_water(left_water_value)
                                all_glasses[index + row + 1].set_filled_water(right_water_value)
                                index += 1

                    LOGGER.info("Water of volume {} poured".format(poured_water))
                else:
                    raise ValueError("Poured water value cannot be negative")
            else:
                raise Exception("Cannot pour water when the stack hasn't been setup.")
        except ValueError as v:
            raise ValueError(v)
    def find_water_in_glass(self):
        pass
