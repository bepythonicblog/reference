#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:14:19 2021

@author: mac
"""

"""
Slicing
"""
s = slice(1,3,1) #(start , stop, step)
words = "lazy crazy complain show start"
print(words[s])
#%%
"""
Building lists of lists
"""
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
l=[1,2,3]
print(id(l))
l*= 2
print(id(l))
t=(1,2,3)
print(id(t))
t*=2
print(id(t))
"""
list.sort and the sorted built-in function
"""
#The list.sort method sorts a list in-place, that is, without making a copy
fruits = ['grape', 'raspberry', 'apple', 'banana']
print("lists: ",fruits)
fruits.sort()
print("sort by .sort() func/ replace the list",fruits) #compare items

#sorted creates a new list
fruits = ['grape', 'raspberry', 'apple', 'banana']
print("lists: ",fruits)
print("sort by sorted/create new list: ",sorted(fruits)) #compare items
print("Reverse : ",sorted(fruits,reverse=True)) #compare items
print("By len : ",sorted(fruits,key=len)) # compare items by len
fruits = ['grape', 'raspberry', 'banaNA', 'Apple']
print("By lowercase : ", sorted(fruits,key=str.lower)) # compare items by len


#%%
"""Searching

Managing ordered sequences with bisect and insort — that use the
binary search algorithm to quickly find and insert items in any sorted sequence.
"""
#Searching with bisect(haystack, needle)
#needle: (from(hay0), to(len(hay)))
#https://code.activestate.com/recipes/577197-sortedcollection/
import bisect as bis

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
index = bis.bisect(HAYSTACK,25,0,4)



def getGrade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    index = bis.bisect(breakpoints, score)
    return grades[index]

for c in [30,90,3]:
    print(getGrade(c))

g = ["grade of {} is {}".format(c,getGrade(c)) for c in [30,90,70]]
print(g)

#Inserting with bisect.insort
bis.insort(HAYSTACK,7)

import random

SIZE = 7
# get the same random value when call random -> randint or randrange
random.seed(1729)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bis.insort(my_list, new_item)
    print("{} -> {}".format(new_item,my_list))

#%%
"""
Array
If all you want to put in the list are numbers, an array.array is more efficient
than a list: it supports all mutable sequence operations (including .pop, .insert and .ex tend),
and additional methods for fast loading and saving such as .frombytes and .tofile.
"""
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
#array.tofile and array.fromfile
array_127 = array('b')
array_127.append(3)
print(array_127)
#array_127.append(128) => signed char is greater than maximum

a = array("b",(1,0,9,3,4))
a = array(a.typecode, sorted(a))
bis.insort(a,1)

#%%
"""Memory views"""
numbers = array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)
print(len(memv))
#change value of a(0) with memv
memv[0] = 5

print(memv.tolist())
#Create memv_oct by casting the elements of memv to typecode 'B' (unsigned char).
memv_oct = memv.cast('B')
print(memv_oct.tolist())
#Note change to numbers: a 4 in the most significant byte of a 2-byte unsigned integer is 1024.
#%%
"""
NumPy and SciPy
NumPy implements multi- dimensional, homogeneous arrays and matrix types
SciPy is a library, written on top of NumPy, offering many scientific computing algorithms
from linear algebra, numerical calculus and statistics.
"""

import numpy as np

a1 = np.arange(1,10,2)
a2 = np.arange(0,15)
a2.shape = [3,5]
print(a2[2])
print(a2.transpose())

"""
 Pandas and Blaze data analysis libraries provide efficient array types that can to hold non-numeric data
 as well as import/export functions compatible with many different formats like .csv, .xls, SQL dumps, HDF5
"""
#%%
"""
Deques and other queues

When use list :
inserting and removing from the left of a list (the 0-index end) is costly because the entire list must be shifted.
The class collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends

"""
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
dq.extend([11, 22, 33])
dq.extendleft([10, 20, 30, 40])
#the optional maxlen argument set the maximum number of items allowed in this instance of deque
#Fluent python page 55 deque method