from __future__ import annotations
import unittest
from entity.glass import Glass


class GlassTests(unittest.TestCase):

    @staticmethod
    def set_up_glass_instance(row, column, is_full, capacity, filled_water):
        """
        Static setup method to setup the glass instance
        :param row: number indicating the position of the glass
        :type row: int
        :param column: number indicating the column of glass
        :type column: int
        :param is_full: flag indicating the level of water filled in the glass
        :type is_full: bool
        :param capacity: number to indicate the capacity of the glass(in ml)
        :type capacity: int
        :param filled_water: number indicating the volume (in ml) of water filled in the glass
        :type filled_water: int
        :return: glass
        :rtype: Glass
        """
        glass = Glass()
        glass.set_row(row)
        glass.set_column(column)
        glass.set_capacity(capacity)
        glass.set_filled_water(filled_water)
        glass.set_is_full(is_full)
        return glass

    def test_reset_is_full(self):
        """
        resetting the glass should set the isFull Flag property to be False
        :return: None
        :rtype: None
        """
        glass = self.set_up_glass_instance(0, 0, True, 250, 200)
        glass.reset()
        self.assertFalse(glass.get_is_full())

    def test_reset_filled_water_level(self):
        """
        resetting the glass should set the filled water level to 0
        :return: None
        :rtype: None
        """
        glass = self.set_up_glass_instance(0, 0, True, 250, 200)
        glass.reset()
        self.assertEqual(glass.get_filled_water(), 0)

    def test_is_valid_row_and_column(self):
        """
        Test to check the is_valid_row_and_column method when column is greater than row
        :return: None
        :rtype:None
        """
        glass = self.set_up_glass_instance(0, 2, True, 250, 200)
        self.assertFalse(glass.is_valid_row_and_column())

    def test_is_valid_row_and_column_when_numbers_are_negative(self):
        """
        Test to check the is_valid_row_and_column method when column is greater than row
        :return: None
        :rtype:None
        """
        glass = self.set_up_glass_instance(0, -2, True, 250, 200)
        self.assertFalse(glass.is_valid_row_and_column())

    def test_is_valid_row_and_column_when_numbers_are_correct(self):
        """
        Test to check the is_valid_row_and_column method when row and column numbers are well within the range
        :return: None
        :rtype:None
        """
        glass = self.set_up_glass_instance(9, 3, True, 250, 200)
        self.assertTrue(glass.is_valid_row_and_column())

    def test_is_valid_row_and_column_when_row_number_is_beyond_limit(self):
        """
        Test to check the is_valid_row_and_column method when row number is beyond a certain limit
        :return: None
        :rtype:None
        """
        glass = self.set_up_glass_instance(13, 3, True, 250, 200)
        self.assertFalse(glass.is_valid_row_and_column())

    def test_fill_water_when_volume_more_than_capacity(self):
        """
        Fill water should update the filled water value prop when the volume poured is less than volume
        :return: None
        :rtype: None
        """
        water_pour_volume = 200
        glass = self.set_up_glass_instance(0, 0, False, 250, 0)
        glass.fill_water(water_pour_volume)
        self.assertEqual(glass.get_filled_water(), 200)
        self.assertFalse(glass.get_is_full())

    def test_fill_water_when_capacity_is_negative(self):
        """
        Fill water method that should return error message when volume poured is more than the capacity
        :return: None
        :rtype: None
        """
        glass = self.set_up_glass_instance(0, 0, False, 250, 200)
        self.assertEqual(glass.get_filled_water()(water_pour_volume),
                         "The capacity of the glass cannot be 0 or negative")

    def test_fill_water_when_row_column_are_negative(self):
        """
        Fill water method that should return error message when the row and column numbers are negative
        :return: None
        :rtype: None
        """
        row = -20
        column = -30
        is_full = False
        capacity = 0
        filled_water = 0
        water_pour_volume = 200

        glass = Glass(row, column, is_full, capacity, filled_water)
        self.assertEqual(glass.fill_water(water_pour_volume), "The row and column numbers cannot be less than 0")
