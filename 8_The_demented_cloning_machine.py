#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 8:  The demented cloning machine


#Sample output


from hashlib import md5
from os import popen

queue=raw_input()
#with open("/media/datos/archivo_0.dat", "w") as file:
#    for i in range(len(queue)/100):
#        file.write(queue[i*100:(i+1)*100]+"\n")
#    if len(queue)%100:
#        file.write(queue[(i+1)*100:]+"\n")
        
#queue="abadrec"

    
mutation=[]
while True:
    try:
        mutation.append(raw_input())
    except EOFError:
        break
        
#mutation=["a=>ca,d=>pip,u=>as", "p=>vt,e=>yt"]

ciclos=len(mutation)
diccionario=[]
for k, serie in enumerate(mutation):
    mutaciones=serie.split(",")
    diccionario.append({})
    for i, cambio in enumerate(mutaciones):
        old, new=cambio.split("=>")
        diccionario[k][old]=new
        
#    with open("/media/datos/archivo_%i.dat" %k, "r") as file:
#        while True:
#            try:
#                queue=file.readline()[:-1]

file=open("/media/datos/archivo.dat", "w")
for char in queue:
    cola=[char]
    for k, mutacion in enumerate(diccionario):
        cola_new=[]
        for elemento in cola:
            cola_new+=list(diccionario[k].get(elemento, elemento))
        cola=cola_new[:]
    txt="".join(cola)
    file.write(char)
            
            
#with open("/media/datos/archivo.dat", "r") as file:
#    buf=buffer(file)
#    txt=file.readline()
##    txt="".join(txt)
##    txt.replace("\n", "")
#print txt
#    print md5(file).hexdigest()
#system("md5sum /media/datos/archivo.dat")

sum = popen('md5sum /media/datos/archivo.dat').read()
