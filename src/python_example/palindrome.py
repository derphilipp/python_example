class Palindrome:
    def palindrome(number: int):
        return number

    def is_palindrome(number: int) -> bool:
        """Checks if a number is a palindrome."""
        return str(number) == str(number)[::-1]
