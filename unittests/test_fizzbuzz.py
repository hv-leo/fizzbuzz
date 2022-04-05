from src import fizzbuzz


def test_multiples_of_three_but_not_five_are_fizz():
    """ All multiples of 3 must return "Fizz". """
    for number in range(1, 100):
        if number % 3 == 0 and not number % 5 == 0:
            assert "Fizz" == fizzbuzz.apply(number)


def test_multiples_of_five_but_not_three_are_buzz():
    """ All multiples of 5 must return "Buzz". """
    for number in range(1, 100):
        if number % 5 == 0 and not number % 3 == 0:
            assert "Buzz" == fizzbuzz.apply(number)


def test_multiples_of_three_and_five_are_fizzbuzz():
    """ All multiples of 3 and 5 must return "FizzBuzz". """
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            assert "FizzBuzz" == fizzbuzz.apply(number)
