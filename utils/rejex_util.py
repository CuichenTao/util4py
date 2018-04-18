#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def has_time(content):
    '''
        检测是否包含时间格式数据
    :param content:
    '''
    content = content.encode("utf8")
    for case in [r'((.*?)年(.*?)月)', r'((.*?)月(.*?)日)', r'((.*?)月(.*?)号)', r'((.*?)时(.*?)分)', r'((.*?)点(.*?)分)', r'(\d+\.\d+\.\d+)', r'(\d+-\d+-\d+)', r'(\d+_\d+_\d+)', r'(\d+/\d+/\d+)', r'(\d+:\d+)', r'(\d+月\d+)']:
        res = re.findall(case, content)
        if res:
            return True
    return False

if __name__ == '__main__':
    pass
