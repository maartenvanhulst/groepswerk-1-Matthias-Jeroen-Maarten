import logging
import logging.config
import os
import pathlib

import yaml as yaml

from src.controller.singleton import Singleton


class LoggerFactory(metaclass=Singleton):
    __loggers = {}

    def __init__(self):
        root_dir = pathlib.Path(os.getcwd())

        while not os.path.exists(os.path.join(root_dir, "logging.yaml")):
            root_dir = pathlib.Path(root_dir.parent)

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
