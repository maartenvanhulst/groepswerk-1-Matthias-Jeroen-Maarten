import os
from src.data_object import DataObject


class League(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_league_by_id.sql', 'get_leagues.sql', 'add_league.sql')