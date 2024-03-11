import unittest
from logic_api.Rankings_api import RankingsApi


class TestRankingsApi(unittest.TestCase):

    def setUp(self):
        """Setup for test cases; runs before each test method."""
        self.rankings_api = RankingsApi()
        self.year = 2021
        self.week = 3
        self.season_type = "regular"

    def test_rank_ascending_order(self):
        """
        Test that ranks are in ascending order.
        """
        # Arrange
        params = {'year': self.year, 'week': self.week, 'season_type': self.season_type}

        # Act
        response = self.rankings_api.get_rankings(**params)

        # Assert
        self.assertTrue(self.rankings_api.is_rank_ascending(response),
                        "Ranks should be in ascending order.")


if __name__ == '__main__':
    unittest.main()
