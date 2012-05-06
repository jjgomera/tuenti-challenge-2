#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 13:  The crazy croupier

#Please implement the most efficient algorithm (in terms of execution time) you can think of. Brute-force based solutions will have a poor evaluation.
#Se usa minimo comun múltiplo de los ciclos que necesita cada carta para volver a la posición inicial
#Al ser L constante, la rotación siempre será la misma, la carta que empiece encima del taco acabará siempre en la misma posición, así que solo será necesario calcular un ciclo, y luego iterar

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm2(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcm(args):
    """Return lcm of args."""   
    return reduce(lcm2, tuple(args))


inputs=int(raw_input())
for input in range(inputs):
    data=raw_input().split()
    N=int(data[0])
    L=int(data[1])

    inicial=[i for i in range(N)]
    pila1=inicial[:L]
    pila2=inicial[L:]
    mezclado=[]
    while len(pila1) and len(pila2):
        mezclado.append(pila1.pop())
        mezclado.append(pila2.pop())
    mezclado.extend(pila1[::-1])
    mezclado.extend(pila2[::-1])

    rotacion={}
    for inicio, fin in zip(inicial, mezclado):
        rotacion[fin]=inicio
    ciclo=[]
    for carta in range(N):
        if carta==rotacion[carta]:
            tandas=0
        else:
            tandas=1
            pos=rotacion[carta]
            while carta!=pos:
                pos=rotacion[pos]
                tandas+=1
        ciclo.append(tandas)

    for i in range(ciclo.count(0)):
        del ciclo[ciclo.index(0)]
    mcm=lcm(ciclo)
    print "Case #%i: %i" %(input+1, mcm)
