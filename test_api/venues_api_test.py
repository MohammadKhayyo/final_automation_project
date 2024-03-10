import unittest
from logic_api.Venues_api import VenuesApi
import cfbd


class TestVenuesApi(unittest.TestCase):

    def setUp(self):
        self.venues_api = VenuesApi()
        # self.mock_venue = cfbd.Venue(id=3997, city="New Haven", name="Yale Bowl")

    def test_get_venue_information(self):
        # Arrange
        self.mock_venue = cfbd.Venue(id=3997, city="New Haven", name="Yale Bowl")
        params = {'id': 3997, 'city': "New Haven", 'name': "Yale Bowl"}

        # Act
        response = self.venues_api.get_venues()

        # Assert
        self.assertTrue(response)
        venue_details = next(
            (venue for venue in response if getattr(venue, 'id', "") == self.mock_venue.id), None)
        self.assertEqual(getattr(venue_details, 'id', ""), self.mock_venue.id)
        self.assertEqual(getattr(venue_details, 'city', ""), self.mock_venue.city)
        self.assertEqual(getattr(venue_details, 'name', ""), self.mock_venue.name)


if __name__ == '__main__':
    unittest.main()
