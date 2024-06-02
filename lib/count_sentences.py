#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace different punctuations that can end a sentence with a period
        text = self.value.replace('!', '.').replace('?', '.')
        # Split the text by period
        sentences = text.split('.')
        # Filter out empty strings
        sentences = [s for s in sentences if s.strip() != '']
        return len(sentences)
