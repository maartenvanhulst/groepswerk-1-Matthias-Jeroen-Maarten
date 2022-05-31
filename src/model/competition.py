import os
from src.data_object import DataObject


class Competition(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_competition_by_id.sql', 'get_competitions.sql', 'add_competition.sql')