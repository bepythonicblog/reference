#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:14:19 2021

@author: mac
"""

"""Slicing"""
s = slice(1,3,1) #(start , stop, step)
words = "lazy crazy complain show start"
print(words[s])

#Building lists of lists
l = [[1,2] * i for i in range(1,4) ]
print(l)

# with list comprh the list built has element with diff reference: it's like
board_d = []
for i in range(3):
    row = ["_"] * 3
    board_d.append(row)

#same reference
weird_board = [['_'] * 3] * 3
#it's like:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
# always the same row is appended