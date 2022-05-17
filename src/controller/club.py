import os
from src.data_object import DataObject
from src.model.club import Club as Model
from dataclasses import fields


class Club(DataObject):
    root_dir = os.getcwd()

    def __init__(self):
        super().__init__('get_club_by_id.sql', 'get_clubs.sql', 'add_club.sql')

    def get_ranking(self):
        # query: select name, base number, SUM(points) as score where
        pass
