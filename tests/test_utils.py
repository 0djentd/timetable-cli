import unittest
from datetime import timedelta

from timetable_cli.utils import parse_timedelta_str


class ParseTimedeltaStrTests(unittest.TestCase):
    def test_1(self):
        input_str = "1h"
        output = parse_timedelta_str(input_str)
        correct_output = timedelta(hours=1)
        self.assertEqual(output, correct_output)

    def test_2(self):
        input_str = "-1h"
        output = parse_timedelta_str(input_str)
        correct_output = timedelta(hours=-1)
        self.assertEqual(output, correct_output)

    def test_3(self):
        input_str = "1d1h1m1s"
        output = parse_timedelta_str(input_str)
        correct_output = timedelta(days=1, hours=1, minutes=1, seconds=1)
        self.assertEqual(output, correct_output)

    def test_4(self):
        input_str = "1d 1h 1m 1s"
        output = parse_timedelta_str(input_str)
        correct_output = timedelta(days=1, hours=1, minutes=1, seconds=1)
        self.assertEqual(output, correct_output)

    def test_5(self):
        input_str = "1s 1m 1h 1d"
        output = parse_timedelta_str(input_str)
        correct_output = timedelta(days=1, hours=1, minutes=1, seconds=1)
        self.assertEqual(output, correct_output)
