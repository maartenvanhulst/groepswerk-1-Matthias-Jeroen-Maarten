from core.logger_factory import LoggerFactory


class LoggingObject:
    log = None

    def __init__(self):
        self.log = LoggerFactory().get_logger(self)
