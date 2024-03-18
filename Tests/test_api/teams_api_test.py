import unittest
from logic.logic_api.Teams_api import TeamsApi
from infra.infra_jira.jira_wrapper import JiraWrapper


class TestTeamsApi(unittest.TestCase):

    def setUp(self):
        self.team = 'Clemson'
        self.teams_api = TeamsApi()
        self.jira = JiraWrapper()
        self.test_name = self.id().split('.')[-1]
        self.summary = f"{self.test_name}"
        self.project_key = "KP"  # Adjust to your JIRA project key
        self.test_error = None  # Initialize error tracking

    def test_get_team_roster(self):
        # Arrange
        params = {'team': self.team}

        # Act
        response = self.teams_api.get_roster(**params)

        # Assert
        self.assertTrue(response)
        self.assertTrue(all(
            getattr(player, 'team') == self.team for player in response), "Roster does not match the team.")

    def tearDown(self):
        if self.test_error:
            issue_key = self.jira.create_issue(self.summary, str(self.test_error), self.project_key)
            print(f"Created JIRA issue: {issue_key}")
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
