#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 9:21 AM
# @Author  : Slade
# @File    : listt.py

from collections import defaultdict, OrderedDict, Counter
from .typet import is_type
from functools import reduce


def index_hash_map(l):
    if is_type(l, list):
        pass
    elif is_type(l, tuple):
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
    pi = (float)(aimcount / length)
    return pi


def single_one(List, explation=True):
    if explation:
        print("input data must be: paris and only one single")
    return reduce(lambda x, y: x ^ y, List)


def subset(List):
    if not is_type(List, list):
        raise TypeError('input data should be list or tuple')
    ret = [[]]
    for num in List:
        for item in ret[:]:
            tmp = item[:]
            tmp.append(num)
            ret.append(tmp)
    return ret


def permute(nums):
    result = []

    def _dfs(last, v_nums):
        len_v_nums = len(v_nums)
        if len_v_nums == 1:
            return result.append(last + v_nums)
        for i, n in enumerate(v_nums):
            _dfs(last + [n], v_nums[:i] + v_nums[i + 1:])

    _dfs([], nums)
    return result


# 将多维列表展开成一维
def flatten(lists):
    '''
    :param lists: 传入的多维列表
    '''
    new_list = []
    for element in lists:
        if not isinstance(element, list):
            new_list.append(element)
        else:
            new_list.extend(flatten(element))

    return new_list


def duplicates(lists):
    '''
    :param lists:
    :return: 原序去重
    '''
    if not is_type(lists, (list, tuple)):
        raise TypeError("input data should be list or tuple")
    return list(OrderedDict.fromkeys(lists).keys())


def topn(lists, n, value_only=False):
    '''
    :param lists:
    :param n: 需要返回的list中最高频次元素的个数
    :param value_only: 只返回值
    :return:
    '''
    if not is_type(lists, (list, tuple)):
        raise TypeError("input data should be list or tuple")
    if value_only:
        return [val[0] for val in Counter(lists).most_common(n)]
    return Counter(lists).most_common(n)


def getindex(l, flag="max"):
    '''
    :param l:
    :param flag:max/min
    :return: 返回list中最大/最小元素的位置
    '''
    if not is_type(l, (list, tuple)):
        raise TypeError("input data should be list or tuple")
    if flag.strip() == "max":
        return max(range(len(l)), key=l.__getitem__)
    elif flag.strip() == "min":
        return min(range(len(l)), key=l.__getitem__)
    else:
        return "Flag Error"
