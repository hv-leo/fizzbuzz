def apply(number: int) -> str:
    """
    Compute the ThreeFive word for a given integer (similar to FizzBuzz).

    :param number: integer value to compute.
    :return: FizzBuzz word.
    """
    if number % 15 == 0:
        return 'ThreeFive'
    elif number % 3 == 0:
        return 'Three'
    elif number % 5 == 0:
        return 'Five'
    else:
        return str(number)
