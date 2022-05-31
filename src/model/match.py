import os
from src.data_object import DataObject


class Match(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_match_by_id.sql', 'get_matches.sql', 'add_match.sql')