import os
from src.data_object import DataObject


class Match(DataObject):
    root_dir = os.getcwd()

    def __init__(self, model):
        super(Match, self).__init__(model, 'get_match_by_id.sql', 'get_matches.sql', 'add_match.sql')