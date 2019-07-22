#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : loaddatat.py
@Author: sladesha
@Date  : 2019/7/21 22:00
@Desc  : 
'''

import pickle


def readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


def writebunchobj(path, bunchobj):
    with open(path, "wb") as file_obj:
        pickle.dump(bunchobj, file_obj, 1)
