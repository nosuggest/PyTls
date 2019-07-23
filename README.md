# PyTls
<p align="center">
<img src="https://img.shields.io/pypi/v/PyTls.svg"></a>
</p>
python工具合集，用来快速复用，极致执行，欢迎试用

+ __init__.py
+ dictt.py
    + [get_map_value()](PyTls/dictt.py#L12)
    字典迭代取值
    + [update_map_value()](PyTls/dictt.py#L34)
    + [sort_map_key()](PyTls/dictt.py#L60)
    + [sort_map_value()](PyTls/dictt.py#L64)
    字典排序
+ StrBuffer.py
参考java中的StringButter
    + [append()](PyTls/StrBuffer.py#L22)
    + [index_at()](PyTls/StrBuffer.py#L37)
    + [sort()](PyTls/StrBuffer.py#L47)
    + [reverse()](PyTls/StrBuffer.py#L50)
    + [char_at()](PyTls/StrBuffer.py#L53)
    + [to_str()](PyTls/StrBuffer.py#L58)
    + [storge()](PyTls/StrBuffer.py#L64)
+ strt.py
    + [str_reverse()](PyTls/strt.py#L14)
    + [str_repeat()](PyTls/dictt.py#L18)
    + [str_splits()](PyTls/dictt.py#L29)
    字符串批切割
+ typet.py
    + [is_none()](PyTls/strt.py#L11)
    + [is_type()](PyTls/dictt.py#L15)
    + [is_empty()](PyTls/dictt.py#L25)
    + [is_has_attr()](PyTls/dictt.py#L35)
+ loaddatat.py
    + [readbunchobj()](PyTls/loaddatat.py#L13)
    + [writebunchobj()](PyTls/loaddatat.py#L19)
    读存数据
+ randomt.py
    + [get_random()](PyTls/randomt.py#L32)
+ Chinese2num.py
数字相关，提取数字更加强大的功能建议参考[YMMNlpUtils](https://github.com/sladesha/machine_learning/blob/master/YMMNlpUtils/YMMNlpUtils/YMMNlpUtils.py)
    + [Chinese_2_num()](PyTls/Chinese2num.py#L20)
    + [ln()](PyTls/Chinese2num.py#L29)
    + [isdigit()](PyTls/Chinese2num.py#L33)
+ matht.py
    + [entropy()](PyTls/matht.py#L14)
    + [condition_entropy()](PyTls/matht.py#L33)
    + [MI()](PyTls/matht.py#L60)来自于条件概率计算法：H(x)-H(x/y)
    + [NMI()](PyTls/matht.py#L66)来自于公式计算：2`*`∑pxylog(pxy/(px`*`py))/(H(x)+H(y))
+ listt.py    
    + [index_hash_map()](PyTls/listt.py#L10)list元素出现位置，等同于numpy array中的`np.where`
    + [Pi()](PyTls/listt.py#L26)
    + [single_one()](PyTls/listt.py#L38)从list找出非两两成对的单样本
    + [subset()](PyTls/listt.py#L44)子集
    + [permute()](PyTls/listt.py#L56)全排列
    + [flatten()](PyTls/listt.py#L70)高维列表展开
    + [duplicates()](PyTls/listt.py#L85)原序去重
    + [topn()](PyTls/listt.py#L95)高频统计
    + [getindex()](PyTls/listt.py#L109)返回list中最大/最小元素的位置
    