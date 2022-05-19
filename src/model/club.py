import os
from src.data_object import DataObject


class Club(DataObject):
    root_dir = os.getcwd()

    def __init__(self, model):
        super(Club, self).__init__(model, 'get_club_by_id.sql', 'get_clubs.sql', 'add_club.sql')

    def get_ranking(self):
        # query: select name, base number, SUM(points) as score where
        pass
