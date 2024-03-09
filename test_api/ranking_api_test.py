import unittest
from unittest.mock import patch
from logic_api.Rankings_api import RankingsApi


class TestRankingsApi(unittest.TestCase):

    def setUp(self):
        self.rankings_api = RankingsApi()
        self.poll_name = "Coaches Poll"

    def test_rank_ascending_order(self):
        """
        Test that ranks within the specified poll are in ascending order.
        """
        year = 2021
        week = 3
        season_type = "regular"
        response = self.rankings_api.get_rankings(year=year, week=week, season_type=season_type)

        self.assertTrue(self.rankings_api.is_rank_ascending(response, self.poll_name))


if __name__ == '__main__':
    unittest.main()
