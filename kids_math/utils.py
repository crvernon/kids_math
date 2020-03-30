"""Common utility functions for the `kids_math` package"""


def valid_answer(response, acceptable, statement):
    """Check value and iterate until valid or too many attempts.

    :param response:                        response from user
    :param acceptable:                      tuple or list; acceptable values
    :param statement:                       string; response to user

    """
    valid = 0
    while valid < 5:
        if response not in acceptable:
            response = input(statement)
            valid += 1
        else:
            return response

    if response not in acceptable:
        print('Sorry still not the correct input.  Ask someone for help and try again.')
        raise ValueError


def say_hello(name):
    """Print out a greeting.

    :param name:                            string;  person's name

    """
    print("Hello {}!".format(name))


def skip_counting(start_number, through_number, by_number):
    """Skip count.

    :param start_number:                    integer;  start number
    :param through_number:                  integer;  number to count to
    :param by_number:                       integer;  number to count by

    """

    for i in range(start_number, through_number + by_number, start_number):
        print(i)

