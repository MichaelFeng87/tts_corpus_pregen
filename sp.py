#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
切割文件
'''

import sys,re

reload(sys)
sys.setdefaultencoding("utf-8")


def sp(fn, prefix, bsize):
	with open(fn, 'r') as fp:
		ll = fp.readlines()
		nn = len(ll)/bsize
		for x in xrange(nn):
			with open(prefix+ ('%02d'%x) +'.txt', 'w') as fpo:
				for li in xrange(bsize*x, min(len(ll), bsize*(x+1))):
					fpo.write(ll[li])
        
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "usage: sp.py fn foprefix  batchsize"
        sys.exit()
        
    print sys.argv[1], sys.argv[2], sys.argv[3]
    
    sp(sys.argv[1], sys.argv[2], int(sys.argv[3]))
