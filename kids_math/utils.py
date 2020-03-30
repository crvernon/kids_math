"""Common utility functions for the `kids_math` package

"""


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

