from __future__ import annotations
import unittest
from entity.glass import Glass
from entity import *


class GlassFactoryTests(unittest.TestCase):

    def test_can_setup_when_row_is_negative(self):
        rows = -10
        glass_factory = GlassFactory()
        self.assertFalse(glass_factory.can_setup(rows))

    def test_can_setup_when_row_is_beyond_permissible_number(self):
        rows = 12
        glass_factory = GlassFactory()
        self.assertFalse(glass_factory.can_setup(rows))

    def test_can_setup_with_correct_numbers(self):
        rows = 6
        glass_factory = GlassFactory()
        self.assertTrue(glass_factory.can_setup(rows))

    def test_setup_glass_stack_returns_the_correct_number_of_glasses(self):
        rows = 6
        expected_number_Of_glasses = rows * ((rows + 1) / 2)
        glass_factory = GlassFactory()
        glass_factory.setup_glass_stack(rows)
        self.assertEqual(len(glass_factory.get_all_glasses()), expected_number_Of_glasses)

    def test_setup_glass_stack_returns_error_message_when_cannot_setup_stack(self):
        rows = 6
        glass_factory = GlassFactory()
        with self.assertRaises(ValueError):
            glass_factory.setup_glass_stack(rows)

    def test_pour_water_with_negative_volume_returns_error(self):
        poured_volume = -10
        glass_factory = GlassFactory()
        with self.assertRaises(ValueError):
            glass_factory.pour_water(poured_volume)

    def test_pour_water_with_some_arbitrary_positive_value(self):
        poured_volume = 20
        glass_factory = GlassFactory()
        with self.assertLogs('root', level="INFO") as cm:
            glass_factory.pour_water(poured_volume)
        self.assertIn("DEBUG:root:Water of volume {} poured".format(poured_volume), cm.output)

    def test_pour_water_with_exact_volume_as_rows_should_have_all_glasses_full(self):
        poured_volume = 6000
        rows = 6
        glass_factory = GlassFactory()
        glass_factory.setup_glass_stack(rows)
        self.pour_water(poured_volume)
        water_volume_is_full = list(filter(lambda x : x.get_is_full(), glass_factory.get_all_glasses()))
        self.assertTrue(water_volume_is_full)

    def test_pour_water_with_zero_volume_returns_error(self):
        poured_volume = 0
        glass_factory = GlassFactory()
        with self.assertRaises(ValueError):
            glass_factory.pour_water(poured_volume)

    def test_find_water_in_glass_when_trying_to_find_glass_with_incorrect_index_throws_error(self):
        row = -1
        column = 10
        rows = 5
        glass_factory = GlassFactory()
        glass_factory.setup_glass_stack(rows)
        with self.assertRaises(ValueError):
            glass_factory.find_water_in_glass(row,column)


    def test_find_water_in_glass_displays_the_correct_value(self):
        row = 0
        column = 0
        rows = 5
        poured_volume = 200
        glass_factory = GlassFactory()
        glass_factory.setup_glass_stack(rows)
        glass_factory.pour_water(poured_volume)
        self.assertEqual(glass_factory.find_water_in_glass(row, column), poured_volume)

