#!/usr/bin/python3
""" Student to JSON """

class Student:
    """ New class student """

       def __init__(self, first_name, last_name, age):
        """init instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json method"""
        return self.__dict__
