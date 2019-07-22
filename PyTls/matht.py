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
from .listt import index_hash_map, Pi

__EPS = 1.4e-45


def entropy(props, explation=True):
    if explation:
        print("the more the unstable")
    if is_type(props, (list)):
        prop = set(props)
        resultEn = 0
        for single in prop:
            pi = Pi(single, props)
            resultEn -= pi * math.log2(pi)
        return resultEn
    elif is_type(props, (float, int)):
        return -props * math.log2(props)
    raise TypeError


def condition_entropy(datax, datay, explation=True):
    '''
    :param datax:
    :param datay:
    :return:H(X/Y)，条件熵，已知Y的情况下，X的不稳定性
    :test：
    condition_entropy([1,0,1,0],[2,3,2,3])------>__EPS
    condition_entropy([1,1,0,0],[2,3,2,3])------>1
    '''
    if explation:
        print("the less the better")
    YElements = list(set(datay))
    resultConEn = 0  # 最终条件熵H(X|Y)
    index_map = index_hash_map(datay)
    for uniqueYEle in YElements:
        YIndex = index_map.get(uniqueYEle)
        # 找出dataY 里所有等于yi = YElements的索引值组成的列表
        dataX_Y = []
        # 拿出datax对应的index下的值
        for idx in YIndex:
            dataX_Y.append(datax[idx])
        HX_uniqueYEle = max(entropy(dataX_Y), __EPS)  # H（X|Y=yi)
        pi = max(__EPS, Pi(uniqueYEle, datay))  # 此时可以计算 pi = p(Y=yi)
        resultConEn += pi * HX_uniqueYEle  # 求和 H（X|Y）= Σ p(Y=yi)*H（X|Y=yi)
    return resultConEn  # 返回条件熵 H（X|Y）


def MI(A, B, explation=True):
    if explation:
        print("the more the better")
    return entropy(A) - condition_entropy(A, B)


def NMI(A, B, explation=True):
    if explation:
        print("the more the better")
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    A_index_map = index_hash_map(A)
    B_index_map = index_hash_map(B)
    # 互信息计算
    MI = 0
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = A_index_map.get(idA)
            idBOccur = B_index_map.get(idB)
            idABOccur = list(set(idAOccur) & set(idBOccur))
            px = 1.0 * len(idAOccur) / total
            py = 1.0 * len(idBOccur) / total
            pxy = 1.0 * len(idABOccur) / total
            MI = MI + pxy * math.log(pxy / (px * py) + __EPS, 2)
    # 标准化互信息
    Hx = entropy(A)
    Hy = entropy(B)
    MIhat = 2.0 * MI / (Hx + Hy)
    return MIhat
