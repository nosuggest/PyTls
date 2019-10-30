#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 8:27 AM
# @Author  : Slade
# @File    : demos.py
import os

os.systerm('''pip install PyTls''')

from PyTls import dictt

# dictt.get_map_value()
msg = {'time': {'20190714': 234, '20190715': 311}}
dictt.get_map_value(msg, None, True, 'time', '20190714')

# dictt.update_map_value()
msg = {'time': '20190428'}
dictt.update_map_value(msg, True, time1="20190515")
print(msg)
dictt.update_map_value(msg, False, time1="20190515")
print(msg)

# dictt.sort_map_key()
msg = {11: 2, 2: 3, 9: 2}
print(dictt.sort_map_key(msg, desc=False))

# dictt.get_tree()
tree = dictt.get_tree()
tree["I"] = dictt.get_tree()
tree["I"]["am"] = dictt.get_tree()
tree["I"]["am"]["Chinese"] = True

# In [33]: tree
# Out[33]:
# defaultdict(<function PyTls.dictt.get_tree.<locals>.<lambda>>,
#             {'I': defaultdict(<function PyTls.dictt.get_tree.<locals>.<lambda>>,
#                          {'am': defaultdict(<function PyTls.dictt.get_tree.<locals>.<lambda>>,
#                                       {'Chinese': True})})})

# dictt.swap()
dictt.swap({1: 2})

# dictt.merge()
dictt.merge({1: 2}, {2: 3})

# dictt.func_dict()
F = dictt.func_dict(lambda x: x * 2)
print((F[2], F))

# dictt.WordCount()
w = dictt.WordCount()
w.add_word(["times"])
w.add_word("times")
print(w.search_word("t"))
print(w.search_word(["times"]))

# dictt.json_loads()
dictt.json_loads('{\'a\': 1, "b": "i\'m tom."}')

###################################################################################################################################################
from PyTls import StrBuffer

word = StrBuffer.StrBuffer("hello")
# 增加一个字符
word.append('s')
print(word.storge())
# 查找一个字符的位置
word.index_at("s")
# 排序
word.sort()
print(word.storge())
# 倒排
word.reverse()
# 查找某个index的元素
word.char_at("s")

###################################################################################################################################################

from PyTls import strt

# str_reverse()
strt.str_reverse("hello")

# strt.str_repeat()
strt.str_repeat("hello", 3)

# strt.str_splits()
strt.str_splits(words="helloword", split_chars=["e|o"])

# strt.judge_anagrams()
strt.judge_anagrams("cbaebabacd", "abc")

###################################################################################################################################################

from PyTls import typet

typet.is_none(None)
typet.is_none([])

typet.is_type("str", str)
typet.is_type(886, int)

typet.is_empty([])
typet.is_empty({})


class Tmp():
    def __init__(self):
        self.val = 0


tmp = Tmp()
typet.is_has_attr(tmp, "val")

###################################################################################################################################################
from PyTls import loaddatat

loaddatat.readbunchobj("你需要读取的文件")
loaddatat.writebunchobj("你需要保存的路径及名称", "你需要保存的内容")

###################################################################################################################################################

from PyTls import randomt

r = randomt.get_random(1, 10, 3)
for i in r:
    print(i)

###################################################################################################################################################

from PyTls import Chinese2num

Chinese2num.Chinese_2_num("八玖二叁七四")
Chinese2num.isdigit("0.234")

###################################################################################################################################################

from PyTls import matht
import math

matht.ln(math.e)
matht.entropy([1, 1, 2], "list")
matht.entropy([0.2, 0.1, 0.7], "prob")
matht.condition_entropy([1, 2, 1, 2], [1, 1, 0, 0])
matht.MI([1, 2, 1, 2], [1, 1, 0, 0])
matht.NMI([1, 2, 1, 2], [1, 1, 0, 0])
matht.word_edit_distince("am", "are")
bm = matht.BM25([["the", "world", "is", "cool"], ["the", "life", "is", "hard"]])
bm.similarity(["life", "is", "Beautiful"])
matht.relative_entropy([2 / 3, 1 / 3], [1 / 2, 1 / 2])
matht.cross_entropy([2 / 3, 1 / 3], [1 / 2, 1 / 2])
matht.JSD([2 / 3, 1 / 3], [1 / 2, 1 / 2])
matht.Hellinger_Distince([1 / 2, 1 / 2], [1 / 3, 2 / 3])
matht.isOdds(2)

###################################################################################################################################################

from PyTls import listt

list_map = listt.index_hash_map([1, 2, 3])
list_map.get(1)

listt.Pi(1, [1, 2, 3])

listt.single_one([1, 1, 2, 3, 2])

listt.subset([1, 2])

listt.permute([1, 2])

listt.flatten([[1, 3, 4], [[4]]])

listt.duplicates([4, 1, 3, 3, 6])

listt.topn([1, 3, 3, 4], 1)

listt.getindex([1, 3, 3, 2, 6, 2], flag="max")

listt.split([1, 2, 3, 4, 5, 6], number=2)

listt.unzip([[1, 2], [3, 4]])

c = listt.Contact("jack", "student")
c = listt.Contact("mika", "teacher")
c = listt.Contact("slade", "student")
'''
# c中存储着key，value对
In [18]: [item for item in c.contactlist.search("mika")]
Out[18]: ['teacher']

In [19]: c
Out[19]: <__main__.Contact at 0x277d1489a58>

In [21]: c.contactlist
Out[21]:
[<__main__.Contact at 0x277d1489a58>,
 <__main__.Contact at 0x277d1358ef0>,
 <__main__.Contact at 0x277d156ae80>]

# 重置操作
In [23]: c.reload()

In [25]: c.contactlist
Out[25]: []

In [26]: Contact.contactlist
Out[26]: []
'''
###################################################################################################################################################

from PyTls import trickt
import time


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


param1 = 2
param2 = 1
trickt.choose_method(add, subtract, param1 > param2, param1, param2)
trickt.choose_method(add, subtract, param1 < param2, param1, param2)

with trickt.Timer():
    time.sleep(2)

###################################################################################################################################################
from PyTls import textt

textt.is_chinese("是")
textt.is_chinese_string("全部都是汉字")
textt.is_number(2)
textt.is_alphabet("asddw奥迪")
textt.is_alphabet_string("asddw奥迪")
textt.stringB2Q("你干么!d7&888学英 语ABC?nz")
textt.stringQ2B("你干么！ｄ７＆８８８学英 语ＡＢＣ？ｎｚ")
textt.remove_punctuation("这里的。需要被去掉")
textt.uniform("格式化字符串，完成全角转半角，大写转小写的工作")
textt.get_homophones_by_char("我的")
textt.get_homophones_by_pinyin("zho1ng", 0)
textt.get_homophones_by_pinyin("zhong", 1)

t = textt.LocationTire()
t.insert(["江苏", "南京", "雨花", "铁心桥", "A座"])
t.insert(["江苏", "南京", "雨花", "软件大道", "B座"])
t.insert(["江苏", "南京", "雨花", "雨花客厅", "C座"])
print(t.match(["江苏", "南京", "雨花", ".", "C座"]))
print(t.search(["江苏", "南京", "雨花"]))

###################################################################################################################################################
from PyTls import wrappert


@wrappert.timespend
def add(a, b):
    return a + b
