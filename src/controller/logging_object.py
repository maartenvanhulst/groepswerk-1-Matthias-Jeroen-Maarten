from logging import Logger

from src.controller.logger_factory import LoggerFactory


class LoggingObject:
    log: Logger = None

    def __init__(self):
        self.log = LoggerFactory().get_logger(self)
