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
print (w.search_word("t"))
print (w.search_word(["times"]))

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
matht.entropy([0.2, 0.1, 0.7])
matht.condition_entropy([1, 2, 1, 2], [1, 1, 0, 0])
matht.MI([1, 2, 1, 2], [1, 1, 0, 0])
matht.NMI([1, 2, 1, 2], [1, 1, 0, 0])
matht.word_edit_distince("am","are")

###################################################################################################################################################

from PyTls import listt

list_map = listt.index_hash_map([1, 2, 3])
list_map.get(1)

listt.Pi(1, [1, 2, 3])

listt.single_one([1, 1, 2, 3, 2])

listt.subset([1, 2])

listt.permute([1,2])

listt.flatten([[1,3,4],[[4]]])

listt.duplicates([4,1,3,3,6])

listt.topn([1,3,3,4],1)

listt.getindex([1,3,3,2,6,2],flag="max")

listt.split([1,2,3,4,5,6],number=2)

listt.unzip([[1,2],[3,4]])