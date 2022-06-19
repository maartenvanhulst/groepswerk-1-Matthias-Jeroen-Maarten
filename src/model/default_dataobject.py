import os
from src.data_object import DataObject


class Default(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_club_by_id.sql', 'get_clubs.sql', 'add_club.sql')

