#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 9:  Il nomme della magnolia


N=int(raw_input())
for n in range(N):
    data=raw_input().split()
    world=data[0].upper()
    ocurrencia=int(data[1])
    
    archivo=1
    while ocurrencia>0 and archivo<=800:
        with open("/media/datos/documents/%s" % str(archivo).zfill(4), "r") as file:
            lineas=file.readlines()
            palabras=[linea.upper().split() for linea in lineas]
                        
        for linea, palabra in enumerate(palabras):
            find_archivo=palabra.count(world)
            if find_archivo:
                if find_archivo<ocurrencia:
                    ocurrencia-=find_archivo
                else:
                    index=palabra.index(world)
                    for i in range(ocurrencia-1):
                        index=palabra.index(world, index+2)
                    ocurrencia=0
                    print "%i-%i-%i" %(archivo, linea+1, index+1)
                    break
                
        archivo+=1
