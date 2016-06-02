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

import sys,re


reload(sys)
sys.setdefaultencoding("utf-8")


def remove_short(ucc):
    rr = []
    for l in ucc:
        if len(l.strip()) > 15 :
            rr.append(l.strip())
    return rr

def remove_white(ucc):
    '''去掉有空格的行'''
    rr = []
    for l in ucc:
        flag = True
        for w in l:
            if w == u' ':
                flag = False
                break
        if flag:
            rr.append(l)
    return rr
    
def split_with_juhao(ucc):
    '''句号换行'''
    rr = []
    for l in ucc:
        ll = l.split(u'。')
        for nl in ll:
            rr.append(nl+u'。')
    
    return rr

def replace_things(ucc):
    '''分号改成逗号'''
    rr = []
    for l in ucc:
        t = l.replace(u'；', u'，')
        t = t.replace(u'：', u'，')
        rr.append(t)
    return rr
    
def remove_kuahao(ucc):
    '''括号内的删除'''
    rr = []
    for l in ucc:
        rr.append(re.sub(u'\uff08.*\uff09', u'', l))
    
    return rr   

def split_long(ucc):
    '''太长的分'''
    rr = []
    for l in ucc:
        if len(l) > 40:
            ll = l.split(u'，')
            if len(ll) >=2:
                idx = len(ll)/2
                nl = ll[0]
                for i in xrange(1,idx):
                    nl = nl + u'，' + ll[i]
                rr.append(nl+u'。')
                nl = ll[idx]
                for i in xrange(idx+1, len(ll)):
                    nl = nl + u'，' + ll[i]
                rr.append(nl)
        else:
            rr.append(l)
    return rr

'''
关于编码
utf-8(类型 str)  ---decode(utf-8)----> 类型unicode  -----encode(utf-8)---->  utf-8(类型 str) 
空格的删除，字数的计算，都必须在 unicode 层面。
'''

def gen(fn, fno):
    with open(fn, 'r') as fp:
        cc = fp.readlines()
        
        ucc = [c.decode("utf-8") for c in cc]
        
        #unicode start
        ucc = remove_short(ucc)
        ucc = remove_white(ucc)
        
        ucc = remove_kuahao(ucc)
        
        ucc = split_with_juhao(ucc)
        ucc = remove_short(ucc)
        
        ucc = replace_things(ucc)
        
        
        ucc = split_long(ucc)
        ucc = remove_short(ucc)
        ucc = split_long(ucc)
        ucc = remove_short(ucc)
        ucc = split_long(ucc)

        
        
        
        #unicode end
        cc = [c.encode("utf-8") for c in ucc]
        
        
        for l in cc:
            print l
        
        print 'Total=%d'%len(cc)
        
        with open(fno, 'w') as fpo:
            for l in cc:
                fpo.write(l+'\n')
            
        
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: tr.sh fn fno"
        sys.exit()
        
    print sys.argv[1], sys.argv[2]
        
    gen(sys.argv[1], sys.argv[2])
