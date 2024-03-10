import unittest
from cfbd.rest import ApiException
from logic_api.Games_api import GamesApi
from infra.api_wrapper import APIWrapper


class TestGameAPI(unittest.TestCase):

    def setUp(self):
        """
        Set up method called before each test. It initializes instances of APIWrapper and GamesApi to be used in the test methods.
        """
        self.year = 2021
        self.game_id = 401309866  # Example game ID
        self.team = 'Clemson'
        self.games_api = GamesApi()
        self.API_wrapper = APIWrapper()

    def test_get_games(self):
        """Test case for getting games for a specific year."""
        # Arrange
        year = 2021
        params = {'year': year}

        # Act
        try:
            response = self.games_api.get_games(**params)

            # Assert
            self.assertTrue(response, "The response should not be empty.")

            params['season'] = params.pop('year')
            status = self.API_wrapper.check_response_content(response_json=response, **params)
            self.assertTrue(status, "The status should be True indicating correct response content.")
        except ApiException as e:
            self.fail(f"API exception: {e}")

    def test_get_game_media(self):
        """Test case for getting game media information for a specific year."""
        # Arrange
        year = 2021
        media_type = 'web'
        params = {'year': year, 'media_type': media_type}

        # Act
        try:
            response = self.games_api.get_game_media(**params)

            # Assert
            self.assertTrue(response, "The response should not be empty.")

            params['season'] = params.pop('year')
            status = self.API_wrapper.check_response_content(response_json=response, **params)
            self.assertTrue(status, "The status should be True indicating correct response content.")
        except ApiException as e:
            self.fail(f"API exception: {e}")

    def test_get_player_game_stats(self):
        """
        Test case to ensure the API can fetch player game stats for a specified year and game ID.
        - Uses 'year' and 'game_id' parameters to fetch stats.
        - Asserts that the response is a list, which is the expected data type for player game stats.
        """
        # Arrange
        params = {'year': self.year, 'game_id': self.game_id}

        # Act
        response = self.games_api.get_player_game_stats(**params)

        # Assert
        self.assertIsInstance(response, list)
        self.assertEqual(getattr(response[0], 'id'), self.game_id)

    def test_get_game_by_id(self):
        """
        Test case to verify that the Games API can retrieve details for a game using a specific game ID.
        - Fetches all games for a year and then filters to find the game with the specified ID.
        - Asserts that the game details are not None and that the ID matches the specified ID.
        """
        # Arrange
        params = {'year': self.year}

        # Act
        games = self.games_api.get_games(**params)
        game_details = next(
            (game for game in games if getattr(game, 'id', "") == self.game_id), None)

        # Assert
        self.assertIsNotNone(game_details, "Game details were not found.")
        self.assertEqual(getattr(game_details, 'id'), self.game_id)

    def test_get_team_records(self):
        """
        Test whether the Games API can retrieve records for a specific team.
        - Uses 'team' parameter to fetch records.
        - Asserts that the response is not empty.
        - Verifies that every record in the response corresponds to the specified team.
        """
        # Arrange
        params = {'team': self.team}

        # Act
        response = self.games_api.get_team_records(**params)

        # Assert
        self.assertTrue(response)
        self.assertTrue(
            all(getattr(record, 'team') == self.team for record in response))


if __name__ == '__main__':
    unittest.main()
