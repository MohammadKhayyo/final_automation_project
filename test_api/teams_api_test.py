import unittest
from unittest.mock import patch
from logic_api.Teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):

    def setUp(self):
        self.team = 'Clemson'
        self.teams_api = TeamsApi()

    @patch('logic_api.Teams_api.TeamsApi.get_roster')
    def test_get_team_roster(self, mock_get_roster):
        # Arrange
        mock_get_roster.return_value = [{'team': self.team, 'players': []}]
        params = {'team': self.team}

        # Act
        response = self.teams_api.get_roster(**params)

        # Assert
        self.assertTrue(response)
        self.assertTrue(all(
            player['team'] == self.team for player in response), "Roster does not match the team.")


if __name__ == '__main__':
    unittest.main()
