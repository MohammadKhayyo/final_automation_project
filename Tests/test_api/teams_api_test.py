import unittest
from logic.logic_api.Teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):

    def setUp(self):
        self.team = 'Clemson'
        self.teams_api = TeamsApi()

    def test_get_team_roster(self):
        # Arrange
        params = {'team': self.team}

        # Act
        response = self.teams_api.get_roster(**params)

        # Assert
        self.assertTrue(response)
        self.assertTrue(all(
            getattr(player, 'team') == self.team for player in response), "Roster does not match the team.")


if __name__ == '__main__':
    unittest.main()
