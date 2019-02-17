# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 14日

def square(x):
    """返回 x 的平方。

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x


if __name__ == '__main__':
    import doctest

    doctest.testmod()
