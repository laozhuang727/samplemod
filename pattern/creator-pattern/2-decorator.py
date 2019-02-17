# -*- coding: utf-8 -*-  
# __author__ = 'ryan.zhuang'
# 2019 02月 15日

"""
*What is this creator-pattern about?
The Decorator creator-pattern is used to dynamically add a new feature to an
object without changing its implementation. It differs from
inheritance because the new feature is added only to that particular
object, not to the entire subclass.
*What does this example behavior?
This example shows a way to add formatting options (boldface and
italic) to a text by appending the corresponding tags (<b> and
<i>). Also, we can see that decorators can be applied one after the other,
since the original text is passed to the bold wrapper, which in turn
is passed to the italic wrapper.
*Where is the creator-pattern used practically?
The Grok framework uses decorators to add functionalities to methods,
like permissions or subscription to an event:
http://grok.zope.org/doc/current/reference/decorators.html
*References:
https://sourcemaking.com/design_patterns/decorator
*TL;DR80
Adds behaviour to object without affecting its class.
"""


class TextTag(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BlobTag(TextTag):
    def __init__(self, wrapped_obj):
        self.__wrapped_obj = wrapped_obj

    def render(self):
        return "<b>{}</b>".format(self.__wrapped_obj.render())


class ItalicWrapper(TextTag):
    def __init__(self, wrapped_obj):
        self.__wrapped_obj = wrapped_obj

    def render(self):
        return "<I>{}</I>".format(self.__wrapped_obj.render())


if __name__ == '__main__':
    ori_text = TextTag("hello")
    blob_text = BlobTag(ori_text)
    italic_blob_text = ItalicWrapper(blob_text)

    print("before:", ori_text.render())
    print("after:", italic_blob_text.render())
