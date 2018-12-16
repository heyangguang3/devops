# -*- coding: utf-8 -*-
__author__ = 'HeYang'
__time__ = '2018/9/9 1:15'

from pyecharts import Line

x_list = ['1s', '2s', '3s']
y_list = ['34', '8', '2']

line = Line('折线图')
line.add('CPU使用率', x_list, y_list)
line.render('/var/www/html/index.html')