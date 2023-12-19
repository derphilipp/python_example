class Palindrome:
    def _reverse_number(number: int) -> int:
        return int(str(number)[::-1])

    # Method signature (be sure your method is public): int palindrome(int N);
    def palindrome(number: int) -> int:
        """Returns a palindrome from a given number."""
        # If it already is a palindrome, we return it
        if Palindrome.is_palindrome(number):
            return number
        # If it is not a palindrome, we run the algorithm
        number = Palindrome.run_until_is_palindrome(number)
        return number

    def is_palindrome(number: int) -> bool:
        """Checks if a number is a palindrome."""
        return number == Palindrome._reverse_number(number)

    def add_reversed_number_to_itself(number: int) -> int:
        """Adds a number to its reversed version."""
        return number + Palindrome._reverse_number(number)

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
