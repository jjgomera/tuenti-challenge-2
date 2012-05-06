#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 7:  The "secure" password


#2Ad
#12c
#2Ac
#2Bc
#1cd
#1xZ
#1dx
#BdZ

#12ABcdxZ
#12BAcdxZ


order=[]
unknown={}
while True:
    try:
        txt=raw_input()
    except EOFError:
        break
    
    if not order:
        order=[char for char in txt]
    else:
        index=[None]*len(txt)
        for i, letra in enumerate(txt):
            if order.count(letra):
                index[i]=order.index(letra)
            
        start=0
        end=len(txt)
        if 0 in index: #hay elementos nuevos al principio
            start=index.index(0)
            order=[char for char in txt[:start]]+order
            for char in txt[:start]:
                if unknown.has_key(char):
                    del unknown[char]
                    
        if len(order)-1 in index: #hay elementos nuevos al final
            end=index.index(len(order)-1)+1
            order=order+[char for char in txt[end:]]
            for char in txt[end:]:
                if unknown.has_key(char):
                    del unknown[char]
                    
        #manipular el resto de elementos
        for indice in range(start, end):
            elemento=txt[indice]
            if elemento not in order:
                if unknown.has_key(elemento):
                    anterior, posterior=unknown[elemento]
                else:
                    anterior, posterior=None, None
                if indice>0:
                    nuevo_anterior=txt[indice-1]
                    if not anterior:
                        anterior=nuevo_anterior
                    if anterior in order and order.count(nuevo_anterior):
                        anterior=order[max(order.index(nuevo_anterior), order.index(anterior))]
                if indice<len(txt)-1:
                    nuevo_posterior=txt[indice+1]
                    if not posterior:
                        posterior=nuevo_posterior
                    if posterior in order and order.count(nuevo_posterior):
                        posterior=order[min(order.index(nuevo_posterior), order.index(posterior))]
                unknown[elemento]=anterior, posterior
                
        #clean unknown
        for key in unknown.keys():
            ant, pos=unknown[key]
            if ant in order and pos in order and order.index(ant)+1==order.index(pos):
                order.insert(order.index(pos), key)
                del unknown[key]
            if ant in order and order.index(ant)+1==len(order) and pos==None:
                order.append(key)
                del unknown[key]
            if pos in order and order.index(pos)==0 and ant==None:
                order.insert(0, key)
                del unknown[key]
                
txt="".join(order)
password=[]
for key in unknown.keys():
    ant, pos=unknown[key]
    start=order.index(ant)
    end=order.index(pos)
    for indice in range(start, end):
        password.append(txt[:indice+1] + key + txt[indice+1:])
    del unknown[key]

for pwd in sorted(password):
    print pwd
    
