#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 9:21 AM
# @Author  : Slade
# @File    : listt.py

from collections import defaultdict
from .typet import is_type

def index_hash_map(l):
    if is_type(l,list):
        pass
    elif is_type(l,tuple):
        l = list(tuple)
    else:
        raise TypeError('input data should be list or tuple')
    tmp = defaultdict()
    for i in range(len(l)):
        if tmp.get(l[i]):
            tmp[l[i]].append(i)
        else:
            tmp[l[i]] = [i]
    return tmp


def Pi(aim, List):
    '''
    #对一个列表List里的某个元素aim求概率 p(X=aim): 即 aim在List有多少个重复值/List元素总个数
    '''
    length = len(list(List))
    aimcount = (list(List)).count(aim)
    pi = (float)(aimcount/length)
    return pi