#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
list工具
"""

def flatten(a):
    """将多维数组转化成一维数组"""
    if not isinstance(a, (list, )):
        return [a]
    else:
        b = []
        for item in a:
            b += flatten(item)
    return b

def most_frequent_elem(a):
    """获取list中最频繁的元素"""
    return max(set(a), key = a.count)



if __name__ == '__main__':
    pass