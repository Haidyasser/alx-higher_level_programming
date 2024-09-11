#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Class that is have only fist_name attribute"""
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        self.first_name = first_name
