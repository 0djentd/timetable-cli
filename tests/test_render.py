import unittest

from timetable_cli.render import Columns


class ColumnsStrTests(unittest.TestCase):
    def test_parse_str_1(self):
        output = Columns.parse_str("start")
        correct_output = [Columns.START]
        self.assertEqual(output, correct_output)

    def test_parse_str_2(self):
        output = Columns.parse_str("Start")
        correct_output = [Columns.START]
        self.assertEqual(output, correct_output)

    def test_parse_str_3(self):
        output = Columns.parse_str("start,end")
        correct_output = [Columns.START, Columns.END]
        self.assertEqual(output, correct_output)

    def test_parse_str_4(self):
        output = Columns.parse_str("start end")
        correct_output = [Columns.START, Columns.END]
        self.assertEqual(output, correct_output)
