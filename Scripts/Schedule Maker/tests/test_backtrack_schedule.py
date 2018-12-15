import unittest
import backtrack_schedule

class TestStringMethods(unittest.TestCase):

    def test_success_triple(self):
        found = backtrack_schedule.python_call(3, 3, None, "triple", True, 1)
        self.assertEqual(found, True)

    def test_success_double(self):
        found = backtrack_schedule.python_call(3, 3, None, "double", True, 1)
        self.assertEqual(found, True)

    def test_success_triple_nine_teams_three_courts_three_rounds(self):
        found = backtrack_schedule.python_call(3, 9, None, "triple", True, 3)
        self.assertEqual(found, True)

    def test_success_triple_nine_teams_three_courts_nine_rounds(self):
        found = backtrack_schedule.python_call(9, 9, None, "triple", True, 3)
        self.assertEqual(found, True)

    @unittest.skip("demonstrating skipping")
    def test_success_double_nine_teams_three_courts_nine_rounds(self):
        found = backtrack_schedule.python_call(9, 9, None, "double", True, 3)
        self.assertEqual(found, True)

if __name__ == '__main__':
    unittest.main()