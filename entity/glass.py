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

    def is_valid_row_and_column(self):
        """
        Method to check the validity of the row and column values.
        Here we are assuming that the maximum number of rows will be be 10.
        :return: is_valid
        :rtype: bool
        """
        is_valid = True
        if self.get_row() < 0 or self.get_row() > 10 or self.get_column() < 0 or self.get_column() > self.get_row():
            is_valid = False
        return is_valid

    def reset(self):
        """
        To reset the glass to empty and setting the flag to False. This method sets the state of glass to the defaults
        for the next set of pouring.
        :return: None
        :rtype: None
        """
        if self.is_valid_row_and_column():
            self.set_is_full(False)
            self.set_filled_water(0)

    def fill_water(self):
        pass
