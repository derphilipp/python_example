"""
Palindrome example for HMS.
This class offers methods to check for palindromes and to transform a number into a palindrome.
"""

VALID_INPUT_FROM = 1
VALID_INPUT_TO = 10_000


class Palindrome:
    """
    Palindrome example for HMS.
    """

    @staticmethod
    def _reverse_number(number: int) -> int:
        return int(str(number)[::-1])

    # Method signature (be sure your method is public): int palindrome(int N);
    @staticmethod
    def palindrome(number: int) -> int:
        """Returns a palindrome from a given number."""

        # Validate input
        if not Palindrome._validate_input(number):
            raise ValueError(
                f"The input must be between {VALID_INPUT_FROM} and {VALID_INPUT_TO} inclusive."
            )
        # If it already is a palindrome, we return it
        if Palindrome.is_palindrome(number):
            return number

        # If it is not a palindrome, we run the algorithm
        return Palindrome.run_until_is_palindrome(number)

    @staticmethod
    def is_palindrome(number: int) -> bool:
        """Checks if a number is a palindrome."""
        return number == Palindrome._reverse_number(number)

    @staticmethod
    def add_reversed_number_to_itself(number: int) -> int:
        """Adds a number to its reversed version."""
        return number + Palindrome._reverse_number(number)

    @staticmethod
    def run_until_is_palindrome(
        number: int, max_size: int = 1_000_000_000
    ) -> (int, int):
        """
        Runs the 'add reversed number to itself' algorithm until a palindrome is found.
        If the number is greater than max_size, it returns -1.
        """
        while not Palindrome.is_palindrome(number):
            if number > max_size:
                return -1
            number = Palindrome.add_reversed_number_to_itself(number)
        return number

    def _validate_input(input_value: int) -> bool:
        """
        N will be between 1 and 10000 inclusive.
        """
        return VALID_INPUT_FROM <= input_value <= VALID_INPUT_TO
