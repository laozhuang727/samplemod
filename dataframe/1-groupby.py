# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日

from operator import itemgetter  # itemgetter用来去dict中的key，省去了使用lambda函数
from itertools import groupby  # itertool还包含有其他很多函数，比如将多个list联合起来。。
import pandas as pd

d1 = {'name': 'zhangsan', 'age': 20, 'country': 'China'}
d2 = {'name': 'wangwu', 'age': 19, 'country': 'USA'}
d3 = {'name': 'lisi', 'age': 22, 'country': 'JP'}
d4 = {'name': 'zhaoliu', 'age': 22, 'country': 'USA'}
d5 = {'name': 'pengqi', 'age': 22, 'country': 'USA'}
d6 = {'name': 'lijiu', 'age': 22, 'country': 'China'}
data_list = [d1, d2, d3, d4, d5, d6]


def list_to_dataframe():
    df = pd.DataFrame(data_list)
    print(df)


# 通过country进行分组：
def test_group_by_country():
    country_group = groupby(data_list, itemgetter('country'))
    for key, group in country_group:
        for g in group:  # group是一个迭代器，包含了所有的分组列表
            print key, g


def test_dataframe_group():
    df = pd.DataFrame(data_list)
    for name, group in df.groupby('age'):
        print name
        print group


def test_dataframe_to_list():
    df = pd.DataFrame(data_list)
    for name, group in df.groupby('age'):
        print name
        a_list = group.values
        print a_list


if __name__ == '__main__':
    list_to_dataframe()
