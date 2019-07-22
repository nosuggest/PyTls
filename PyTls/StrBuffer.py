#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : StrBuffer.py
@Author: sladesha
@Date  : 2019/7/21 17:19
@Desc  : 
'''
from .typet import is_type

class StrBuffer(object):

    '''
    编写类似java stringbuilder 工具类 ，
    将字符串扩展变的容易简单
    '''

    def __init__(self, content=None):
        if  is_type(content,str):
            self.__buf = list(content)

    def append(self, line):
        '''
        字符串追加，如果是string，会分片存储
        '''
        if line == None:
            raise ValueError('append value is None !')
        if isinstance(line, (str, list, tuple)):
            self.__buf.extend(line)
            return
        raise TypeError('append function can accept value\'s is list str tuple ')

    def __add__(self, line):
        self.append(line)
        return self

    def index_at(self, value):
        if not is_type(value,str):
            raise ValueError("now type is %s but %s is needed" % (type(value).__name__, str.__name__))
        if len(value) > len(self.__buf):
            return -1
        return self.__buf.index(value)

    def __len__(self):
        return len(self.__buf)

    def sort(self,reverse=False):
        self.__buf.sort(reverse=reverse)

    def reverse(self):
        return str(''.join(self.__buf))[::-1]

    def char_at(self, index):
        if not is_type(index,int):
            raise ValueError("now type is %s but %s is needed" % (type(index).__name__, int.__name__))
        return self.__buf[index]

    def to_str(self, join_str=''):
        return join_str.join(self.__buf)

    def __str__(self):
        return self.to_str()

    def storge(self):
        return self.__buf

    def __getitem__(self, key):
        return self.char_at(key)

    def __eq__(self, val):
        if val == None:
            return False
        if isinstance(val, list):
            return self.__buf == val
        elif isinstance(val, StrBuffer):
            return self.__buf == val.storge()
        elif isinstance(val, str):
            return self.to_str() == val
        return False