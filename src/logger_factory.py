import logging
import logging.config
import os

import yaml as yaml

from src.singleton import Singleton
from src.controller.settings import Settings


class LoggerFactory(metaclass=Singleton):
    __loggers = {}

    def __init__(self):
        root_dir = Settings.ROOT_DIR

        if len(self.__loggers) == 0:
            with open(os.path.join(root_dir, "logging.yaml"), "r") as config_file:
                config = yaml.safe_load(config_file.read())
                logging.config.dictConfig(config)

            logging.basicConfig(level=logging.INFO)

    def get_logger(self, cls, log_level=logging.INFO):
        class_name = cls.__class__.__name__

        if class_name not in self.__loggers:
            logger = logging.getLogger(class_name)
            logger.setLevel(log_level)

            self.__loggers[class_name] = logger

        return self.__loggers[class_name]
