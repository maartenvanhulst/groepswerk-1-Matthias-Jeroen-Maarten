import os
from src.data_object import DataObject


class Series(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_series_by_id.sql', 'get_series.sql', 'add_series.sql')