#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Chinese2num.py
@Author: sladesha
@Date  : 2019/7/21 23:23
@Desc  : 
'''

from .typet import is_type, is_none
from math import log
from math import e

_zh_num = {'壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '拾': 10, '零': 0, '一': 1, '二': 2,
           '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, "两": 2}

__all__ = ["Chinese_2_num", "ln", "isdigit"]


def Chinese_2_num(ch):
    if not is_type(ch, str):
        raise ValueError("wrong input data type")
    if len(ch) == 1:
        return _zh_num.get(ch)
    else:
        return ''.join(map(str, [_zh_num.get(x) for x in ch if not is_none(_zh_num.get(x))]))


def ln(num):
    return log(num, e)


def isdigit(num):
    if isinstance(num, (float, int)):
        return True
    # 小数
    if isinstance(num, str) and (num.isdigit() or num[:2] == '0.' and num[2:].isdigit()):
        return True
    return False
