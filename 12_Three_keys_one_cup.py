#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 12:  Three keys one cup

from PIL import Image

#Entrada datos
input=raw_input()

#From file comment
key1="a541714a17804ac281e6ddda5b707952"

#From qrcode
key2="ed8ce15da9b7b5e2ee70634cc235e363"


#Easy, but  the third key i didn't know how extract, maybe steganography like 17, my finish challenge last year.

#The clue for me dont work:
#Break the hash and you have 3 hint:  a90365a5c53eb8a9d03b6a248d894c5a
#   MD5: lsbqrmd
#   CISCO: "/K̼[�ۻWn��", "e��>���;j$��LZ", "g��Z�ʹ_@��(>"
# I loose the time try to decodified thats three codes

#Finally i go back to steganography

archivo = Image.open("CANTTF.png")
altura, anchura=archivo.size

rojo=[]
verde=[]
azul=[]
for i in xrange(altura):
    rojo_fila=[]
    verde_fila=[]
    azul_fila=[]
    for j in xrange(anchura):
        r, g, b=archivo.getpixel((j, i))
        rojo_fila.append(str(r)[-1])
        verde_fila.append(str(g)[-1])
        azul_fila.append(str(b)[-1])
    rojo.append(rojo_fila)
    verde.append(verde_fila)
    azul.append(azul_fila)
    
with open("matriz_rojo.dat", "w") as file:
    for sospechoso in rojo:
        file.write("".join(sospechoso)+"\n")
with open("matriz_verde.dat", "w") as file:
    for sospechoso in verde:
        file.write("".join(sospechoso)+"\n")
with open("matriz_azul.dat", "w") as file:
    for sospechoso in azul:
        file.write("".join(sospechoso)+"\n")

#Look the files in a text editor with zoom, it can see a anomaly in the first line, 97 pixel in the three color channel

codigo = ""
for x in range(100):
    r,g,b= archivo.getpixel((x,0))
    codigo+=str(r & 1)
    codigo+=str(g & 1)
    codigo+=str(b & 1)
#print codigo

characters = []
bits = 8
for i in range(0, len(codigo), bits):
    num = int(codigo[i:i+bits],2)
    characters.append(chr(num))

decodifiedMessage="".join(characters)
key3=decodifiedMessage

suma=""
for i in range(len(input)):
    char=hex(int(key1[i], 16)+int(key2[i], 16)+int(key3[i], 16)+int(input[i], 16))[-1]
    suma+=char
print suma

