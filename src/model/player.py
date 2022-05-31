import os
from src.data_object import DataObject


class Player(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_player_by_id.sql', 'get_players.sql', 'add_player.sql')