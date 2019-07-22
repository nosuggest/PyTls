#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : randomt.py
@Author: sladesha
@Date  : 2019/7/21 22:42
@Desc  : 
'''

import random as rd

__all__ = ["get_random"]


class Random():
    def __init__(self, min_value, max_value, limit):
        self.min_value = min_value
        self.max_value = max_value
        self.limit = limit
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit and self.__index == self.limit:
            raise StopIteration
        self.__index += 1
        return rd.randint(self.min_value, self.max_value)


def get_random(min_value, max_value, limit=10):
    return Random(min_value, max_value, limit)
