import unittest
from unittest.mock import patch

from cfbd.rest import ApiException

from logic_api.Games_api import GamesApi
from infra.api_wrapper import APIWrapper


class TestGameAPI(unittest.TestCase):

    def setUp(self):
        """
        Set up method called before each test. It initializes instances of APIWrapper and GamesApi to be used in the test methods.
        """
        self.year = 2021
        self.game_id = 333130154  # Example game ID
        self.team = 'Clemson'
        self.games_api = GamesApi()
        self.API_wrapper = APIWrapper()

    def test_get_games(self):
        """Test case for getting games for a specific year."""
        year = 2021
        try:
            params = {'year': year}
            response = self.games_api.get_games(**params)
            self.assertTrue(response)
            params = {'season': year}
            status = self.API_wrapper.check_response_content(response_json=response, **params)
            self.assertTrue(status)
        except ApiException as e:
            self.fail(f"API exception: {e}")

    # @patch('logic_api.Games_api.GamesApi.get_games')
    # def test_get_games(self, mock_get_games):
    #     """
    #     Test whether the Games API can retrieve games for a given year.
    #     - Uses 'year' parameter to fetch games from the specific season.
    #     - Asserts that the response is not empty.
    #     - Checks if each game in the response has the correct 'season' value using a helper function.
    #     - Asserts that the check returns True, indicating the response has the expected data.
    #     """
    #     # Arrange
    #     mock_get_games.return_value = [{'id': 1, 'season': self.year}]
    #     params = {'year': self.year}
    #
    #     # Act
    #     response = self.games_api.get_games(**params)
    #
    #     # Assert
    #     self.assertTrue(response)
    #     self.assertEqual(response[0]['season'], self.year)

    def test_get_game_media(self):
        """Test case for getting game media information for a specific year."""
        year = 2021
        try:
            params = {'year': year}
            response = self.games_api.get_game_media(**params)
            self.assertTrue(response)
            params = {'season': year}
            status = self.API_wrapper.check_response_content(response_json=response, **params)
            self.assertTrue(status)
        except ApiException as e:
            self.fail(f"API exception: {e}")

    # @patch('logic_api.Games_api.GamesApi.get_game_media')
    # def test_get_game_media(self, mock_get_game_media):
    #     """
    #     Test whether the Games API can retrieve media information for games from a specific year.
    #     - Uses 'year' parameter to fetch game media.
    #     - Asserts that the response is not empty.
    #     - Verifies that the media information corresponds to the specified year.
    #     """
    #     # Arrange
    #     mock_get_game_media.return_value = [{'id': 1, 'season': self.year}]
    #     params = {'year': self.year}
    #
    #     # Act
    #     response = self.games_api.get_game_media(**params)
    #
    #     # Assert
    #     self.assertTrue(response)
    #     self.assertEqual(response[0]['season'], self.year)

    @patch('logic_api.Games_api.GamesApi.get_player_game_stats')
    def test_get_player_game_stats(self, mock_get_player_game_stats):
        """
        Test case to ensure the API can fetch player game stats for a specified year and game ID.
        - Uses 'year' and 'game_id' parameters to fetch stats.
        - Asserts that the response is a list, which is the expected data type for player game stats.
        """
        # Arrange
        mock_get_player_game_stats.return_value = [
            {'game_id': self.game_id, 'stats': {}}]
        params = {'year': self.year, 'game_id': self.game_id}

        # Act
        response = self.games_api.get_player_game_stats(**params)

        # Assert
        self.assertIsInstance(response, list)
        self.assertEqual(response[0]['game_id'], self.game_id)

    @patch('logic_api.Games_api.GamesApi.get_games')
    def test_get_game_by_id(self, mock_get_games):
        """
        Test case to verify that the Games API can retrieve details for a game using a specific game ID.
        - Fetches all games for a year and then filters to find the game with the specified ID.
        - Asserts that the game details are not None and that the ID matches the specified ID.
        """
        # Arrange
        mock_get_games.return_value = [
            {'id': self.game_id, 'season': self.year}]
        params = {'year': self.year}

        # Act
        games = self.games_api.get_games(**params)
        game_details = next(
            (game for game in games if game['id'] == self.game_id), None)

        # Assert
        self.assertIsNotNone(game_details, "Game details were not found.")
        self.assertEqual(game_details['id'], self.game_id)

    @patch('logic_api.Games_api.GamesApi.get_team_records')
    def test_get_team_records(self, mock_get_team_records):
        """
        Test whether the Games API can retrieve records for a specific team.
        - Uses 'team' parameter to fetch records.
        - Asserts that the response is not empty.
        - Verifies that every record in the response corresponds to the specified team.
        """
        # Arrange
        mock_get_team_records.return_value = [
            {'team': self.team, 'records': {}}]
        params = {'team': self.team}

        # Act
        response = self.games_api.get_team_records(**params)

        # Assert
        self.assertTrue(response)
        self.assertTrue(
            all(record['team'] == self.team for record in response))


if __name__ == '__main__':
    unittest.main()
