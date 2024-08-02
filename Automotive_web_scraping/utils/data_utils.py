"""Contains utilities used through out the project"""
import json
import re
from pathlib import Path

class DataFormater:
    """Class for formating the data obtained from config.json"""
    def __init__(self, name):
        self.data_file = str(Path(__file__).parents[1]) + fr"/configurations/{name}.json"
        self.data = self._load_data()

    def _load_data(self):
        with open(self.data_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_data(self, key = None):
        """Returns the data needed for formating related to a site"""
        return self.data[key] if key else self.data

class StringTransformer:
    """Class for transforming string"""

    @classmethod
    def remove_whitespaces(cls, string):
        """Removes white spaces and other characters from string"""
        return ' '.join(re.sub(r'[^\w\s.]','',string).split())
