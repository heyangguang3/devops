# -*- coding: utf-8 -*-
__author__ = 'HeYang'
__time__ = '2018/9/9 1:10'

from pyecharts import Pie

attr = ['已使用内存', '未使用内存']
data = ['1000', '2560']

pie = Pie('饼图')
pie.add('内存使用情况', attr, data, rosetype='area')
pie.render()