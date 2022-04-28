import sys
import traceback

FATAL_CANNOT_CREATE_CONNECTION = 10
FATAL_CANNOT_CREATE_CURSOR = 11
FATAL_ERROR_IN_QUERY = 12
FATAL_ERROR_IN_FETCH_ALL = 13
FATAL_ERROR_IN_COMMIT = 14

ERROR_CANNOT_CLOSE_CURSOR = 1000
ERROR_CANNOT_CLOSE_CONNECTION = 1001

FATAL_UNEXPECTED_ERROR = 10000

__ERROR_MESSAGES = {}


def build_error_messages():
    global __ERROR_MESSAGES

    __ERROR_MESSAGES[FATAL_CANNOT_CREATE_CONNECTION] = "Cannot create connection to the database" # 10
    __ERROR_MESSAGES[FATAL_CANNOT_CREATE_CURSOR] = "Cannot create cursor"# 11
    __ERROR_MESSAGES[FATAL_ERROR_IN_QUERY] = "Cannot execute query" # 12
    __ERROR_MESSAGES[FATAL_ERROR_IN_FETCH_ALL] = "Cannot fetch data" # 13
    __ERROR_MESSAGES[FATAL_ERROR_IN_COMMIT] = "Cannot commit" # 14

    __ERROR_MESSAGES[ERROR_CANNOT_CLOSE_CURSOR] = "Cannot close cursor" # 1000
    __ERROR_MESSAGES[ERROR_CANNOT_CLOSE_CONNECTION] = "Cannot close connection" # 1001

    __ERROR_MESSAGES[FATAL_UNEXPECTED_ERROR] = "Unexpected error" # 10000


def get_error_message(error_code):
    global __ERROR_MESSAGES

    if __ERROR_MESSAGES == {}:
        build_error_messages()

    try:
        return __ERROR_MESSAGES[error_code]

    except KeyError as k:
        return "The developer did not enter a specific message for error {0}".format(k)


def handle_error(error_code, error):
    assert 1000 <= error_code < 10000, "Error codes should be between 1000 and 10000"

    error_message = get_error_message(error_code)

    print("ERROR {0}: {1}".format(error_code, error_message))
    print("Reason: {0}".format(error))


def handle_fatal(exit_code, error):
    assert exit_code < 1000 or exit_code == FATAL_UNEXPECTED_ERROR , \
        "Fatal codes should be below 1000 (or 10000 for unexpected)"

    error_message = get_error_message(exit_code)

    print("FATAL {0}: {1}".format(exit_code, error_message))
    print("Reason: {0}".format(error))
    print("Aborting")

    sys.exit(exit_code)


def handle_unexpected(error):
    print(traceback.format_exc())
    print("")

    handle_fatal(FATAL_UNEXPECTED_ERROR, error)
