#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 11:  Descrambler

#The score of a word is the sum of all its letters (including the letters of the horizontal word) using the following table:
#1 point: A E I L N O R S T U
#2 points: D G
#3 points: B C M P
#4 points: F H V W Y
#5 points: K
#8 points: J X
#10 points: Q Z


puntos={ "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1, 
                "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, 
                "K": 5, 
                "X": 8, "J": 8, 
                "Q": 10, "Z": 10}


def puntuacion(palabra):
    value=0
    for char in palabra:
        value+=puntos[char]
    return value


def isColocable(tablero, palabra):
    """Calcula si la palabra comparte alguna letra con la palabra del tablero"""
    colocable=False
    letras_compartidas=[]
    for letra in tablero:
        if letra in palabra:
            colocable=True
            letras_compartidas.append(letra)
    return colocable, letras_compartidas


def isDisponible(rack, palabra, enganche):
    """Calcula si tenemos disponibles las letras para añadir la palabra al tablero"""
    enganchada=False
    disponible=True
    rack=list(rack)
    for char in palabra:
        if char not in rack:
            if char in enganche and not enganchada:
                enganchada=True
            else:
                disponible=False
        else:
            del rack[rack.index(char)]
    return disponible


with open("descrambler_wordlist.txt", "r") as file:
    lineas=file.readlines()

N=int(raw_input())
for n in range(N):
    rack, tablero=raw_input().split()
    
    value=0
#    indice=[]
    for i, palabra in enumerate(lineas):
        palabra=palabra[:-1]
        colocable, letras_compartidas=isColocable(tablero, palabra)
        disponible=isDisponible(rack, palabra, letras_compartidas)
        if colocable and disponible:
            valor=puntuacion(palabra)
            if valor>value:
                value=valor
                indice=palabra
                
# if its necessary save all best word, and not only the first in dictionary
#                indice=[palabra]
#            elif valor==value:
#                indice.append(palabra)
#    print indice, value
                
    print indice, value
    
