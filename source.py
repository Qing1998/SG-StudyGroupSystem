#!/user/bin/env python
#!-*-coding:utf-8 -*-
#!@Time     :2018/10/6 2018/10/6
#!@Author   :Qingslev
#!@File     :.py

class Member(object):
    def __init__(self,name,potato=2):
        self.name=name
        self.potato=potato
    def __str__(self):
        return 'Member: %s Potato:%s' %self.name %self.potato
