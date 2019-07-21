#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : matht.py
@Author: sladesha
@Date  : 2019/7/22 0:15
@Desc  : 
'''

import math
from .typet import is_type
import sys


__EPS = 1.4e-45


def entropy(props):
    if is_type(props, (list)):
        return sum(-prop * math.log2(prop) for prop in props)
    elif is_type(props, (float, int)):
        return -props * math.log2(props)
    raise TypeError


def NMI(A,B):
    #样本点数
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    #互信息计算
    MI = 0
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A==idA)
            idBOccur = np.where(B==idB)
            idABOccur = np.intersect1d(idAOccur,idBOccur)
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*math.log(pxy/(px*py)+__EPS,2)
    # 标准化互信息
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(np.where(A==idA)[0])
        Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+__EPS,2)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(np.where(B==idB)[0])
        Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+__EPS,2)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

