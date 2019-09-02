import math

from typing import Type, Tuple, Union, List

FloatInt = Union[int, float]


class MathCheck:

    @staticmethod
    def is_even(number: int) -> bool:
        """ prec: x is an integer
            postc: returns True if x is even, False otherwise"""
        if number == 0:
            return False

        if number % 2 == 0:
            return True

        return False

    @staticmethod
    def positivity(number: FloatInt) -> int:
        """ precondition:  number is an integer
            postcondition:  returns 1 if number is positive, 0 for 0, and -1 if negative"""
        if number < 0:
            return -1
        if number > 0:
            return 1
        return 0


class PowerMath:

    @staticmethod
    def cube(number: FloatInt) -> FloatInt:
        """ prec: x is an integer
            postc: returns the cube of x"""
        return number ** 3

    @staticmethod
    def square(num: FloatInt) -> FloatInt:
        """ prec: x is an integer
            postc: returns the square of x"""
        return num * num

    @staticmethod
    def sum_squares(number: int):
        """ precondition:  number is a non-negative  integer
            postcondition:  returns the sum of the squares of the integers 0-number"""
        if number < 0:
            raise ValueError('The given number cannot be negative')

        number: List[int] = range(number + 1)
        number = [k * k for k in number]

        return sum(number)


class PrimeMath:

    @staticmethod
    def is_prime(number: int) -> bool:
        """ prec: n is an integer
            postc: returns True if x is prime, False otherwise"""
        prime_check = 2
        while prime_check * prime_check <= number:
            if number % prime_check == 0:
                return False

            prime_check += 1

        return True

    @staticmethod
    def prime_factors(number: int) -> List[int]:
        """ prec: n is an integer
            postc: returns the prime factors of x"""
        if number == 1:
            return []

        smallest_factor: int = PrimeMath.smallest_factor(number)
        prime_factors: List[int] = PrimeMath.prime_factors(int(int(number) / smallest_factor))

        return [smallest_factor] + prime_factors

    @staticmethod
    def smallest_factor(number: int) -> int:
        """ prec: n is an integer
            postc: returns the smallest factor of n"""
        factor: int = 2
        while factor * factor <= number:
            if number % factor == 0:
                return factor

            factor += 1

        return number


class StatisticsMath:

    @staticmethod
    def standard_deviation(*numbers: FloatInt) -> FloatInt:
        """
        Calculates the standard deviation from a list of numbers
        :param numbers: A list of numbers
        :return: The standard deviations
        """
        mean_of_nums: FloatInt = 0
        for num in numbers:
            mean_of_nums += num

        mean_of_nums = mean_of_nums / len(numbers)

        num_sum: float = 0.0
        for num in numbers:
            num_sum += (float(num) - float(mean_of_nums)) ** 2

        return (num_sum / float(len(numbers))) ** 0.5

    @staticmethod
    def mean(*args: FloatInt) -> float:
        """ precondition:  num is a numerical list
            postcondition:  returns the average of the numbers is num"""
        return sum(*args) / float(len(args))


class TriangleMath:

    @staticmethod
    def hypotenuse(side_a: FloatInt, side_b: FloatInt) -> float:
        # TODO: In future, split to RightTriangleMath (after adding more functions)
        """ precondition: a and b are numbers
            postcondition: returns the length of the hypotenuse of a right triangle
                            with legs of length a and b."""
        a_squared: FloatInt = side_a * side_a
        b_squared: FloatInt = side_b * side_b

        return (a_squared + b_squared) ** .5

    @staticmethod
    def third_side(side_a: FloatInt, side_b: FloatInt, theta: FloatInt) -> float:
        """ precondition: a, b, and theta are numbers.
                            a and b are the side lengths of a triangle, and theta is an angle in
                            radians.
            postcondition: returns the length of the third side"""
        a_squared: FloatInt = side_a * side_a
        b_squared: FloatInt = side_b * side_b
        a_b_2: FloatInt = 2 * side_a * side_b * math.cos(theta)

        sides: FloatInt = a_squared + b_squared - a_b_2
        return math.sqrt(sides)


class TrigMath:

    @staticmethod
    def largest_sine(floats: List[FloatInt]) -> float:
        """ prec: x is a list of floats.
            postc:  returns the largest sine of the list of floats"""
        floats = floats
        floats = [math.sin(k) for k in floats]
        floats.sort()

        return floats[-1]


class WeatherMath:

    @staticmethod
    def to_celsius(farenheit: FloatInt) -> float:
        """ precondition:   tempF is a number
            postcondition:  returns tempF converted to centigrade"""
        return 5.0 / 9.0 * (farenheit - 32)

    @staticmethod
    def to_farenheit(celsius: FloatInt) -> float:
        """ precondition:   tempC is a number
            postcondition:  returns tempC converted to Farenheit"""
        return (9.0 * celsius) / 5.0 + 32


class MathTools:
    check: Type[MathCheck] = MathCheck
    powers: Type[PowerMath] = PowerMath
    primes: Type[PrimeMath] = PrimeMath
    stats: Type[StatisticsMath] = StatisticsMath
    triangle: Type[TriangleMath] = TriangleMath
    trig: Type[TrigMath] = TrigMath
    weather: Type[WeatherMath] = WeatherMath

    @staticmethod
    def absolute(number: FloatInt) -> FloatInt:
        """ prec: x is an integer
            postc: returns x if x is positive, -x if x is negative"""
        return abs(number)

    @staticmethod
    def factorial(number: int) -> int:
        """ precondition:  nn is a non-negative  integer
            postcondition:  returns n!"""
        if number == 0:
            return 1

        return number * MathTools.factorial(number - 1)

    @staticmethod
    def fibonacci(number: int) -> int:
        """ precondition:  n is a non-negative  integer
            postcondition:  returns the fibonacci sum of n"""
        return MathTools.fibonacci_sum(number)[1]

    @staticmethod
    def fibonacci_sum(number: int) -> Tuple[int, int]:
        """ precondition:  n is a non-negative  integer
            postcondition:  helper method that returns the fibonacci sum of n"""
        if number == 0:
            return -1, 0

        if number == 1:
            return 0, 1

        output: Tuple[int, int] = MathTools.fibonacci_sum(number - 1)
        return output[1], output[0] + output[1]

    @staticmethod
    def max(*numbers: FloatInt) -> FloatInt:
        """ prec: x is a list of numbers
            postc: returns the largest number in x"""
        return max(*numbers)

    @staticmethod
    def min(*numbers: FloatInt) -> FloatInt:
        """ prec: x is a list of numbers
            postc: returns the smallest number in x"""
        return min(*numbers)

    @staticmethod
    def product(*numbers: FloatInt) -> FloatInt:
        """ prec: x is a list of numbers
            postc: returns the product of the list"""
        product: FloatInt = 1
        for k in numbers:
            product *= k

        return product
