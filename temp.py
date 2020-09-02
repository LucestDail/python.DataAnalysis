#!/usr/bin/env python3
from math import exp, log,sqrt
# pringing simple string
print("output #1: i'm excited to learn Python.")

# adding
x = 4
y = 5
z = x + y
print(f'output #2: result : {z}')

# list adding
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a+b
print(f'output #3: result -> {c}')

# type test
x = 2
y = 2.5*4.8
r = 8/float(3)
print(f'output #4: {x}, {y}, {z}')
# module import
print(f'output #4: {exp(x)}, {log(y)}, {sqrt(z)}')

# String testing
s1 = 'i\'m enjoying learning python.'
s2 = "this is a long string. without the backslash\
    it would run off of the page on the right\
        in the text editor and be very difficult to read"
s3 = '''you can use triplesingle quotes
for multi-line comment strings.'''
s4 = """you can also use triple double quotes
for multi-line comment strings."""
print(f'output #s1: {s1}')
print(f'output #s2: {s2}')
print(f'output #s3: {s3}')
print(f'output #s4: {s4}')

# another string test
s5 = "this is a "
s6 = "sample string"
s7 = s5 + s6
print(f'output #s5: {s7}')
lentesting = len(s7)
print(f'output #s6: {lentesting}')

# split test
s8 = "this, is, a, sample, string"
len_list = s8.split()
len_list1 = s8.split(" ", 2)
len_list2 = s8.split(",")
print(f'output #s4: {len_list}')
print(f'output #s4: {len_list1}')
print(f'output #s4: {len_list2}')