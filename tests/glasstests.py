from __future__ import annotations
import unittest
from entity import *


class GlassTests(unittest.TestCase):

    def test_reset_is_full(self):
        """
        resetting the glass should set the isFull Flag property to be False
        :return: None
        :rtype: None
        """
        glass = Glass()
        glass.reset()
        self.assertFalse(glass.get_is_full())

    def test_reset_filled_water_level(self):
        """
        resetting the glass should set the filled water level to 0
        :return: None
        :rtype: None
        """
        glass = Glass()
        glass.reset()
        self.assertEqual(glass.get_filled_water_level(), 0)

    def test_fill_water_when_volume_more_than_capacity(self):
        """
        Fill water should update the filled water value prop when the volume poured is less than volume
        :return: None
        :rtype: None
        """
        row = 0
        column = 0
        is_full = False
        capacity = 250
        filled_water = 0
        water_pour_volume = 200

        glass = Glass(row, column, is_full, capacity, filled_water)
        glass.fill_water(water_pour_volume)
        self.assertEqual(glass.get_filled_water_level(), 200)
        self.assertFalse(glass.get_is_full())

    def test_fill_water_when_capacity_is_negative(self):
        """
        Fill water method that should return error message when volume poured is more than the capacity
        :return: None
        :rtype: None
        """
        row = 0
        column = 0
        is_full = False
        capacity = 0
        filled_water = 0
        water_pour_volume = 200

        glass = Glass(row, column, is_full, capacity, filled_water)
        self.assertEqual(glass.fill_water(water_pour_volume), "The capacity of the glass cannot be 0 or negative")

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
