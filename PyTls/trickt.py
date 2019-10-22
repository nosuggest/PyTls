#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 1:30 PM
# @Author  : Slade
# @File    : trickt.py

from .typet import is_type
import time


def choose_method(func1, func2, condition, *params):
    if not is_type(condition, bool):
        raise TypeError('condition should be bool')
    return (func1 if condition else func2)(*params)


class Timer(object):
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *unused):
        print("total time is %s second." % (time.time() - self.start))
