#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 6:  Cross-stitched fonts

#Materials for cross-stitching are quite simple: cloth, a needle and thread. There are many kinds of fabrics for cross-stitching, all of them available in different resolutions or counts. The count (ct) is the number of pixels (or stitches) per inch of cloth, for example, 14ct indicates 14 pixels per inch.
#
#We have some rectangular fabric pieces and messages to stitch, and we want to use all possible space with maximum font size (measured in pixels or stitches) without splitting words across lines. As good geeks, we will use a monospace font for the message, therefore all characters, including whitespaces, take up the same space (both in vertical and horizontal). We must leave a whitespace between words, but we will not leave any between different lines.
#In order to buy enough thread, we have estimated that each stitch uses 1/(fabric ct) inches of thread, and that the average number of stitches per character (except the whitespace!) is (font size)2/2. For example, if we use a 14ct fabric with a font size of 14, then each character will use an average of 7’’ of thread.
#Your task is to compute the minimum amount of thread we need to order. We cannot order fractions of an inch, that is, if we need 16.6'' of thread, we will order 17''.


from math import ceil

N=int(raw_input())
for input in range(N):
    data=raw_input().split()
    w=int(data[0])
    h=int(data[1])
    ct=int(data[2])
    txt=raw_input()
    
    letras=len(txt)
    caracteres=letras-txt.count(" ")

    size=0
    cabe=True
    while cabe and size<20:
        size+=1
        length=w*ct
        filas=h*ct-size
        for palabra in txt.split(" "):
            if len(palabra)*size<length:
                length-=(len(palabra)+1)*size
            elif filas>=size and len(palabra)*size<w*ct:
                length=w*ct-(len(palabra)+1)*size
                filas-=size
            else:
                cabe=False
                size-=1
                
    if not cabe and size==1:
        hilo=0
    else:
        hilo=size**2*caracteres/2./ct

    print "Case #%i: %i" %(input+1, ceil(hilo))
