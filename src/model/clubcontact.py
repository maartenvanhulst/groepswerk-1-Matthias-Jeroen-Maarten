import os
from src.data_object import DataObject


class ClubContact(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_clubcontact_by_id.sql', 'get_clubcontacts.sql', 'add_clubcontact.sql')