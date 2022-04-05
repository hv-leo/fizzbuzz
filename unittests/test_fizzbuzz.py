from src import fizzbuzz


def test_multiples_of_three_but_not_five_are_three():
    """ All multiples of 3 must return "Three". """
    for number in range(1, 100):
        if number % 3 == 0 and not number % 5 == 0:
            assert "Three" == fizzbuzz.apply(number)


def test_multiples_of_five_but_not_three_are_five():
    """ All multiples of 5 must return "Five". """
    for number in range(1, 100):
        if number % 5 == 0 and not number % 3 == 0:
            assert "Five" == fizzbuzz.apply(number)


def test_multiples_of_three_and_five_are_threefive():
    """ All multiples of 3 and 5 must return "ThreeFive". """
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            assert "ThreeFive" == fizzbuzz.apply(number)

def test_numbers_not_multiple_of_three_nor_five():
    """ All non multiples of 3 and 5 must return the number itself. """
    for number in range(1, 100):
        if number % 3 != 0 and number % 5 != 0:
            assert str(number) == fizzbuzz.apply(number)
