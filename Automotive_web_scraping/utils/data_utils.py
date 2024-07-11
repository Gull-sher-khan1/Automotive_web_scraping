import json

class FormatData:
    def __init__(self, name):
        self.data_file = f"{name}.json"
        self.data = self._load_data()

    def _load_data(self):
        with open(self.data_file, "r") as f:
            return json.load(f)

    def get_data(self, site):
        return self.data[site]