# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日

class Building(object):
    def __init__(self):
        self._floor = None
        self._size = None

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0._floor} | Size: {0._size}'.format(self)


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()

    return building


# Concrete buildings
class House(Building):
    def build_floor(self):
        self._floor = 'One'

    def build_size(self):
        self._size = 'big'


class Flat(Building):
    def build_floor(self):
        self._floor = "10"

    def build_size(self):
        self._size = 'small'


if __name__ == '__main__':
    house = construct_building(House)
    print(house)
    flat = construct_building(Flat)
    print(flat)
