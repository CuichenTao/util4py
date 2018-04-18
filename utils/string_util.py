#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import filter_util

def removeEndSymbol(content):
    """
        去除字符串中结尾句号
        例: u"你好啊。" <=> u"你好啊"
    """
    str_len = len(content)
    if str_len > 2 and content[str_len -1] == u"。" and content[str_len - 2] != u"。":
        return content[0:str_len - 1]
    return content

def removeStartAt(content):
    """
        去除字符串中@开头，并且紧跟 ':', '：', ' ' 三种情况
        例: u"@:你好啊" <=> u"你好啊"
    """
    if content.find(u'@') == 0:
        index1 = content.find(u'：')
        index2 = content.find(u':')
        index3 = content.find(u' ')
        if index1 < 0:
            index1 = len(content)
        if index2 < 0:
            index2 = len(content)
        if index3 < 0:
            index3 = len(content)
        index = min(index1, index2, index3)
        content = content[index + 1:]
        if content[0] == u'：' or content[0] == u':' or content[0] == u' ':
            content = content[1:]
        return content
    return content

def removeStartShape(content):
    """
        去除字符串#开始方括号对以及其中内容
        例: u"#你好啊#嘎嘎" <=> u"嘎嘎"
    """
    if content[0] == u'#':
        content = content[1:]
        if content.find(u'#') > 0:
            content = content[content.find(u'#') + 1:]
    return content


def removeEndShape(content):
    """
        去除字符串#结尾方括号对以及其中内容
        例: u"你好啊#嘎嘎#" <=> u"你好啊"
    """
    if content[len(content) -1] == u'#':
        content = content[0:len(content) - 1]
        if content.rfind(u'#') > 0:
            content = content[0: content.rfind(u'#')]
    return content


def removeEndEnglishBracket(content):
    """
        去除字符串结尾英文方括号对
        例: u"你好啊[嘎嘎]" <=> u"你好啊"
    """
    if content[len(content) -1] == u']' and content.rfind(u'[') > 0:
        return content[0: content.rfind(u'[')]
    return content

def removeStartEnglishBracket(content):
    """
        去除字符串结尾英文方括号对
        例: u"你好啊[嘎嘎]" <=> u"你好啊"
    """
    if content.startswith(u'[') and content.rfind(u']') > 0:
        return content[content.rfind(u']'):]
    return content


def removeStartChBracket(content):
    """
        去除字符串结尾英文方括号对
        例: u"你好啊[嘎嘎]" <=> u"你好啊"
    """
    if content.startswith(u'［') and content.rfind(u'］') > 0:
        return content[content.rfind(u'］')+1:]
    return content

def removeEndRoundBracket(content):
    """
        去除字符串结尾中文圆括号对
        例: u'你好啊（嘎嘎）' <=> u'你好啊'
    """
    if content[len(content) -1] == u'）' and content.rfind(u'（') > 0:
        return content[0: content.rfind(u'（')]
    return content

def removeEndEnRoundBracket(content):
    """
        去除字符串结尾中文圆括号对
        例: u'你好啊（嘎嘎）' <=> u'你好啊'
    """
    if content[len(content) -1] == u')' and content.rfind(u'(') > 0:
        return content[0: content.rfind(u'(')]
    return content

def removeStartRoundBracket(content):
    """
        去除字符串结尾中文圆括号对
        例: u'（嘎嘎）你好啊' <=> u'你好啊'
    """
    if content.startswith == u'（' and content.rfind(u'）') > 0:
        return content[content.find(u'）')+1:]
    return content


def removeStartBracket(content):
    """
        去除字符串开始中文方括号对
        例： u'【你好啊】嘎嘎' <=> u'嘎嘎'
    """
    if content[0] == u'【' and content.find(u'】') > 0:
        return content[content.find(u'】') + 1:]
    return content


def removeEndBracket(content):
    """
        去除字符串开始中文方括号对
        例： u'嘎嘎【你好啊】' <=> u'嘎嘎'
    """
    if content.endswith(u'】') and content.find(u'【') > 0:
        return content[:content.find(u'【')]
    return content

def removeInnerBracket(content):
    """
        去除字符串开始中文方括号对
        例： u'中文【你好啊】嘎嘎' <=> u'嘎嘎'
    """
    if content.find(u"【") > 0 and content.find(u"】") > content.find(u"【"):
        content_res = content[:content.find(u'【')] + content[content.find(u"】") + 1:]
        return content_res
    return content


def getContentInStartBracket(content):
    """
        获取字符串开始中文方括号对中的内容
        例： u'【你好啊】嘎嘎' <=> u'你好啊'
    """
    if content[0] == u'【' and content.find(u"】") > 0:
        return content[1: content.find(u'】')]
    return ""


def removeStartChineseBracket(content):
    """
        去除字符串『符号开始的内容
        例： u'『你好啊』嘎嘎' <=> u'嘎嘎'
    """
    if content[0] == u"『" and content.find(u"』") > 0:
        return content[content.find(u"』") + 1:]
    return content


def removeStartEnglishHalfBracket(content):
    """
        去除字符串『符号开始的内容
        例： u'『你好啊』嘎嘎' <=> u'嘎嘎'
    """
    if content[0] == u"「" and content.find(u"」") > 0:
        return content[content.find(u"」") + 1:]
    return content

def removeCnEndEnglishHalfBracket(content):
    """
        去除字符串『符号开始的内容
        例： u'『你好啊』嘎嘎' <=> u'嘎嘎'
    """
    if content.endswith(u"「") and content.find(u"」") > 0:
        return content[:content.find(u"「")]
    return content


def removeSubBetweenTwoWords(content, startWord, endWord):
    if content.find(startWord) >= 0 and content.find(endWord) > 0 and content.find(startWord) < content.find(endWord):
        return content[:content.find(startWord)] + content[content.find(endWord) + 1:]
    return content



# 过长句子切分

cut_words = [u'。', u'?', u'？', u'!', u'！', u'…', u'；', u';']

def find_first_symbol(content,start=0):
    min_pos = 1000000
    symbol = ""
    for item in cut_words:
        pos = content.find(item, start)
        if pos < min_pos and pos > -1:
            min_pos = pos
            symbol = item
    if min_pos != 1000000:
        return min_pos, symbol
    else:
        return -1, symbol

def cut_line(content, start=0):
    pos,symbol = find_first_symbol(content, start)
    while True:
        if len(content) -1 > pos:
            if content[pos+1] == symbol:
                pos+=1
            else:
                break
        else:
            break
    return pos

def get_cut_content(content):
    new_list = []
    cut_pos = cut_line(content)
    while True:
        pre_str = content[:cut_pos + 1]
        end_str = content[cut_pos+1:]
        if cut_pos != -1 :
            if filter_util.ch_num(pre_str) > 3:
                new_list.append(pre_str)
                content = end_str
                cut_pos = cut_line(content)
            else:
                content = pre_str + end_str
                cut_pos= cut_line(content, start=cut_pos+1)
        else:
            new_list.append(end_str)
            break
    while '' in new_list:
        new_list.remove('')
    arr_len = len(new_list)
    if arr_len > 1:
        if filter_util.ch_num(new_list[arr_len-1]) < 3:
            new_list[arr_len-2] = new_list[arr_len-2] + new_list[arr_len-1]
            new_list.pop()
    res_list = []
    for item in new_list:
        item = item.lstrip(u'）').lstrip(u')').strip()
        res_list.append(item)
    return res_list


def new_split_list(lst, num):
    new_list = []
    while '' in lst:
        lst.remove('')
    for item in [lst[i:i+num] for i in xrange(0,len(lst),num)]:
        new_list.append("".join(item))
    return new_list

in_num_word = [u'二',u'三',u'四',u'五',u'六',u'七',u'八',u'九',u'十',u'1', u'2', u'3', u'4',u'5',u'6',u'7', u'8', u'9',u'0']

def f_num_word(content):
    for item in in_num_word:
        if content.startswith(item+"."):
            return True
    return False


def cut_sentence(content):
    if f_num_word(content):
        return content
    else:
        lst = get_cut_content(content)
        new_list = []
        if len(lst) > 3:
            if len(lst) < 7:
                new_list = new_split_list(lst, 2)
            else:
                new_list = new_split_list(lst, 3)
        else:
            new_list = lst
        return "||".join(new_list).strip().lstrip(u'）').lstrip(u')').rstrip(u'(').rstrip(u'（')


if __name__ == '__main__':
    pass
