import unittest
from unittest.mock import patch
from logic_api.Rankings_api import RankingsApi


class TestRankingsApi(unittest.TestCase):

    def setUp(self):
        """Setup for test cases; runs before each test method."""
        self.rankings_api = RankingsApi()
        self.poll_name = "Coaches Poll"

    @patch('logic_api.Rankings_api.RankingsApi.get_rankings')
    def test_rank_ascending_order(self, mock_get_rankings):
        """
        Test that ranks within the specified poll are in ascending order.
        """
        # Arrange
        year = 2021
        week = 3
        season_type = "regular"
        mock_response = {'polls': [
            {'name': self.poll_name, 'ranks': [{'rank': 1}, {'rank': 2}, {'rank': 3}]}
        ]}
        mock_get_rankings.return_value = mock_response

        # Act
        response = self.rankings_api.get_rankings(year=year, week=week, season_type=season_type)

        # Assert
        self.assertTrue(self.rankings_api.is_rank_ascending(response, self.poll_name),
                        "Ranks within the specified poll should be in ascending order.")


if __name__ == '__main__':
    unittest.main()
