#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import re


def get_date():
    '''
        获取今日日期=> 格式: '20171213'
    '''
    return time.strftime("%Y%m%d")


def get_timestamp():
    '''
        获取当前时间戳：　13位
    '''
    return int(round(time.time() * 1000))

def formatTime(timestamp):
    '''
        格式化时间戳
    :param timestamp:
    '''
    time_local = time.localtime(timestamp / 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)

def get_time():
    '''
        获取当前时间戳=> 格式: '2017-12-13 16:32:30'
    '''
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')