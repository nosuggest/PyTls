# PyTls

python工具合集，用来快速复用，极致执行

+ __init__.py
+ dictt.py
    + [get_map_value()](PyTls/dictt.py#L12)
    字典迭代取值
    + [update_map_value()](PyTls/dictt.py#L34)
    + [sort_map_key()](PyTls/dictt.py#L60)
    + [sort_map_value()](PyTls/dictt.py#64)
    字典排序
+ StrBuffer.py
参考java中的StringButter
    + [append()](PyTls/StrBuffer.py#22)
    + [index_at()](PyTls/StrBuffer.py#37)
    + [sort()](PyTls/StrBuffer.py#47)
    + [reverse()](PyTls/StrBuffer.py#50)
    + [char_at()](PyTls/StrBuffer.py#53)
    + [to_str()](PyTls/StrBuffer.py#58)
    + [storge()](PyTls/StrBuffer.py#64)
+ strt.py
    + [str_reverse()](PyTls/strt.py#14)
    + [str_repeat()](PyTls/dictt.py#18)
    + [str_splits()](PyTls/dictt.py#29)
    字符串批切割
+ typet.py
    + [is_none()](PyTls/strt.py#11)
    + [is_type()](PyTls/dictt.py#15)
    + [is_empty()](PyTls/dictt.py#25)
    + [is_has_attr()](PyTls/dictt.py#35)
+ loaddatat.py
    + [readbunchobj()](PyTls/loaddatat.py#13)
    + [writebunchobj()](PyTls/loaddatat.py#19)
    读存数据
+ randomt.py
    + [get_random()](PyTls/randomt.py#32)
+ Chinese2num.py
数字相关，提取数字更加强大的功能建议参考[YMMNlpUtils](https://github.com/sladesha/machine_learning/blob/master/YMMNlpUtils/YMMNlpUtils/YMMNlpUtils.py)
    + [Chinese_2_num()](PyTls/Chinese2num.py#20)
    + [ln()](PyTls/Chinese2num.py#29)
    + [isdigit()](PyTls/Chinese2num.py#33)
+ matht.py
    + [entropy()](PyTls/matht.py#14)
    + [condition_entropy()](PyTls/matht.py#33)
    + [MI()](PyTls/matht.py#60)来自于条件概率计算法：H(x)-H(x/y)
    + [NMI()](PyTls/matht.py#66)来自于公式计算：2`*`∑pxylog(pxy/(px`*`py))/(H(x)+H(y))
+ listt.py    
    + [index_hash_map()](PyTls/listt.py#10)list元素出现位置，等同于numpy array中的`np.where`
    + [Pi()](PyTls/listt.py#26)