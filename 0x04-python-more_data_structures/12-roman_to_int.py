#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        sum_x = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for j in range(len(roman_string)):

            if j == len(roman_string) - 1:
                sum_x += num[roman_string[j]]

            elif num[roman_string[j + 1]] <= num[roman_string[j]]:
                sum_x += num[roman_string[j]]

            else:
                sum_x -= num[roman_string[j]]

        return (sum_x)
    else:
        return (0)
