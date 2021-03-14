from interfaces.abstractGlass import AbstractGlass
import logging as LOGGER


class Glass(AbstractGlass):
    """
    The Entity class representing the Glass Object. This class extends the `AbstractGlass` class and overrides the
    methods of that class. This class has some properties which indicate the state of the glass and its contents. The
    properties are:
    <ul>
        <li>row</li>
        <li>column</li>
        <li>is_full</li>
        <li>capacity</li>
        <li>filled_water</li>
    </ul>
    The class also has methods to enforce some compliance and correctness of the values.
    """

    def __init__(self):
        """
        The default constructor for the glass class. The properties are set to some defaults based on the business
        rules and assumptions
        """

        self._row = 0
        self._column = 0
        self._is_full = False
        self._capacity = 250
        self._filled_water = 0

    def get_row(self):
        """
        Getter for row
        :return: _row
        :rtype: int
        """
        return self._row

    def set_row(self, row):
        """
        Setter for row
        :param row: value indicating the row number the current glass belongs to
        :type row: int
        :return: None
        :rtype: None
        """
        self._row = row

    def get_column(self):
        """
        Getter for Column
        :return: _column
        :rtype: int
        """
        return self._column

    def set_column(self, column):
        """
        Setter for column
        :param column: value indicating the column number the current glass belongs to
        :type column: int
        :return: None
        :rtype: None
        """
        self._column = column

    def get_is_full(self):
        """
        Getter for is_full
        :return: _is_full
        :rtype: bool
        """
        return self._is_full

    def set_is_full(self, is_full):
        """
        Setter for _is_full
        :param is_full: bool value indicating whether the glass is full or not
        :type is_full: bool
        :return: None
        :rtype: None
        """
        self._is_full = is_full

    def get_capacity(self):
        """
        Getter for _capacity
        :return: _capacity
        :rtype: int
        """
        return self._capacity

    def set_capacity(self, capacity):
        """
        Setter for capacity
        :param capacity: value indicating the capacity(in ml) of the glass
        :type capacity: int
        :return: None
        :rtype: None
        """
        self._capacity = capacity

    def get_filled_water(self):
        """
        Getter for filled_water
        :return: _filled_water
        :rtype: int
        """
        return self._filled_water

    def set_filled_water(self, filled_water):
        """
        Setter for filled_water
        :param filled_water: value indicating the volume of water poured into the glass
        :type filled_water: int
        :return: None
        :rtype: None
        """
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
            LOGGER.error("Row or Columns cannot be negative")
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

    def fill_water(self, water_volume):
        """
        Method that emulates filling of water action into a glass. Returns a ValueError if the poured volume is 0 or
        negative, sets the filled_water to capacity if the poured volume is greater than capacity and sets
        filled_water to the poured volume if it is less than the capacity

        :param water_volume: Value indicating the poured volume
        :type water_volume: int
        :return: None
        :rtype: None
        """
        if water_volume <= 0:
            LOGGER.error("Poured volume cannot be negative or zero")
            raise ValueError("Poured Volume cannot be negative or zero")
        elif water_volume > self.get_capacity():
            self.set_filled_water(self.get_capacity())
            self.set_is_full(True)
        else:
            self.set_filled_water(water_volume)
