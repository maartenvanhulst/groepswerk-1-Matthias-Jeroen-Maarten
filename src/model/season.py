import os
from src.data_object import DataObject


class Season(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_season_by_id.sql', 'get_seasons.sql', 'add_season.sql')