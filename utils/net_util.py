#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import requests
import json

"""
    本工具类封装了未归类的功能
"""

def http_get(url):
    response = urllib2.urlopen(url)
    return response.read()

def http_post(url, data):
    post_data = urllib.urlencode(data)
    response = urllib2.urlopen(url, post_data)
    return response.read()

def req_get(url):
    """存在乱码问题"""
    return requests.get(url).text

def req_post(url, data):
    return requests.post(url, data=data).text


if __name__ == '__main__':
    pass
