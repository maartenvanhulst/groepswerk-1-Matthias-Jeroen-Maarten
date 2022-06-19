import psycopg2
import pathlib
import yaml
import os
from src.logging_object import LoggingObject
from src.controller.settings import Settings
from src.errors import *

Settings.load()


class DataObject(LoggingObject):
    connection = None
    root_dir = Settings.ROOT_DIR

    def __init__(self, model, fetch_by_id_query="", fetch_all_query="", insert_query=""):
        super().__init__()
        self.model = model
        self.fetch_query = fetch_by_id_query
        self.fetch_all_query = fetch_all_query
        self.insert_query = insert_query

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

    def db_execute(self, query, input_data=None):

        self.log.info('Getting connection')
        self.connection = self.db_get_connection()

        self.log.info('Getting cursor')
        cursor = self.db_get_cursor()

        self.log.info(f'cursor_1: {cursor}')

        fetched_data = None

        try:
            self.log.info(f'Starting query execution: {query}')

            # Get data from DB (select)
            if query.startswith("select") or query.startswith("SELECT"):

                self.log.info('Running fetch data')
                cursor.execute(query, input_data)
                fetched_data = cursor.fetchall()

            # Add data into DB (create/insert/update)
            else:
                self.log.info('Running insert/update data')
                cursor.execute(query, input_data)

                try:
                    self.connection.commit()

                except Exception as e:
                    handle_unexpected(e)
            self.log.info('Query executed')

        except psycopg2.OperationalError as e:
            handle_error(FATAL_ERROR_IN_QUERY, e)

        except Exception as e:
            handle_unexpected(e)

        try:
            cursor.close()

        except Exception as e:
            handle_unexpected(e)

        self.log.info('Connection Closed ')

        return fetched_data

    def fetch_by_id(self, row_id: int):
        query = self.db_execute(
            open(os.path.join(self.root_dir, 'src', 'database', self.fetch_query), 'r').read(), row_id)
        return query

    def fetch_all(self):
        query = self.db_execute(
            open(os.path.join(self.root_dir, 'src', 'database', self.fetch_all_query), 'r').read())
        return query

    def insert(self):
        record = []
        for field in self.model.__dataclass_fields__:
            record.append(getattr(self.model, field))
        self.db_execute(open(os.path.join(self.root_dir, 'src', 'database', self.insert_query), 'r').read(), record[1:])