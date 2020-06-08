#!/usr/bin/env python
# coding=utf-8
# ================================================================
#   Copyright (C) 2019 Tuya NLP. All rights reserved.
#   
#   FileName：test1.py
#   Author  ：rentc(桑榆)
#   DateTime：2020/6/5
#   Desc    ：
#
# ================================================================

import  ahocorasick     # 导入包
tree = ahocorasick.AhoCorasick("南京","南京市","长江大桥","市长", "江大桥") # 构建ac自动机
print(tree.search("南京市长江大桥")) # 检索

