#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 3:  The Evil Trader

data=[]
while True:
    try:
        txt=raw_input()
    except EOFError:
        break
    data.append(int(txt))
    
start=0
end=1
profit=data[end]-data[start]
i=0
j=1

while i<len(data)-2 and j<len(data)-1:
    j+=1
    newprofit=data[j]-data[start]
    if newprofit>profit:
        end=j
        profit=newprofit
    
    i+=1
    newprofit=data[j]-data[i]
    if newprofit>profit and j>i:
        start=i
        profit=newprofit
        
print start*100, end*100, profit
