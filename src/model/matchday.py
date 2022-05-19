import os
from src.data_object import DataObject


class Matchday(DataObject):
    root_dir = os.getcwd()

    def __init__(self, model):
        super(Matchday, self).__init__(model, 'get_matchday_by_id.sql', 'get_matchdays.sql', 'add_matchday.sql')