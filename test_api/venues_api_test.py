import unittest
from unittest.mock import patch
from logic_api.Venues_api import VenuesApi
import cfbd


class TestVenuesApi(unittest.TestCase):

    def setUp(self):
        self.venues_api = VenuesApi()

    @patch('logic_api.Venues_api.VenuesApi.get_venues')
    def test_get_venue_information(self, mock_get_venues):
        # Arrange
        mock_venue = cfbd.Venue(id=1, city="CityName", name="StadiumName")
        mock_get_venues.return_value = [mock_venue]

        # Act
        response = self.venues_api.get_venues()

        # Assert
        self.assertTrue(response)
        self.assertIsInstance(response[0], cfbd.Venue)
        self.assertEqual(response[0].id, mock_venue.id)
        self.assertEqual(response[0].city, mock_venue.city)
        self.assertEqual(response[0].name, mock_venue.name)


if __name__ == '__main__':
    unittest.main()
