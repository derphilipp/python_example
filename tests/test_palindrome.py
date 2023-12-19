"""Test cases for the __main__ module."""
import pytest

from python_example.palindrome import Palindrome


"""
A palindrome is a number that is the same whether it is read from
left-to-right or right-to-left."""
"""For example, 121 and 34543 are both palindromes."""

"""
It turns out that nearly every integer can be transformed into a palindrome
by reversing its digits and adding it to the original number.
If that does not create a palindrome, add the reverse of the new number to itself.
A palindrome is created by repeating the process of reversing the number
and adding it to itself until the number is a palindrome.
"""


def test_121_is_a_palindrome() -> None:
    """For example, 121 and 34543 are both palindromes."""
    value = 121
    result = Palindrome.is_palindrome(value)
    assert result is True


def test_34543_is_a_palindrome() -> None:
    """For example, 121 and 34543 are both palindromes."""
    value = 34543
    result = Palindrome.is_palindrome(value)
    assert result is True


""" It turns out that nearly every integer can be transformed
into a palindrome by reversing its digits and adding it to the original number."""


# But not for the first time...
def test_5817_is_not_turned_into_a_palindrome_by_processing_once() -> None:
    """5817 does not turn into a palindrome by adding it to its reversed version ONCE"""
    value = 5817
    mid_value = Palindrome.add_reversed_number_to_itself(value)
    result = Palindrome.is_palindrome(mid_value)
    assert result is False


def test_10_is_turned_into_a_palindrome_by_processing_once() -> None:
    """10 does turn into a palindrome by adding it to its reversed version ONCE"""
    value = 10
    mid_value = Palindrome.add_reversed_number_to_itself(value)
    result = Palindrome.is_palindrome(mid_value)
    assert result is True


""" Create a class Transform that contains the method palindrome,
 which takes a number N that is to be transformed and returns a number
 that is the resultant palindrome from this process.
"""

# Remark: I followed this procedure, although this results in all methods being static.
# In Python it is not necessary to create a class to have static methods - but can be useful
# just for structuring your program.


def test_1221_is_already_a_palindrome() -> None:
    """Of course if N is already a palindrome, return it without changing it."""
    value = 1221
    result = Palindrome.palindrome(value)
    assert result == value


def test_196_does_not_turn_into_a_palindrome_in_a_reasonable_amount_of_time() -> None:
    """Though it is theorized that all numbers can be transformed to palindromes in this way,
    some numbers do not converge in a reasonable amount of time.
    For instance, 196 has been carried out to 26,000 digits without finding a palindrome.
    So if the method finds that the resultant palindrome must be greater than 1,000,000,000,
    return the special value -1 instead."""

    value = 196
    result = Palindrome.palindrome(value)
    assert result == -1


def test_5817_can_be_turned_into_a_palindrome() -> None:
    value = 5817
    iterations, mid_value = Palindrome.run_until_is_palindrome(value)
    result = Palindrome.is_palindrome(mid_value)
    assert result is True
    assert iterations == 2


def test_28_can_be_turned_into_palindrome_121() -> None:
    """
    N = 28
    28 + 82 = 110
    110 + 011 = 121, a palindrome. Return 121"""
    value = 28
    result = Palindrome.palindrome(value)
    assert result == 121


def test_51_can_be_turned_into_palindrome_66() -> None:
    """
    Example 2:
    N = 51
    51 + 15 = 66, a palindrome. Return 66"""
    value = 51
    result = Palindrome.palindrome(value)
    assert result == 66


def test_11_is_already_a_palindrome() -> None:
    """
    Further examples:
    Example 3: N = 11, return 11"""
    value = 11
    result = Palindrome.palindrome(value)
    assert result == value


def test_607_can_be_turned_into_palindrome_4444() -> None:
    """
    Example 4: N = 607, return 4444"""
    value = 607
    result = Palindrome.palindrome(value)
    assert result == 4444


def test_196_does_not_turn_into_a_palindrome_in_a_reasonable_amount_of_time() -> None:
    """
    Example 5: N = 196, return -1"""
    value = 196
    result = Palindrome.palindrome(value)
    assert result == -1


# TODO: Check for invalid input
