#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : strt.py
@Author: sladesha
@Date  : 2019/7/21 16:23
@Desc  : 
'''

import re
from .typet import is_type, is_empty


def str_reverse(word):
    return word[::-1]


def str_repeat(word, n):
    if is_type(word, str) and is_type(n, int):
        return word * n
    else:
        raise TypeError("word should be str and n should be int...")


def _split_words(words, split_char):
    return words.split(split_char)


def str_splits(words, split_chars, warning_info=True):
    """
        param:words:basestring:split string
        param:split_chars:split char list
        Test:str_split("下午吃的两个了的苹果",["的","了"]）
    """
    if warning_info:
        print("be careful if split_chars with symbol:|...")
    if is_empty(words):
        return []
    if is_type(split_chars, list):
        split_chars = "|".join(split_chars)
    else:
        raise TypeError("split_chars should be list instead of %s" % type(split_chars))
    return [word for word in re.split(split_chars, words) if len(word) > 0]
