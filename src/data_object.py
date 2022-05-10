import psycopg2
import pathlib
import yaml
import os
from src.controller.logging_object import LoggingObject

from src.errors import *


class DataObject(LoggingObject):

    connection = None

    def __init__(self):
        super().__init__()

    def db_get_connection(self):

        try:

            if self.connection is None:
                self.log.info('No open connection')
                root_dir = pathlib.Path(os.getcwd())
                self.log.info(f"path: {root_dir}")

                while not os.path.exists(os.path.join(root_dir, 'src', "connection.secret")):
                    root_dir = pathlib.Path(root_dir.parent)
                self.log.info(f"path: {root_dir}")

                with open(os.path.join(root_dir, 'src', "connection.secret"), "r") as connect_options:
                    options = yaml.load(connect_options, Loader=yaml.FullLoader)
                    self.log.info('Connection options loaded')

                self.connection = psycopg2.connect(
                    f"dbname={options['database']} user={options['user']} password={options['password']}")
                self.log.info('Connected')

            return self.connection

        except psycopg2.OperationalError as e:
            handle_fatal(FATAL_CANNOT_CREATE_CONNECTION, e)

        except Exception as e:
            handle_unexpected(e)

    def db_get_cursor(self):
        try:
            cursor = self.connection.cursor()

            return cursor

        except psycopg2.OperationalError as e:
            handle_fatal(FATAL_CANNOT_CREATE_CURSOR, e)

        except Exception as e:
            handle_unexpected(e)

    def db_close_connection(self):
        self.connection = self.db_get_connection()

        if self.connection is None:
            return

        if self.connection.is_connected():
            try:
                self.connection.close()

            except psycopg2.OperationalError as e:
                handle_error(ERROR_CANNOT_CLOSE_CONNECTION, e)

            except Exception as e:
                handle_unexpected(e)

    def db_execute(self, query, data=None):
        self.log.info('Getting connection')
        self.connection = self.db_get_connection()
        self.log.info('Getting cursor')
        cursor = self.db_get_cursor()

        try:
            self.log.info('Starting query execute')
            if data is None:
                cursor.execute(query)
            else:
                cursor.execute(query, data)
            self.log.info('Query executed')

        except psycopg2.OperationalError as e:
            handle_error(FATAL_ERROR_IN_QUERY, e)

        except Exception as e:
            handle_unexpected(e)

        try:
            self.connection.commit()

        except Exception as e:
            handle_unexpected(e)

        try:
            cursor.close()

        except Exception as e:
            handle_unexpected(e)

    def db_read(self):
        return self.db_get_cursor().fetchall()