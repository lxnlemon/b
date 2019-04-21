# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/4/20 23:42
# @Author  : lxn


for i in range(1,10):
    for j in range(1,i+1):
        print(' {}*{} = {}'.format(j,i,i*j),end='')
    print()
