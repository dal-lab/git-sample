"""
string_maker test
"""


import pytest
import text_formatter


def test_string_maker_length():
    length = 10
    text_length_10 = text_formatter.xstring_maker(length=length)
    assert len(text_length_10('12345')) == length


def test_string_maker_length_over():
    length = 10
    text_length_10 = text_formatter.xstring_maker(length=length)
    assert len(text_length_10('1234567890123')) == length


def test_string_maker_align_left():
    test_word = 'AAAAA'
    length = 20
    text_align_left = text_formatter.xstring_maker(length=length)
    assert text_align_left(test_word) == test_word.ljust(length, ' ')


def test_string_maker_align_right():
    test_word = 'AAAAA'
    length = 20
    text_align_right = text_formatter.xstring_maker(
        length=length, align='RIGHT')
    assert text_align_right(test_word) == test_word.rjust(length, ' ')


def test_string_maker_align_center():
    test_word = 'AAAAA'
    length = 20
    text_align_center = text_formatter.xstring_maker(length=length, align='MID')
    assert text_align_center(test_word) == test_word.center(length, ' ')


def test_string_maker_align_center_padding_star():
    test_word = 'AAAAA'
    length = 20
    padding = '*'
    text_align_center_padding_star = text_formatter.xstring_maker(
        length=length, align='MID', padding=padding)
    assert text_align_center_padding_star(test_word) \
        == test_word.center(length, padding)
