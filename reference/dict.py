#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:20:03 2022

@author: mac
"""

"""
Dictionaries
"""

my_dict = {}
from collections import abc
import collections
r = isinstance(my_dict, abc.Mapping)
print(r)
"""

The built-in functions live in __builtins__.__dict__.


Using insinstace is better than checking whether a function argument is of dict type,
because then alternative mapping types can be used.


An object is hashable if it has a hash value which never changes during its lifetime
(it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method).
Hashable objects which compare equal must have the same hash value.

User-defined types are hashable by default because their hash value is their id()
and they all compare not equal. If an object implements a custom __eq__ that takes into account its internal state,
 it may be hashable only if all its attributes are immutable.

"""
#building a dict:
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a==b==c==d==e)
#%%
"""
dict comprehensions
"""

DIAL_CODES = [
    (81, 'Japan'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan')
]

d = { code:country for code ,country in DIAL_CODES}
print(d)
d = {country.upper():code for code ,country in DIAL_CODES}
print(d)
#%%
"""
Handling missing keys with setdefault
=> get is not the best way to handling a missing key.
index.get(word, [])
use setdefault instead my_dict.setdefault(key, [])
"""
import sys
import re
WORD_RE = re.compile('\w+')
index = {}

file = "pyzen.txt"

with open(file, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper): print(word, index[word])

index2 = {}
with open(file, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index2.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index2, key=str.upper): print(word, index2[word])
"""
my_dict.setdefault(key, []).append(new_value)
is the same as
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(new_value)
"""
#%%
#Mappings with flexible key lookup

#Create a defaultdict with the list constructor as default_factory.
index = collections.defaultdict(list)
with open(file, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper): print(word, index[word])
"""
If word is not initially in the index, the default_factory is called to produce the missing value,
which in this case is an empty list that is then assigned to index[word] and returned,
so the .append(location) operation always succeeds.

If no default_factory is provided, the usual KeyError is raised for missing keys.

The mechanism that makes defaultdict work by calling default_factory is actually the __missing__ special method
"""

a = collections.defaultdict(list,[("k",3),("A",4)])
a["RR"].append(2)