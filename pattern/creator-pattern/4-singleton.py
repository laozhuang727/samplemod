# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日


def singleton_decorator(cls):
    """定义一个单例装饰器"""
    instance = {}

    def wrapper_singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper_singleton


@singleton_decorator
class SingletonDemo:
    def __init__(self, name):
        self._name = name



if __name__ == '__main__':
    tony = SingletonDemo("tony")
    karry = SingletonDemo("karry")

    print(tony._name, karry._name)
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry?:", tony == karry)
