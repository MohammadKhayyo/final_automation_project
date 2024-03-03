import json

from os.path import dirname, join


class ConfigurationManager:
    def get_filename(self, filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output

    def load_settings(self, file_path="../config.json"):  # Update this line
        """Loads configuration settings from a JSON file."""
        filename = self.get_filename(file_path)
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
