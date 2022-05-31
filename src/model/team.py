import os
from src.data_object import DataObject


class Team(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_team_by_id.sql', 'get_team.sql', 'add_team.sql')