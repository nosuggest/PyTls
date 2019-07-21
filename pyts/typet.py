#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : typet.py
@Author: sladesha
@Date  : 2019/7/21 15:08
@Desc  : 
'''


def is_none(value):
    return (not value == value) or (value is None)


def is_type(value, value_type):
    if is_none(value):
        return False
    if is_none(value_type):
        return False
    if not isinstance(value, value_type):
        print("now type is %s but %s is needed"%(value,value_type))
    return isinstance(value, value_type)


def is_empty(value):
    try:
        return len(value) == 0
    except:
        try:
            return value.empty
        except:
            raise TypeError("support list/tuple/array/df only now...")


def is_has_attr(value, attr):
    if is_none(value):
        return False
    if not is_type(attr, str):
        return False
    return hasattr(value, attr)


