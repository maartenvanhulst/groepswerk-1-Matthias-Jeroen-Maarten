import os
from src.data_object import DataObject


class Matchday(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_matchday_by_id.sql', 'get_matchdays.sql', 'add_matchday.sql')