#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 10:  Coding m00re and m00re


function={"@": "__add__", 
                "$": "__sub__", 
                "&": "__div__", 
                "#": "__mul__",
                "conquer": "__mod__"}

while True:
    try:
        data=raw_input().split()
    except EOFError:
        break

    pila=[]
    while True:
        if not data:
            break
        txt=data.pop(0)
        try:
            pila.insert(0, int(txt))
        except ValueError: #operacion
                if txt in ["@", "#", "&", "$", "conquer"]:
                    pila[0]=pila[1].__getattribute__(function[txt])(pila[0])
                    del pila[1]
                elif txt=="dance":
                    pila[0:2]=pila[1::-1]
                elif txt=="fire":
                    del pila[0]
                elif txt=="mirror":
                    pila[0]=-pila[0]
                elif txt=="breadandfish":
                    pila.insert(0, pila[0])
                elif txt==".":
                    break
    print pila[0]
