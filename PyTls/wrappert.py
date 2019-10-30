#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 10:11 PM
# @Author  : Slade
# @File    : wrappert.py
import time



def timespend(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('params:%r (%r, %r); total spend time : %2.2f sec' % (method.__name__, args, kw, te - ts))
        return result

    return timed


