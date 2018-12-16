# -*- coding: utf-8 -*-
__author__ = 'HeYang'
__time__ = '2018/9/9 0:56'

from pyecharts import Gauge

gauge = Gauge('仪表盘')
gauge.add('CPU监控图/每秒', 'CPU负载', [60])
gauge.render()