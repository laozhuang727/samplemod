# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 16日

# 有多种文件的读取方法
# 支持格式转换
# 支持最终输出

def get_text():
    return "plain-text"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


def convert_to_other_format(data, new_format):
    print u'Convert {} from into {}'.format(data, new_format)


def save(data):
    print('Save file')


def template_function(getter, converter=None, saver=None):
    data = getter()
    print("Got `{}` format data".format(data))

    if converter:
        convert_to_other_format(data, ".bin")

    if saver:
        save(data)

    print("`{}` was processed".format(data))


if __name__ == '__main__':
    template_function(get_csv, converter=convert_to_other_format, saver=save)
