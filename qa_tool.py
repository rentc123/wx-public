#!/usr/bin/env python
# coding=utf-8
# ================================================================
#   Copyright (C) 2019 Tuya NLP. All rights reserved.
#   
#   FileName：qa_tool.py
#   Author  ：rentc(桑榆)
#   DateTime：2020/6/4
#   Desc    ：
#
# ================================================================

class QaTool:
    def __init__(self, path):
        self.id2content = {}
        self.init_qa(path)

    def init_qa(self, path):
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line != '' and not line.startswith("#"):
                    s = line.split("\t")
                    if len(s) == 4:
                        channel_id = s[1]
                        know_id = s[0]
                        ques = {"know_id": s[0], "channel_id": s[1], "title": s[2], "answer": s[3]}
                        if channel_id not in self.id2content:
                            self.id2content[channel_id] = {}
                            self.id2content[channel_id][know_id] = ques
                        else:
                            self.id2content[channel_id][know_id] = ques

    def get_answer(self, channel_id, know_id):
        cid2content = self.id2content.get(channel_id, {})
        content = cid2content.get(know_id, {})
        answer = content.get('answer', '...')
        return answer

    def get_title(self, channel_id, know_id):
        cid2content = self.id2content.get(channel_id, {})
        content = cid2content.get(know_id, {})
        title = content.get('title', '...')
        return title


if __name__ == '__main__':
    qa_tool = QaTool("data/qa_pair_data.txt")
    qid = "qa-pair-66"
    print(qa_tool.get_title("1000", qid))
    print(qa_tool.get_answer("1000", qid))
