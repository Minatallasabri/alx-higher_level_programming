#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        first_character = sentence[0]
    else:
        first_character = None
    return (lenght, first_character)
