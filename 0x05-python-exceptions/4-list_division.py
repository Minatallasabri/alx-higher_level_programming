#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for j in range(list_length):
        try:
            divi = my_list_1[j] / my_list_2[j]
        except (ValueError, TypeError):
            print("wrong type")
            divi = 0
        except (ZeroDivisionError):
            print("division by 0")
            divi = 0
        except (IndexError):
            print("out of range")
            divi = 0
        finally:
            new_list.append(divi)
    return (new_list)
