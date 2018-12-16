# -*- coding: utf-8 -*-
__author__ = 'HeYang'
__time__ = '2018/9/9 1:47'


# 仪表盘
# 每秒/CPU负载

from pyecharts import Gauge
from pyecharts import Pie
import psutil
import time
import datetime

# 获取每秒CPU负载


def cpu_info(times):
    time.sleep(times)
    cpu_percent = psutil.cpu_percent()
    return cpu_percent


def ybp_cpu_load(location='/var/www/html/index.html'):
    gauge = Gauge('CPU负载图')
    gauge.add('CPU负载/每秒/%s' % datetime.datetime.now().strftime('%H:%M:%S') , 'CPU负载', cpu_info(1))
    gauge.render(location)


def mem_info(times):
    time.sleep(times)
    mem_obj = psutil.virtual_memory()
    return mem_obj.used, mem_obj.free


def bt_mem(location='/var/www/html/index.html'):
    attr = ['已使用内存/单位M', '剩余内存/单位M']
    userd, free = mem_info(1)
    data = [userd/1024/1024, free/1024/1024]
    print data
    pie = Pie('内存监控图/%s' % datetime.datetime.now().strftime('%H:%M:%S'))
    pie.add('内存情况', attr, data)
    pie.render(location)


if __name__ == '__main__':
    while True:
        bt_mem()