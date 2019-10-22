#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 1:55 PM
# @Author  : Slade
# @File    : textt.py
import pypinyin
from pypinyin import pinyin
import re


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if len(uchar) != 1:
        raise ValueError("单个字符判断")
    if '\u4e00' <= uchar <= '\u9fa5':
        return True
    else:
        return False


def is_chinese_string(string):
    """判断是否全为汉字"""
    for c in string:
        if not is_chinese(c):
            return False
    return True


def is_number(uchar):
    """判断一个unicode是否是数字"""
    if len(uchar) != 1:
        raise ValueError("单个字符判断")
    if '\u0030' <= str(uchar) <= '\u0039':
        return True
    else:
        return False


def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if len(uchar) != 1:
        raise ValueError("单个字符判断,多个字符请用is_alphabet_string")
    if ('\u0041' <= uchar <= '\u005a') or ('\u0061' <= uchar <= '\u007a'):
        return True
    else:
        return False


def is_alphabet_string(string):
    """判断是否全为字母"""
    for c in string:
        if not is_alphabet(c):
            return False
    return True


def stringB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # 半角空格直接转化
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:  # 半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring


def stringQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring


def remove_punctuation(strs):
    """
    去除标点符号
    :param strs:
    :return:
    """
    return re.sub("[\s+\.\!\/<>“”,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", strs.strip())


def uniform(ustring, punc=True):
    """格式化字符串，完成全角转半角，大写转小写的工作"""
    if punc:
        return remove_punctuation(stringQ2B(ustring).lower())
    else:
        return stringQ2B(ustring).lower()


def get_homophones_by_char(input_char, start=0x4e00, end=0x9fa5):
    """
    根据汉字取同音字
    :param input_char:
    :return:
    """
    if len(input_char) > 1:
        raise ValueError("single char please")
    result = []
    for i in range(start, end + 1):
        if pinyin([chr(i)], style=pypinyin.NORMAL)[0][0] == pinyin(input_char, style=pypinyin.NORMAL)[0][0]:
            result.append(chr(i))
    return result


def get_homophones_by_pinyin(input_pinyin, types=1, start=0x4e00, end=0x9fa5):
    """
    根据拼音取同音字
    :param input_pinyin:
    :param type:{1:zhong,0:zho1ng}
    :return:
    """
    result = []

    if types:
        style = pypinyin.NORMAL
    else:
        style = pypinyin.TONE2

    for i in range(start, end + 1):
        if pinyin([chr(i)], style=style)[0][0] == input_pinyin:
            # TONE2: 中zho1ng
            result.append(chr(i))
    return result


class _Node():
    def __init__(self):
        self.is_four_area = False
        self.children = {}


class LocationTire(object):
    def __init__(self):
        self.root = _Node()
        self.level4_area = None

    def insert(self, areas):
        node = self.root
        tmp_level = 0
        for area in areas:
            tmp_level += 1
            if area not in node.children:
                child = _Node()
                if tmp_level == 4:
                    child.is_four_area = True
                node.children[area] = child
                node = child
            else:
                node = node.children[area]

    def search(self, areas):
        node = self.root
        for area in areas:
            if area in node.children:
                if node.children[area].is_four_area:
                    return area
                node = node.children[area]
            else:
                return " "
        return node.children.keys()

    def match(self, areas):
        node = self.root
        self.level4_area = None

        def dfs(node, idx):
            if idx == len(areas) - 1:
                return list(node.children.keys())[0]
            if areas[idx] == '.':
                for area in node.children.keys():
                    # print(dfs(node.children[area], idx + 1))
                    # print(areas[-1])
                    # print("---")
                    if dfs(node.children[area], idx + 1) == areas[-1]:
                        return area
            if areas[idx] in node.children:
                return dfs(node.children[areas[idx]], idx + 1)

        return dfs(node, 0)
