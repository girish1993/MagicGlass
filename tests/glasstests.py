from __future__ import annotations
import unittest
from entity import *

    class GlassTests(unittest.TestCase):

        def set_row(self, row):
            self._row = row

        def set_column(self, column):
            self._column = column

        def test_reset_isFull(self):
            """
            resetting the glass should set the isFull Flag property to be False
            :return: None
            :rtype: None
            """
            glass = Glass()
            glass.reset()
            self.assertFalse(glass.get_isFull())


        def test_reset_filled_water_level(self):
            """
            resetting the glass should set the filled water level to 0
            :return: None
            :rtype: None
            """
            glass = Glass()
            glass.reset()
            self.assertEqual(glass.get_filled_water_level(), 0)


