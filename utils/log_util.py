#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os

"""
日志工具
"""

class logger:
    '''
        如果文件路径为空，则只输出到控制台
        不同的执行文件需要更改loggerName，不然会重复打印
    '''
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG, loggerName="wash logger"):
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        if path:
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
