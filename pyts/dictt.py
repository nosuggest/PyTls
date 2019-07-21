#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : dictt.py
@Author: sladesha
@Date  : 2019/7/21 16:00
@Desc  : 
'''
from typet import is_type


def get_map_value(data, default=None, is_last=True, *argv):
    '''
    :param data: 待查找字典
    :param default: 默认值
    :param is_last: 是否需要查找到底层
    :param argv: 需查找字段
    :return:
    '''
    if not is_type(data, dict):
        return TypeError("input data should be dict")
    node = data
    for name in argv:
        if node.get(name):
            node = node.get(name)
        else:
            return default
    if is_last:
        return node if not is_type(node, dict) else default
    else:
        return node


def update_map_value(d, is_strict=True, **kw):
    '''
    :param d: 待变更数据
    :param is_strict: 是否允许新增
    :param kw: "money" = 3，对应为字典形式
    :return:
    '''
    if d is None:
        raise ValueError('input data should not be none !')
    if isinstance(d, dict):
        for key, val in kw.items():
            if is_strict:
                if d.get(key):
                    d[key] = val
            else:
                d[key] = val
    elif isinstance(d, object):
        for key, val in kw.items():
            if is_strict:
                if hasattr(key):
                    setattr(d, key, val)
            else:
                setattr(d, key, val)
    return True
