import traceback
import unittest
from cfbd.rest import ApiException
from logic.logic_api.Games_api import GamesApi
from infra.infra_api.api_wrapper import APIWrapper
from infra.infra_jira.jira_wrapper import JiraWrapper


class TestGameAPI(unittest.TestCase):

    def setUp(self):
        super().setUp()  # Call the base class setup
        self.year = 2021
        self.game_id = 401309866  # Example game ID
        self.team = 'Clemson'
        self.games_api = GamesApi()
        self.API_wrapper = APIWrapper()
        self.jira = JiraWrapper()
        self.project_key = "KP"  # Adjust to your JIRA project key
        self._test_errors = None
        self.summary = f"Assertion failed in {self.id().split('.')[-1]}"

    def tearDown(self):
        for test, exc_info in self._outcome.errors:
            if exc_info:
                # This will format the exception information into a string
                error_type, error_instance, error_traceback = exc_info
                formatted_traceback = ''.join(traceback.format_exception(error_type, error_instance, error_traceback))
                description = f"Test {self._testMethodName} failed: {str(error_instance)}\n{formatted_traceback}"
                issue_key = self.jira.create_issue(self.summary, f"{self._test_errors}\n{description}",
                                                   self.project_key)
                print(f"Created JIRA issue: {issue_key}")
        super().tearDown()

    def assertAndCapture(self, assertion_callable, *args, **kwargs):
        try:
            assertion_callable(*args, **kwargs)
        except Exception as e:  # Catch any kind of exception
            self._test_errors = (e.__class__.__name__, str(e), e.__traceback__)
            raise

    # Now use assertAndCapture for each assertion in your test methods
    def test_get_games(self):
        # Arrange
        params = {'year': self.year}

        # Act
        response = self.games_api.get_games(**params)

        # Assert
        self.assertAndCapture(self.assertTrue, response, "The response should not be empty.")
        params['season'] = params.pop('year')
        status = self.API_wrapper.check_response_content(response_json=response, **params)
        self.assertAndCapture(self.assertTrue, status, "The status should be True indicating correct response content.")

    def test_get_game_media(self):
        """test_ui case for getting game media information for a specific year."""
        # Arrange
        year = 2021
        media_type = 'web'
        params = {'year': year, 'media_type': media_type}

        # Act
        response = self.games_api.get_game_media(**params)

        # Assert
        self.assertAndCapture(self.assertTrue, response, "The response should not be empty.")

        params['season'] = params.pop('year')
        status = self.API_wrapper.check_response_content(response_json=response, **params)
        self.assertAndCapture(self.assertTrue, status, "The status should be True indicating correct response content.")

    def test_get_player_game_stats(self):
        """
        test_ui case to ensure the API can fetch player game stats for a specified year and game ID.
        - Uses 'year' and 'game_id' parameters to fetch stats.
        - Asserts that the response is a list, which is the expected data type for player game stats.
        """
        # Arrange
        params = {'year': self.year, 'game_id': self.game_id}

        # Act
        response = self.games_api.get_player_game_stats(**params)

        # Assert
        self.assertAndCapture(self.assertIsInstance, response, list)
        self.assertAndCapture(self.assertEqual, getattr(response[0], 'id'), self.game_id)

    def test_get_game_by_id(self):
        """
        test_ui case to verify that the Games API can retrieve details for a game using a specific game ID.
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
        self.assertAndCapture(self.assertIsNotNone, game_details, "Game details were not found.")
        self.assertAndCapture(self.assertEqual, getattr(game_details, 'id'), self.game_id)

    def test_get_team_records(self):
        """
        test_ui whether the Games API can retrieve records for a specific team.
        - Uses 'team' parameter to fetch records.
        - Asserts that the response is not empty.
        - Verifies that every record in the response corresponds to the specified team.
        """
        # Arrange
        params = {'team': self.team}

        # Act

        response = self.games_api.get_team_records(**params)

        # Assert
        self.assertAndCapture(self.assertTrue, response)
        self.assertAndCapture(self.assertTrue,
                              all(getattr(record, 'team') == self.team for record in response))


if __name__ == '__main__':
    unittest.main()
