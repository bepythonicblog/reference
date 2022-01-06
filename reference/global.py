#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:58:51 2021

@author: mac
"""


"""
@Fluent python page 39
-> The special method that makes += work is __iadd__
if __iadd__ is not implemented, Python falls back to calling __add__.

-> Repeated concatenation of immutable sequences is inefficient

• Putting mutable items in tuples is not a good idea.
• Augmented assignment is not an atomic operation — we just saw it throwing an exception after doing part of its job.
• Inspecting Python bytecode is not too difficult, and is often helpful to see what is going on under the hood.
    exp : >>> dis.dis('a + b')
    1           0 LOAD_NAME                0 (a)
                2 LOAD_NAME                1 (b)
                4 BINARY_ADD
                6 RETURN_VALUE


if you need to store 10 million of floating point values an array is much more efficient
, because an array does not actually hold full-fledged float objects,
but only the packed bytes representing their machine values — just like an array in the C language.
On the other hand, if you are constantly adding and removing items from the ends of a list as a FIFO or LIFO
 data structure, a deque (double-ended queue) works faster.

Sets are optimized for fast membership checking.
"""



"""
Book refence:
    @Fluent python book
"""