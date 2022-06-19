import os

from src.singleton import Singleton


class Settings(metaclass=Singleton):
    LOGGING_CONFIG_FILE: str = "logging.yaml"
    ROOT_DIR: str = None

    # If the developer instantiates the class, we use the singleton approach
    def __init__(self):
        # Skip logging here !
        # Do not use the LoggerFactory here, nor can you inherit from LoggingObject.
        # LoggingObject and LoggerFactory need the Settings class to determine the root directory
        # for reading their config.  You get a circular reference.
        # Instead, use print.  Just uncomment the print statements, if you want to debug.

        # print("In constructor")

        if self.ROOT_DIR is None:
            # print("Settings class called for the first time")

            self.ROOT_DIR = os.getcwd()

            # print(f"Current dir: {self.ROOT_DIR}")

            while not os.path.exists(os.path.join(self.ROOT_DIR, self.LOGGING_CONFIG_FILE)):
                prev_root = self.ROOT_DIR
                self.ROOT_DIR = os.path.join(self.ROOT_DIR, os.pardir)
                self.ROOT_DIR = os.path.abspath(self.ROOT_DIR)  # os.pardir is actually ".." in most cases

                if self.ROOT_DIR == prev_root:
                    # Avoid eternal loop when not found.
                    # On Linux, the parent of / is /
                    # Not tested on Windows yet
                    raise Exception(f"Can't find the {self.LOGGING_CONFIG_FILE} file, can't determine root directory")

                # print(f"Checking: {self.ROOT_DIR}")

            # print(f"Determined root dir: {self.ROOT_DIR}")

            Settings.ROOT_DIR = self.ROOT_DIR
            # This sets the class attribute if the developer calls the class without instantiating
            # However, the class must be instanced once for the load of the settings to happen,
            # before calling it through the class

        print(f"Root dir: {self.ROOT_DIR}")

    # If the developer uses the class method with load, we make one instance
    @classmethod
    def load(cls):
        Settings()
