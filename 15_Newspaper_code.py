#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 15:  Newspaper code

from PIL import Image
import math

#Look up something in the image, maybe the point the text is talking about, so doing zoom it can be see several points, without color in the image
#We can extract the points to avoid some error in transcription

#archivo = Image.open("newspaper.png")
#altura, anchura=archivo.size
#
#puntos=[]
#for i in xrange(anchura):
#    for j in xrange(altura):
#        r, g, b, a=archivo.getpixel((j, i))
#        if a!=255:
#            puntos.append("%i-%i" %(j, i))
#    
#with open("matriz_puntos.dat", "w") as file:
#        file.write("\n".join(puntos))

#print "thesecrethasbeenrevealedtosolvethechallengewhichisthetwentiethemirp"
#print "the secret has been revealed to solve the challenge which is the twentieth emirp"

#or reeally you want the 20th emirp
# so using my solution of last year:

def isPrime(n):
    """Given integer n, check if its prime"""
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for k in xrange(3, 1 + int(math.sqrt(n)), 2):
            if n % k == 0:
                return False
        return True


emirp=[]
x=2
while len(emirp)<20:
    r = int(x.__repr__()[::-1])
    if (isPrime(x)) and (r != x) and (isPrime(r)):
        emirp.append(x)
    x+=1

print emirp[-1]
