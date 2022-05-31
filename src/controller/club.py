import dataclasses

from flask import render_template
from src.logging_object import LoggingObject

from model.club import Club as Model

class Club(LoggingObject):

    model = None

    def __init__(self):
        super().__init__()
        self.model = Model()


