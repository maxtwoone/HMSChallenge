import Palindrome
import pytest


def test_28gives121():
    assert Palindrome.palindrome(28)[0] == 121


def test_51gives66():
    assert Palindrome.palindrome(51)[0] == 66


def test_11gives11():
    assert Palindrome.palindrome(11)[0] == 11

def test_607gives4444():
    assert Palindrome.palindrome(607)[0] == 4444

def test_196givesnegative1():
    assert Palindrome.palindrome(196)[0] == -1
