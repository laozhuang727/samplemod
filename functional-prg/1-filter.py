# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日

# reference: https://www.seoxiehui.cn/article-69259-1.html
if __name__ == '__main__':
    # 可以看到，我们给列表中的每个元素应用了一个函数。那么怎样才能实现过滤呢？先来看看之前的这段代码：
    num_list = range(-5, 5)

    print(list(filter(lambda x: x < 0, num_list)))  # normal
    print([num for num in num_list if num < 0])  # good

    # 如果想求所有小于0的数字的平方呢？使用Lambda、映射和过滤可以写成：
    print(list(map(lambda x: x * x, filter(lambda x: x < 0, num_list))))  # normal
    print([num * num for num in num_list if num < 0])  # good

    # 将字典中的tuple value转为大写
    count_dict = [
        ("86", "China"),
        ("91", "India"),
        ("1", "Unite State"),
    ]

    print(count_dict)

    dict = {code: country for code, country in count_dict}
    print(dict)

    converted_from_list = {code: country.upper() for code, country in count_dict}
    print(converted_from_list)

    # 对于dict的循环处理
    converted_from_dict = {code: country.upper() + "0000" for code, country in dict.items()}
    print(converted_from_dict)
