#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: stanford_parser_2.py
# Time: 16-12-7 下午2:25
# -------------------------------------------
import sys
from nltk.tree import Tree

reload(sys)
sys.setdefaultencoding("utf-8")

import nltk
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser


# 句法分析
def parser(sentence):
    chi_parser = StanfordParser(path_to_jar=u"/home/zhangxin/work/stanford/jars/stanford-parser.jar",
                                path_to_models_jar=u"/home/zhangxin/work/stanford/jars/stanford-parser-3.6.0-models.jar",
                                # model_path=u"/home/zhangxin/work/stanford/jars/edu/chineseFactored.ser.gz")
                                model_path=u"/home/zhangxin/work/stanford/jars/edu/chinesePCFG.ser.gz")
    re = chi_parser.parse(sentence.split())

    return re


# 依存句法分析
def parser_dependency(sentence):
    eng_parser = StanfordDependencyParser(path_to_jar=u"/home/zhangxin/work/stanford/jars/stanford-parser.jar",
                                          path_to_models_jar=u"/home/zhangxin/work/stanford/jars/stanford-parser-3.6.0-models.jar",
                                          model_path=u"/home/zhangxin/work/stanford/jars/edu/chinesePCFG.ser.gz")
    res = list(eng_parser.parse(sentence.split()))
    print type(res)
    for row in res[0].triples():
        # print row[1]
        print row[0][0], row[1], row[2][0]

    return res