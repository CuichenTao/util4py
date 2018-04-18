#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime

"""
日期工具
"""

def get_date():
    """获取今日日期
    格式: 20171213
    """
    return time.strftime("%Y%m%d")

def get_timestamp():
    """获取当前时间戳
    格式: 1524032735404
    """
    return int(round(time.time() * 1000))

def formatTime(timestamp):
    """格式化时间戳
    格式: 2017-12-13 16:32:30
    """
    time_local = time.localtime(timestamp / 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)

def get_time():
    """获取当前时间
    => 格式: '2017-12-13 16:32:30'
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_time_before(days=0,hours=0,minutes=0,seconds=0,microseconds=0):
    """获取时间偏移数据
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :param microseconds:
    :return: 获取当前时间戳=> 格式: '2017-12-13 16:32:30'
    """
    res = datetime.datetime.now() - datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)
    return res.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print(get_time_before(minutes=10))


