#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:51:42 2021

@author: mac
"""
# list comp []

symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

# A listcomp is meant to do one thing only: to build a new list.
# Please don’t use that syntax if you are not doing something with the produced list.
codes2 = [ord(symbol) for symbol in symbols]

def fil(x):
    if x > 127:
        return True
    else:
        return False

f = filter(fil, map(ord,symbols))
print(list(f))
# f return <filter object at 0x7fe70e305790>
# to get resutl use list function
f1 = filter(lambda c : c > 127, map(ord,symbols))
print(list(f1))