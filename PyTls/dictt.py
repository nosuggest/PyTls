#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : dictt.py
@Author: sladesha
@Date  : 2019/7/21 16:00
@Desc  : 
'''
from .typet import is_type
import collections
from functools import reduce
from collections import defaultdict
import sys
import json

__all__ = ["get_map_value", "update_map_value", "sort_map_key", "sort_map_value", "get_tree", "swap", "merge",
           "func_dict", "WordCount"]


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
        if is_type(node.get(name), (dict, str, int, list, tuple)):
            node = node.get(name)
        else:
            return default
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


def sort_map_key(d, desc=False):
    return sorted(d.items(), key=lambda x: x[0], reverse=desc)


def sort_map_value(d, desc=True):
    return sorted(d.items(), key=lambda x: x[1], reverse=desc)


def get_tree():
    tree = lambda: collections.defaultdict(tree)
    return tree()


def swap(d):
    if len(d) != len(set(d.values())):
        raise ValueError("value has the same")
    return {v: k for k, v in d.items()}


def merge(d1, d2):
    return dict(d1.items() | d2.items())


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def func_dict(func):
    return keydefaultdict(func)


class tire():
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class WordCount():
    def __init__(self):
        self.root = tire()

    def add_word(self, words):
        node = self.root
        for word in words:
            if word not in node.children:
                node.children[word] = tire()
                node.count += 1
            node = node.children[word]
        node.is_end = True

    def search_word(self, words):
        if sys.version_info >= (3, 2):
            from functools import lru_cache
            @lru_cache()
            def dfs(node, i=0):
                if i == len(words):
                    return node.is_end
                if words[i] in node.children:
                    return dfs(node.children[words[i]], i + 1)
                return False
        else:
            def dfs(node, i=0):
                if i == len(words):
                    return node.is_end
                if words[i] in node.children:
                    return dfs(node.children[words[i]], i + 1)
                return False
        node = self.root
        return dfs(node, 0)


def __replace_quote__(json_str):
    double_quote = []
    new_list = []
    for index, val in enumerate(json_str):
        if val == '"' and json_str[index - 1] != "\\":
            if double_quote:
                double_quote.pop(0)
            else:
                double_quote.append(val)
        if val == "'" and json_str[index - 1] != "\\":
            if not double_quote:
                val = '"'
        new_list.append(val)
    return "".join(new_list)


def json_loads(json_str, defaulttype=dict, escape=True):
    if not json_str:
        return defaulttype()
    elif escape:
        return json.loads(__replace_quote__(json_str))
    else:
        return json.loads(json_str)
