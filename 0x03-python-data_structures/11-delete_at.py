#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
      if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    n_item = my_list[idx]
    my_list.remove(n_item)
    return my_list
