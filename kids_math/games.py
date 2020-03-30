from kids_math.utils import valid_answer
from kids_math.gifs import PeterRabbitGif, FrozenGif


def greater_than_less_than(first_number, second_number):
    """Fill in.

    """

    gifs = PeterRabbitGif()
    acceptable = ('=', '>', '<')

    if first_number == second_number:
        result = '='

    elif first_number > second_number:
        result = '>'

    else:
        result = '<'

    response = input("""Is the first number greater than (>), less than (<), or equal to (=) the second number? 
    [enter either >, <, or =]:  """).strip()

    wrong_input = "Try again:  Your answer must either be >, <, or ="

    response = valid_answer(response, acceptable, wrong_input)

    wrong_response = "Sorry!  {} is not {} to {}.  Try again...".format(first_number, response, second_number)

    # ask five more times if need be
    correct = 0
    while correct < 5:

        if response == result:
            print('\nCORRECT!!! GREAT WORK!!!')
            return gifs.wink()

        else:
            response = input(wrong_response)

            # check for valid answer
            response = valid_answer(response, acceptable, wrong_input)

            correct += 1

    print("Sorry, either try again or ask for help.")
    return gifs.nope()


def add_to_five(number):
    """Add to the 5 by any number.

    :param number:                          

    """
    gifs = FrozenGif()
    acceptable = (int, float)

    type_number = type(number)

    if type_number in acceptable:

        # get answer
        answer = 5 + number

        response = int(input("Enter the answer to 5 + {}?  ".format(number)))
        type_response = type(response)

        wrong_response = "Sorry! 5 + {} is not equal to {}.  Try again...".format(number, response)

        if (type_response in acceptable) and (response == answer):
            print('\n CORRECT!!! GREAT WORK!!!')
            return gifs.walking()

        else:
            correct = 0
            while correct < 5:

                if (type_response in acceptable) and (response == answer):
                    print('\n CORRECT!!! GREAT WORK!!!')
                    return gifs.walking()

                elif (type_response in acceptable) and (response != answer):

                    response = int(input(wrong_response))

                    correct += 1
                else:
                    pass

            print("Sorry, either try again or ask for help.")
            return gifs.olaf_heart()
