from interfaces.abstractGlass import AbstractGlass


class Glass(AbstractGlass):

    def __init__(self):
        self._row = 0
        self._column = 0
        self._is_full = False
        self._capacity = 250
        self._filled_water = 0

    def get_row(self):
        return self._row

    def set_row(self, row):
        self._row = row

    def get_column(self):
        return self._column

    def set_column(self, column):
        self._column = column

    def get_is_full(self):
        return self._is_full

    def set_is_full(self, is_full):
        self._is_full = is_full

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_filled_water(self):
        return self._filled_water

    def set_filled_water(self, filled_water):
        self._filled_water = filled_water

    def reset(self):
        pass

    def fill_water(self):
        pass
