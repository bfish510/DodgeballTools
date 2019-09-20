import unittest
from core import Parameters, BackTrackSchedule
from groupings.GroupingStrategyInterface import GroupingStrategyInterface
from groupings.Triplets import TripletGroupingStrategy
from groupings.DoublesGroupingStrategy import DoublesGroupingStrategy

class TestStringMethods(unittest.TestCase):

    def test_simple(self):
        grouping_strat = GroupingStrategyInterface(DoublesGroupingStrategy(True))
        paramas = Parameters(3, 3, None, grouping_strat, 1, True)
        found = BackTrackSchedule(paramas).init_backtrack()
        self.assertEqual(found, True)

if __name__ == '__main__':
    unittest.main()