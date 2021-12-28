#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:17:57 2021

@author: mac
"""
print("========Tuples==========")
"""
Tuples can be used as immutable lists and as records with no field names.
when using a tuple as a collection of fields the number of items is often fixed
and their order is always vital.
"""

lax_coordinates = (33.9425, -118.408056)
#parallel assignment
latitude, longitude = lax_coordinates

#tuple unpacking or iterable unpacking
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
#record (city: tokyo,year:2003...)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print(year)

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country,_ in traveler_ids:
    print(country)

# swapping the values of variables without using a temporary variable:
longitude, latitude = latitude, longitude

#prefixing an argument with a star when calling a function
print(divmod(20, 8))
t = (20,8)

#print(divmod(*t))

quotient, remainder = divmod(*t)
#print(quotient)

#os.path.split() function builds a tuple (path, last_part) from a filesystem path.
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

#Using * to grab excess items
a, b, *rest = range(5)
a, *body, c, d = range(5)
#print(rest)

#Nested tuple unpacking
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]

for name, *e , (lat,lon) in metro_areas:
    print('{:15} | {:^9} | {:^9}'.format(name,lat,lon))
print("========Named tuples==========")
"""
Named tuples
tuples are very handy. But there is a missing feature when using them as records:
sometimes it is desirable to name the fields.
namedtuple take exactly the same amount of memory as tuples
because the field names are stor‐ ed in the class.
They use less memory than a regular object because they do store attributes
in a per-instance __dict__.
Two parameters are required to create a named tuple: a class name and
a list of field names, which can be given as an iterable of strings or
as a single spacedelimited string.
"""
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])
c = Card("1","A")
print(c)

City = namedtuple('City', 'name country population coordinates')
print(City._fields)

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
"""
_fields is a tuple with the field names of the class.
_make() lets you instantiate a named tuple from an iterable; City(*delhi_da
ta) would do the same.
_asdict() returns a collections.OrderedDict built from the named tuple
instance. That can be used to produce a nice display of city data.
"""
