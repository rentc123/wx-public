#!/usr/bin/env python
# coding=utf-8
# ================================================================
#   Copyright (C) 2019 Tuya NLP. All rights reserved.
#   
#   FileName：test.py
#   Author  ：rentc(桑榆)
#   DateTime：2020/6/4
#   Desc    ：
#
# ================================================================

r={
"responseText": [
        {
            "type:": "Text",
            "content": "端午节快要到了！我们店很多商品都在打折促销哦，来看看吧！"
        }
    ]
}
response_texts=[]
if 'responseText' in r:
    for cont in r['responseText']:
        rtype = cont.get('type')
        print(rtype)
        content = cont.get('content')
        if rtype == 'Text':
            response_texts.append(content)

response_text = "\n".join(response_texts)
print(response_text)