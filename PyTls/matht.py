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
from math import log
from math import e

__EPS = 1.4e-45


def entropy(props, explation=False):
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


def condition_entropy(datax, datay, explation=False):
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


def MI(A, B, explation=False):
    if explation:
        print("the more the better")
    return entropy(A) - condition_entropy(A, B)


def NMI(A, B, explation=False):
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


def ln(num):
    return log(num, e)


def word_edit_distince(str1, str2):
    # 构造(len(str1)+1) x (len(str2)+1)的矩阵，其中+1是为了考虑str1或者st2为空的情况
    matrix = [[i + j for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # 注意这边从1开始，所以比target和source的时候需要考虑-1
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            # 上侧，左侧，左上侧
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    return matrix[len(str1)][len(str2)]
