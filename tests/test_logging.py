import logging

from src.logger_factory import LoggerFactory
from src.logging_object import LoggingObject


class MyTestObject(LoggingObject):
    pass


class TestLogging:
    def test_logging(self):
        lc = LoggerFactory().get_logger(self, logging.INFO)

        lc.info("test")

    def test_object(self):
        lo = MyTestObject()

        lo.log.info("test")