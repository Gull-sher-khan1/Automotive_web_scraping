"""File containing database related utilities"""

class DuplicateHeadingsHandler:
    """Class handles the issue related to duplicate entries inside the table"""
    headings_to_be_stored = []
    stored_headings = []
    db = None

    def __init__(self, headings, db):
        self.headings_to_be_stored = headings
        self.db = db

    def get_stored_headings(self):
        """gets all already stored headings inside the headings that are scraped"""
        table = self.db['headlines']
        if len(table.table.columns) > 1:
            column = table.table.columns.heading
            clause = column.in_(self.headings_to_be_stored)
            self.stored_headings = [row['heading'] for row in table.find(clause)]
        return self

    def get_non_existing_headings(self):
        """gets headings that need to be stored in DB"""
        return list(set(self.headings_to_be_stored) - set(self.stored_headings))
