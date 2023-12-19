"""Test cases for the __main__ module."""
from python_example import palindrome


"""
A palindrome is a number that is the same whether it is read from
left-to-right or right-to-left. For example, 121 and 34543 are both palindromes.

It turns out that nearly every integer can be transformed into a palindrome
by reversing its digits and adding it to the original number.
If that does not create a palindrome, add the reverse of the new number to itself.
A palindrome is created by repeating the process of reversing the number
and adding it to itself until the number is a palindrome.
"""


def test_121_is_a_palindrome() -> None:
    value = 121
    result = palindrome.Palindrome.is_palindrome(value)
    assert result is True
