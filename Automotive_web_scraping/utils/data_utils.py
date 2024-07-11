"""Contains utilities used through out the project"""
import json

class FormatData:
    """Class for formating the data obtained from config.json"""
    def __init__(self, name):
        self.data_file = f"{name}.json"
        self.data = self._load_data()

    def _load_data(self):
        with open(self.data_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_data(self, site):
        """Returns the data needed for formating related to a site"""
        return self.data[site]
