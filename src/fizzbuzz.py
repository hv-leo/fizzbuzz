def apply(number: int) -> str:
    """
    Compute the FizzBuzz word for a given integer.

    :param number: integer value to compute.
    :return: FizzBuzz word.
    """
    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)
