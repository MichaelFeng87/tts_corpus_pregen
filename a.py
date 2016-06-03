#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
语音识别中，我们没有足够多的真人录音语料库，因而，我尝试使用在线语音合成（有12个发音人，随机分布），来制造 corpus。
从网上找来的文章，因为有长短不一的句子，各种混乱的符号，无法直接使用。我们需要每行30个字左右的一系列句子。
本脚本就是用来处理text 到 list of sentence的。

chenbingfeng 2016年06月02日


	1）空行删除，长度少于10个字的行删除。
	2）段内有空格的，删除。
	3）句号分行。
	4）分号分行。
    5）超过30字的长句，逗号分行。
'''

import sys
import re
import jieba


reload(sys)
sys.setdefaultencoding("utf-8")

def replace_fuhao(l):
    '''所有符号转换成空格'''
    a= re.findall(u"([\u4e00-\u9fff]+)", l)
    return " ".join(a)

dict = {}


def load_lexicon_dict():
	with open('lexicon.txt', 'r') as fp:
		cc = fp.readlines()
		cc = [c.decode('utf-8') for c in cc]
		for c in cc :
			k = c.find(' ')
			k, v= c[0:k], c[k+1:-1] #-1去掉换行
			dict[k] = v
	
def phoneme(w):
	'''给一个词寻找 phoneme'''
	if dict.has_key(w):
		return dict[w].strip()
	r = u''
	for c in w:
		r = r + dict[c] + ' '
	
	return r.strip()

if __name__ == "__main__":
	load_lexicon_dict()
	print phoneme(u'宇宙')
	print phoneme(u'少年绿茶表')


