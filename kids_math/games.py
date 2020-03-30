from matplotlib.pyplot import imshow

from kids_math.utils import valid_answer


def greater_than_less_than(first_number, second_number):
    """Fill in.

    """
    acceptable = ('=', '>', '<')

    if first_number == second_number:
        result = '='

    elif first_number > second_number:
        result = '>'

    else:
        result = '<'

    response = input("Is the first number greater than (>), less than (<), or equal to (=) the second number? [type in the symbol]").strip()

    wrong_input = "Try again:  Your answer must either be >, <, or ="

    response = valid_answer(response, acceptable, wrong_input)

    wrong_response = "Sorry!  {} is not {} to {}.  Try again...".format(first_number, response, second_number)

    # ask five more times if need be
    correct = 0
    while correct < 5:

        if response == result:
            print('GREAT JOB!')
            return 0

        else:
            response = input(wrong_response)
            correct += 1

    print("Sorry, either try again or ask for help.")
