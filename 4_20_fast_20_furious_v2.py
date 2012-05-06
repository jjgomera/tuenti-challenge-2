#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 4:  20 fast 20 furious


#how much gasoline we must buy each day.
#1 liter of gasoline per kart used per race.

#    Before a race starts, groups are being seated one at a time until there are no more groups waiting or there are not enough karts for the next group.
#    Then the race starts, whether all the karts are being used or not.
#    When the race finishes they wait again in the same order until the day is over.

#Every day we have exactly R races.


#N: Test cases
#r_max: carreras diarias
#k_max: número de coches
#g_max: número de grupos



N=int(raw_input())

for input in range(N):
    txt=raw_input().split()
    r_max=int(txt[0])
    k_max=int(txt[1])
    g_max=int(txt[2])
    txt=raw_input().split()
    group=[int(i) for i in txt]
    
    with open("archivo_%i.dat" %input, "w") as file:
        file.write(str(r_max)+"\n")
        file.write(str(k_max)+"\n")
        file.write(str(g_max)+"\n")
        file.write(str(group)+"\n")

    gente=sum(group)
    if gente<=k_max:
        gasolina_total=r_max * gente
        
    else:
        indice_max=g_max-1
        gasolina_total=0
        indice=0
        r=1
        while r<=r_max:
            k=0
            while k+group[indice]<=k_max:
                k+=group[indice]
                if indice==indice_max:
                    indice=0
                else:
                    indice+=1
                    
            if indice==0:
                gasolina_total=r_max/r*(gasolina_total+k)
                r=r_max/r*r+1
            else:
                r+=1
                gasolina_total+=k

    print gasolina_total
    
