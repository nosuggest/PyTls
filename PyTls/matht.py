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


def entropy(props, type="list", explation=False):
    '''
    :param props:输入数据
    :param type:"list"是实验出现的结果，和非1；"prob"是实验结果出现的频率，和为1
    :param explation:是否提示结果的大小稳定度解释
    :return:
    '''
    if explation:
        print("the more the unstable")
    if type not in ("list", "prob"):
        raise ValueError("type should be list or prob,list be the expriment")
    if type == "list":
        if is_type(props, (list)):
            prop = set(props)
            resultEn = 0
            for single in prop:
                pi = Pi(single, props)
                resultEn -= pi * math.log(pi)
            return resultEn
        elif is_type(props, (float, int)):
            return -props * math.log(props)
    else:
        resultEn = 0
        for pi in props:
            resultEn -= pi * math.log(max(pi, __EPS))
        return resultEn

    raise TypeError


def condition_entropy(datax, datay, type="list", explation=False):
    '''
    :param datax:
    :param datay:
    :param type:"list"是实验出现的结果，和非1；"prob"是实验结果出现的频率，和为1
    :return:H(X/Y)，条件熵，已知Y的情况下，X的不稳定性
    :test：
    condition_entropy([1,0,1,0],[2,3,2,3])------>__EPS
    condition_entropy([1,1,0,0],[2,3,2,3])------>0.6931471805599453
    '''
    if explation:
        print("the less the better")
    if len(datax) != len(datay):
        raise ValueError("datax and datay shoule be the same length")
    if type not in ("list", "prob"):
        raise ValueError("type should be list or prob,list be the expriment")
    resultConEn = 0  # 最终条件熵H(X|Y)
    if type == "list":
        YElements = list(set(datay))
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
    else:
        for i in range(len(datax)):
            resultConEn += datax[i] * math.log(max(datax[i] / max(datay[i], __EPS), __EPS))
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


class BM25(object):
    """docstring for BM25"""

    def __init__(self, docs):
        self.docs = docs
        self.idf = {}
        # document frequenty
        self.df = {}
        # 每个doc中每个word的出现次数frequency
        self.f = []
        # 文章个数，平均文章长度
        self.D = len(self.docs)
        self.avgdl = sum(len(doc) for doc in self.docs) / self.D
        # 可调参数
        self.k1 = 1
        self.b = 0.75

        self.init()

    def init(self):
        for doc in self.docs:

            tmp = {}
            for word in doc:
                tmp[word] = tmp.get(word, 0) + 1
            self.f.append(tmp)

            for key in tmp.keys():
                self.df[key] = self.df.get(key, 0) + 1

        for k, v in self.df.items():
            self.idf[k] = math.log(self.D + 0.5) - math.log(v + 0.5)

    def relation(self, doc, index):
        score = 0
        for word in doc:
            if word not in self.f[index]:
                continue
            doc_len = len(self.docs[index])
            fi = self.f[index].get(word)
            score += (self.idf.get(word) * fi * (self.k1 + 1)) / (
                fi + self.k1 * (1 - self.b + self.b * (doc_len / self.avgdl)))
        return score

    def similarity(self, doc):
        scores = []
        for i in range(self.D):
            score = self.relation(doc, i)
            scores.append(score)
        return scores


def JSD(prob1, prob2):
    if len(prob1) != len(prob2):
        raise ValueError("input shoule be the same length")
    prob1_norm = sum(abs(p) for p in prob1)
    prob2_norm = sum(abs(p) for p in prob2)
    prob1 = [p / prob1_norm for p in prob1]
    prob2 = [p / prob2_norm for p in prob2]
    middle = [(prob1[idx] + prob2[idx]) / 2 for idx in range(len(prob1))]
    return 0.5 * (condition_entropy(prob1, middle, "prob") + condition_entropy(prob2, middle, "prob"))
