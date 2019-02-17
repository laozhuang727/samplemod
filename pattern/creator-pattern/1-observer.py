# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 14日

"""
监听器设计模式，https://gitbook.cn/gitchat/column/5a1c24de28554541fbc8f2e8/topic/5a1f8dfd211fa435d2b9cc5d
"""

from __future__ import print_function

import abc  # 利用abc模块实现抽象类


class Subject(object):
    """
    被观察者
    """

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        """
        通知所有的监听对象
        :param modifier: 修改发起者。 如果发现是它自个发起的，就不必通知它
        """
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)


class Observer(object):
    """观察者对象"""

    def update(self, subject):
        """
        当被观察者数据发生变化时，通知观察人员，
        :param subject: 被观察者
        """
        pass


# Example usage
class WaterHeater(Subject):
    """
    热水器，继承了监听对象
    """
    def __init__(self):
        super(WaterHeater,self).__init__()
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature
        print(u"最新水温调整为：", self._temperature)
        self.notify()


class WashMode(Observer):
    def update(self, subject):
        if 40 < subject._temperature < 70:
            print(u"洗澡模式收到通知！！ 水温刚刚好，可以洗澡了")


class DrinkMode(Observer):
    def update(self, subject):
        if subject._temperature > 100:
            print(u"饮水模式收到通知！！ 水开了，可以喝了")


if __name__ == '__main__':
    heater = WaterHeater()
    washMode = WashMode()
    drinkMode = DrinkMode()

    heater.add_observer(washMode)
    heater.add_observer(drinkMode)

    heater.set_temperature(10)
    heater.set_temperature(20)
    heater.set_temperature(30)
    heater.set_temperature(40)
    heater.set_temperature(50)
    heater.set_temperature(110)
