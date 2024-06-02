#!/usr/bin/env python3

import pytest
from count_sentences import MyString

import io
import sys

def test_is_sentence():
    string = MyString("This is a sentence.")
    assert string.is_sentence() == True

    string.value = "This is not a sentence"
    assert string.is_sentence() == False

def test_is_question():
    string = MyString("Is this a question?")
    assert string.is_question() == True

    string.value = "This is not a question"
    assert string.is_question() == False

def test_is_exclamation():
    string = MyString("This is exciting!")
    assert string.is_exclamation() == True

    string.value = "This is not exciting"
    assert string.is_exclamation() == False

def test_count_sentences():
    string = MyString("This is a string! It has three sentences. Right?")
    assert string.count_sentences() == 3

    string.value = "This... is tricky! How many sentences? Two!!"
    assert string.count_sentences() == 4

    string.value = ""
    assert string.count_sentences() == 0
