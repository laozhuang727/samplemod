# -*- coding: utf-8 -*-
# __author__ = 'ryan.zhuang'
# 2019 02月 17日
#
# 使用Counter进行计数统计
# reference : http://www.mamicode.com/info-detail-1527234.html

import unittest
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from collections import Counter


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    def test_init_counter(self):
        data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
        c = Counter(data)

        print(c)
        return c

    def test_print_elements(self):
        counter = self.test_init_counter()
        print(counter.elements)
        print(list(counter.elements()))

    # 在原基础上增加了计数值
    def test_update_counter(self):
        counter = self.test_init_counter()
        counter.update(['a', 'a', 'a', 'a'])
        print(counter)

    # 在原基础上减少计数值
    def test_update_counter(self):
        counter = self.test_init_counter()
        counter.subtract(['a', 'a', 'a', 'a'])
        print(counter)

    # 统计最高频的前n个
    def test_most_common(self):
        counter = self.test_init_counter()
        result = counter.most_common(2)
        print(result)

    # 集合操作+
    def test_collection_op(self):
        counter = self.test_init_counter()
        another_counter = Counter(['a', 'a'])

        print u"+操作后：", counter + another_counter  # counter[x] + another_counter[x]
        print u"-操作后：", counter - another_counter  # counter[x] + another_counter[x]

    # 集合操作交集， 并集
    def test_collection(self):
        counter = self.test_init_counter()
        another_counter = Counter(['a', 'a'])

        print u"交集后：", counter & another_counter  # counter[x] + another_counter[x]
        print u"并集后：", counter | another_counter  # counter[x] + another_counter[x]

    def test_other_op(self):
        c = self.test_init_counter()
        print u"keys：", c.keys()
        print u"has keys：", c.has_key('a')
        print u"get：", c.get('a')
        print u"items：", c.items()
        print u"values：", c.values()
        print u"viewitems：", c.viewitems()
        print u"viewkeys：", c.viewkeys()

    def test_init_tuple_counter(self):
        data = [('China', '老王'), ('China', '李四'), ('印度', '张三'), ('China', '老王')]
        c = Counter(data)

        # 注意list中的中文打印处理
        print(str(c).decode('string_escape'))
        return c


if __name__ == '__main__':
    unittest.main()
