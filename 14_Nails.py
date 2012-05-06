#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 14:  Nails

import numpy

#If all you have is a hamming, everything looks like a nail.
#If all you have is a hammer, everything looks like a nail --> Dont use the normal binary tools, binary to ascii
#Ummm maybe morse, or other code, no exit.

#Hamming, not hammer
#Maybe http://en.wikipedia.org/wiki/Hamming_code

#From image
txt="00001010001101100011011001011101110011100011011101111100010001000100001000110100010001001101110111110011100100101100010010011101010001101000"
#print len(txt)%8, len(txt)%7
#Module 7 = 0, so try with Hamming (7,4) without an additional parity bit
bits=7

G=numpy.matrix( [[1,1,0,1], 
                            [1,0,1,1], 
                            [1,0,0,0], 
                            [0,1,1,1], 
                            [0,1,0,0], 
                            [0,0,1,0], 
                            [0,0,0,1]])

H=numpy.matrix( [[1,0,1,0,1,0,1], 
                            [0,1,1,0,0,1,1], 
                            [0,0,0,1,1,1,1]])

def bin2Str(codigo):
    characters = []
    for i in range(0, len(codigo), 8):
        num = int(codigo[i:i+8],2)
        characters.append(chr(num))
        if num<32 or num>165:
            return "Error!"
    return "".join(characters)

while True:
    try:
        txt=raw_input()
    except EOFError:
        break
    
    if len(txt)%7!=0:
        print "Error!"
    else:
        mensaje=""
        for i in range(0, len(txt), bits):
            data=numpy.matrix([int(char) for char in txt[i:i+bits]]).transpose()
            error=(H*data)%2
            indice=-1
            while error.any()!=0:
                indice+=1
                new_data=data.copy()
                new_data[indice, 0]=not data[indice, 0]
                error=(H*new_data)%2
                
            if indice!=-1:
                data=new_data.copy()
            byte=str(data[2, 0])+str(data[4, 0])+str(data[5, 0])+str(data[6, 0])
            mensaje+=byte
            
        print bin2Str(mensaje)

