#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:26:17 2021

@author: mac
"""
from math import hypot

class Vector:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    # important than __str__
    def __repr__(self):
        return "Vector(%r,%r)" % (self.x, self.y)

    # if not implemented python will use __repr__
    def __str__(self):
        return "V({},{})".format(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)