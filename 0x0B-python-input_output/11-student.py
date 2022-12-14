#!/usr/bin/python3
"""
    Defines a student class
"""


class Student:
    """Student definition"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary rep of 'Student' class"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for key, val in json.items():
            self.__setattr__(key, val)
