#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 1:30 PM
# @Author  : Slade
# @File    : trickt.py

from .typet import is_type


def choose_method(func1, func2, condition, *params):
    if not is_type(condition, bool):
        raise TypeError('condition should be bool')
    return (func1 if condition else func2)(*params)
