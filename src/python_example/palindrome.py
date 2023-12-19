class Palindrome:
    def _reverse_number(number: int) -> int:
        return int(str(number)[::-1])

    def palindrome(number: int):
        # If it already is a palindrome, we return it
        if Palindrome.is_palindrome(number):
            return number
        # If it is not a palindrome, we run the algorithm
        iterations, number = Palindrome.run_until_is_palindrome(number)
        return number

    def is_palindrome(number: int) -> bool:
        """Checks if a number is a palindrome."""
        return number == Palindrome._reverse_number(number)

    def turn_into_palindrome(number: int) -> int:
        # reversing its digits and adding it to the original number
        return number + Palindrome._reverse_number(number)

    def run_until_is_palindrome(
        number: int, max_iterations: int = 1000, max_size: int = 1_000_000_000
    ) -> (int, int):
        """Runs the palindrome algorithm until a palindrome is found."""
        iterations = 0
        while not Palindrome.is_palindrome(number):
            number = Palindrome.turn_into_palindrome(number)
            iterations += 1
            if iterations > max_iterations:
                raise RuntimeError(
                    f"No palindrome found (max iterations: {max_iterations})"
                )
            elif number > max_size:
                return iterations, -1
        return iterations, number
