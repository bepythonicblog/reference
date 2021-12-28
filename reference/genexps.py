#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:58:14 2021

@author: mac
"""

# Generator expressions ()

symbols = '$¢£¥€¤'
#f = tuple(ord(symbol) for symbol in symbols) f is a tuple

#f is now a generator
f = (ord(symbol) for symbol in symbols)
print(type(f),"\n",list(f))

import array
I = array.array("I",(ord(symbol) for symbol in symbols))

def gen1():
    for symbol in symbols:
        yield ord(symbol)
"""
Yield is a keyword in Python that is used to return from a function
without destroying the states of its local variable and when the function is called,
the execution starts from the last yield statement.
Any function that contains a yield keyword is termed a generator
"""

#for s in gen1():
    #print(s)
#If the generator expression is the single argument in a function call,
#there is no need to duplicate the enclosing parenthesis.


# infinite generator

def integerGen():
    print("one time init")
    i = 1
    while True:
        print("in while")
        yield i
        i=i+1
        print('loop')

colors = ['black', 'white']
sizes = ['S','M','L']
cont = [1,2,9]

for tsh in ( "{}-{}".format(c,s) for c in colors for s in sizes):
    print(tsh)

for tsh in ( "%s %s %d" % (c,s,n) for c in colors for s in sizes for n in cont):
    print(tsh)