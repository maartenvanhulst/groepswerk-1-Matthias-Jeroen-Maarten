import psycopg2
import yaml
import os

from src.errors import *

__CONNECTION = None


def db_get_connection():
    global __CONNECTION

    while os.getcwd()[-12:] != 'groepswerk-1':
        os.chdir('..')

    try:
        if __CONNECTION is None:
            with open("connection.secret", "r") as connect_options:
                options = yaml.load(connect_options, Loader=yaml.FullLoader)

            __CONNECTION = psycopg2.connect(
                f"dbname={options['database']} user={options['user']} password={options['password']}")

        return __CONNECTION

    except psycopg2.OperationalError as e:
        handle_fatal(FATAL_CANNOT_CREATE_CONNECTION, e)

    except Exception as e:
        handle_unexpected(e)


def db_get_cursor(connection):
    try:
        cursor = connection.cursor()

        return cursor

    except psycopg2.OperationalError as e:
        handle_fatal(FATAL_CANNOT_CREATE_CURSOR, e)

    except Exception as e:
        handle_unexpected(e)


def db_close_connection():
    connection = db_get_connection()

    if connection is None:
        return

    if connection.is_connected():
        try:
            connection.close()

        except psycopg2.OperationalError as e:
            handle_error(ERROR_CANNOT_CLOSE_CONNECTION, e)

        except Exception as e:
            handle_unexpected(e)


# def db_get_records(query):
#     data = None
#     connection = db_get_connection()
#     cursor = db_get_cursor(connection)
#
#     try:
#         cursor.execute(query)
#
#     except mysql.connector.Error as e:
#         handle_fatal(FATAL_ERROR_IN_QUERY, e)
#
#     except Exception as e:
#         handle_unexpected(e)
#
#     try:
#         data = cursor.fetchall()
#
#     except mysql.connector.Error as e:
#         handle_fatal(FATAL_ERROR_IN_FETCH_ALL, e)
#
#     except Exception as e:
#         handle_unexpected(e)
#
#     try:
#         cursor.close()
#
#     except mysql.connector.Error as e:
#         handle_error(ERROR_CANNOT_CLOSE_CURSOR, e)
#
#     except Exception as e:
#         handle_unexpected(e)
#
#     return data
#
#
# def db_get_record(query):
#     data = db_get_records(query)
#
#     if data is None:
#         return None
#
#     return data[0]
#
#
# def db_get_value(query):
#     data = db_get_record(query)
#
#     if data is None:
#         return None
#
#     return data[0]


def db_execute(query, data=None):
    connection = db_get_connection()
    cursor = db_get_cursor(connection)

    try:
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)

    except psycopg2.OperationalError as e:
        handle_error(FATAL_ERROR_IN_QUERY, e)
        # ToDo: add Rollback?

    except Exception as e:
        handle_unexpected(e)
        # ToDo: add Rollback?

    try:
        connection.commit()

    # except mysql.connector.Error as e:
    #     handle_error(FATAL_ERROR_IN_COMMIT, e)

    except Exception as e:
        handle_unexpected(e)
        # ToDo: add Rollback?

    try:
        cursor.close()

    # except mysql.connector.Error as e:
    #     handle_error(ERROR_CANNOT_CLOSE_CURSOR, e)

    except Exception as e:
        handle_unexpected(e)

while os.getcwd()[-12:] != 'groepswerk-1':
    os.chdir('..')

db_execute(open('./src/database/create_db.sql', 'r').read())