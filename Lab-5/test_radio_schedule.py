import unittest

import radio_schedule as schedule


class ScheduleTests(unittest.TestCase):
    def setUp(self):
        schedule.conn = schedule.create_connection()

    def test_parameterized_insert_and_morning_listing(self):
        schedule.add_slot("Morning's Show", "Host", 7, 60)
        schedule.add_slot("Afternoon", "Host", 13, 30)
        self.assertEqual(schedule.morning_shows(), ["Morning's Show"])

    def test_overlap_parser(self):
        self.assertTrue(schedule.overlap_free("8 <= 9"))
        attack = "__import__('os').system('whoami')"
        self.assertFalse(schedule.overlap_free(attack))
        self.assertFalse(schedule.overlap_free("bad <= 5"))

    def test_validation(self):
        invalid_inputs = [
            ("", "Host", 7, 30),
            ("Show", "", 7, 30),
            ("Show", "Host", 24, 30),
            ("Show", "Host", 7, 0),
        ]
        for args in invalid_inputs:
            with self.assertRaises(ValueError):
                schedule.add_slot(*args)

    def test_remove_slot(self):
        schedule.add_slot("Show", "Host", 7, 30)
        self.assertTrue(schedule.remove_slot(1))
        self.assertFalse(schedule.remove_slot(1))
        self.assertEqual(schedule.morning_shows(), [])


if __name__ == "__main__":
    unittest.main()
