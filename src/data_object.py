import psycopg2
import yaml
import os
import controller.logging_object as logging_object

from src.errors import *


class DataObject(logging_object):

    connection = None

    def __init__(self):
        pass

    def db_get_connection(self):
        while os.getcwd()[-12:] != 'groepswerk-1':
            os.chdir('..')

        try:
            if self.connection is None:
                with open("connection.secret", "r") as connect_options:
                    options = yaml.load(connect_options, Loader=yaml.FullLoader)

                self.connection = psycopg2.connect(
                    f"dbname={options['database']} user={options['user']} password={options['password']}")

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
        self.connection = self.db_get_connection()
        cursor = self.db_get_cursor()

        try:
            if data is None:
                cursor.execute(query)
            else:
                cursor.execute(query, data)

        except psycopg2.OperationalError as e:
            handle_error(FATAL_ERROR_IN_QUERY, e)

        except Exception as e:
            handle_unexpected(e)

        try:
            self.connection.commit()

        # except mysql.connector.Error as e:
        #     handle_error(FATAL_ERROR_IN_COMMIT, e)

        except Exception as e:
            handle_unexpected(e)

        try:
            cursor.close()

        # except mysql.connector.Error as e:
        #     handle_error(ERROR_CANNOT_CLOSE_CURSOR, e)

        except Exception as e:
            handle_unexpected(e)


if __name__ == "__main__":

    d_object = DataObject()
    os.chdir("..")
    print(os.getcwd())
    # while os.getcwd()[-12:] != 'groepswerk-1':
    #
    #     os.chdir('..')

    d_object.db_execute(open('./src/database/create_db.sql', 'r').read())

