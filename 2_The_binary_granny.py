#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 2:  The binary granny    

def sumandos(num):
    sum=0
    resto=0
    numbin=bin(num)[-1:2:-1]
    for digit in numbin:
        if int(digit)-resto==1:
            sum+=1
        elif int(digit)-resto==0:
            sum+=2
            resto=1
        elif int(digit)-resto==-1:
            sum+=1
            resto=1
    sum+=int(bin(num)[2])-resto
    return sum
    
inputs=int(raw_input().split()[0])
for input in range(inputs):
    num=int(raw_input())
    max=sumandos(num)
    print "Case #%i: %i" %(input+1, max)
