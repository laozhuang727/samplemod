# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日

class Order(object):
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self._discount_strategy = discount_strategy

    def get_discount_price(self):
        if self._discount_strategy:
            discount_amt = self._discount_strategy(self)
        else:
            discount_amt = 0

        return self.price - discount_amt

    def __repr__(self):
        fmt = "<Price : {}, price after discount: {}\n"
        return fmt.format(self.price, self.get_discount_price())


def ten_percent_discount(order):
    return order.price * 0.10


def on_sale_discount(order):
    return order.price * 0.25 + 20


if __name__ == '__main__':
    normal_order = Order(100)
    print(normal_order)

    order1 = Order(100, discount_strategy=ten_percent_discount)
    print(order1)
    order2 = Order(100, discount_strategy=on_sale_discount)

    print(order2)
