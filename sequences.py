""" Code from Chapter 2 of Fluent Python
    Exploring Sequences
"""

# Use listcomps to build sequences, like so:
symbols = "(*&@(*#$^%ashd"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

# Cartesian Products
# Listcomps can generate lists from te Cartesian product
# of two or more iterables.
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]

# Generator Expressions
# Use these to build non-list sequences
# Can use a listcomp, but Genexps save memory because
# they yield items one by one using iterator protocol,
# instead of building a whole list just to feed another constructor
# Syntax: Same as listcomps, but use () instead of []
# init a tuple using genexp
tuple(ord(symbol) for symbol in symbols)
import array
array.array('I', (ord(symbol) for symbol in symbols)) # first arg for array is storage type

# cartesian product in a genexp, to save space
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
# yields 1 by 1. The full list is never generated


# Tuples as records
# tuples can be used as records, with no field names
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32456, 0.66, 8014)
traveler_ids = [('USA', '31195855')]
for passport in sorted(traveler_ids):
    print('%s/%s', passport)

for country, _ in traveler_ids:
    print(country)

# Tuple Unpacking
# Works with any iterable object
# swap w/o temp
a = 1
b = 2
b, a = a, b

# another example - prefixing an argument with a star,
# when calling a function
divmod(20, 8)
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)

# can use * to grab rest of items in a sequence
# py3:  a, b, *rest = range(5)
# and the * can appear in any position
# a, *body, c, d = range(5)

# can also unpack nested tuples
# python will do the right thing if expression matches the nesting structure

# Named Tuples
# collections.namedtuple
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', country='JP', population='36.933',
             coordinates=(35.689, 139.691))
# and we can access these fields by name OR position, delimited
# can also access some special methods in a namedtuple
#City._fields
#City._make(data)



# Memoization
# from: https://jeremykun.com/2012/01/12/a-spoonful-of-python/
def memoize(f):
   cache = {}

   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]

   memoizedFunction.cache = cache
   return memoizedFunction

@memoize
def fib(n):
   if n <= 2:
      return 1
   else:
      return fib(n-1) + fib(n-2)

# Managing Ordered Sequences with Bisect
# Two main fns from bisect module: bisect and insort
import bisect
import sys
HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,30,21]

ROW_FMT = '{0:2d} @ {1:2d}         {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

# bisect_left(haystack, needle) adds duplicates to the left of same item

# Interesting use case for bisect. Perform table lookups by numeric values
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i] # index into grades with resulting value...

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

# use bisect.insort() to inset while keep a sorted list always sorted

# When a list is NOT the answer --> ARRAYS!!
# use array.tofile() and array.fromfile() to load huge arrays and save them
