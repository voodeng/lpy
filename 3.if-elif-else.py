#!/bin/env python
# coding=utf8
# -*- coding: utf8 -*-

from __future__ import division
#### if-else ####
print '#### if-else ####'
a = input("a: ") # 12 or 10+2
b = input("b: ")
if(a>b):
    print "max: ", a
else:
    print "max: ", b
#### if-elif-else ####
print '#### if-elif-else ####'
score = raw_input("score: ") # string
score = int(score)
if(score>=90) and (score<=100):
    print "A"
elif(score>=80 and score<90):
    print "B"
elif(score>=60 and score<80):
    print "C"
else:
    print "D"
#### switch I ####
print '#### switch ####'
x = 1
y = 2
operator = "/"
result = {
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y
}
print result.get(operator)
#### switch II ####
print '#### switch II ####'
class switch(object):               
    def __init__(self, value):   # init value
        self.value = value
        self.fall = False        # no break, then fall=False    
    def __iter__(self):
        yield self.match         # match method to create 
        raise StopIteration      # exception to check loop
    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args: # successful
            self.fall = True
            return True
        else:                    # fail
            return False
operator = "+"
x = 1
y = 2
for case in switch(operator):
    if case('+'):
        print x+y
        break
    if case('-'):
        print x-y
        break
    if case('*'):
        print x*y
        break
    if case('/'):
        print x/y
        break
    if case():
        print 'NULL'
