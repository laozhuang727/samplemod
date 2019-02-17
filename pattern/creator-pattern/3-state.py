# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 15日


class Context(object):
    def __init__(self):
        pass


class State(object):
    def __init__(self):
        self._min_temperature = None
        self._max_temperature = None

    def behavior(self, water):
        pass


# ======  Example from here  ======
class SolidState(State):
    def __init__(self):
        super(SolidState, self).__init__()
        self._min_temperature = -10000
        self._max_temperature = 0

    def behavior(self, water):
        print u"固体状态，坚硬如铁. 当前体温:", water._temperature


class WaterState(State):
    def __init__(self):
        super(WaterState, self).__init__()
        self._min_temperature = 0
        self._max_temperature = 100

    def behavior(self, water):
        print u"液体状态，如丝般柔滑. 当前体温:", water._temperature


class GasState(State):
    def __init__(self):
        super(GasState, self).__init__()
        self._min_temperature = 100
        self._max_temperature = 99999

    def behavior(self, water):
        print u"气体状态，透明不可见.当前体温:", water._temperature


class Water(Context):
    def __init__(self):
        super(Water, self).__init__()

        self._temperature = 40
        self._state = WaterState()

    def increase_temperature(self, incr_amount):
        self._temperature += incr_amount
        self.do_temperature_change()

    def decrease_temperature(self, decr_amount):
        self._temperature -= decr_amount
        self.do_temperature_change()

    def do_temperature_change(self):
        if self._temperature <= 0:
            self.change_state(SolidState())
        elif 0 < self._temperature < 100:
            self.change_state(WaterState())
        else:
            self.change_state(GasState())

    def change_state(self, new_state):
        self._state = new_state

    def behavior(self):
        self._state.behavior(self)


if __name__ == '__main__':
    water = Water()
    water.behavior()
    water.increase_temperature(30)
    water.behavior()
    water.increase_temperature(80)
    water.behavior()
    water.decrease_temperature(300)
    water.behavior()
