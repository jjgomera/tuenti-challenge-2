#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 5:  Time is never time again
#Codigo para el cálculo de las pulsaciones de los relojes extraidos de las pruebas del año pasado

import datetime

#Reloj 1
cursor={0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

#Reloj 2
#En este caso la variable cursor representa los led que se iluminan al cambiar de número, así el elemento 0 son los led nuevos que se iluminan para que desaparezca el cero y se muestre el uno
cursor_decimal={0:1, 1:0, 2:4, 3:1, 4:1, 5:2, 6:1, 7:1, 8:4, 9:0}
cursor_hexadecimal={0:2, 1:0, 2:4, 3:1, 4:1, 5:2}
multiplicador=[36000, 3600, 600, 60, 10, 1]


while True:
    try:
        txt=raw_input().split()
    except EOFError:
        break

    fecha1=txt[0].split()[0].split("-")
    time1=txt[1].split()[0].split(":")
    fecha2=txt[3].split()[0].split("-")
    time2=txt[4].split()[0].split(":")

    year1=int(fecha1[0])
    month1=int(fecha1[1])
    day1=int(fecha1[2])
    hour1=int(time1[0])
    min1=int(time1[1])
    sec1=int(time1[2])

    year2=int(fecha2[0])
    month2=int(fecha2[1])
    day2=int(fecha2[2])
    hour2=int(time2[0])
    min2=int(time2[1])
    sec2=int(time2[2])

    start=datetime.datetime(year1, month1, day1, hour1, min1, sec1)
    end=datetime.datetime(year2, month2, day2, hour2, min2, sec2)

    diferencia=end-start
    dias=diferencia.days
    segundos=diferencia.seconds

    contador=36+2401920*dias+36*dias
    contador2=36+146469*dias+10*dias

    dec_hour, uni_hour, dec_min, uni_min, dec_sec, uni_sec=0, 0, 0, 0, 0, 0
    for segundo in range(1, segundos+1):
        dec_hour=segundo/36000
        uni_hour=(segundo-dec_hour*36000)/3600
        dec_min=(segundo-dec_hour*36000-uni_hour*3600)/600
        uni_min=(segundo-dec_hour*36000-uni_hour*3600-dec_min*600)/60
        dec_sec=(segundo-dec_hour*36000-uni_hour*3600-dec_min*600-uni_min*60)/10
        uni_sec=segundo-dec_hour*36000-uni_hour*3600-dec_min*600-uni_min*60-dec_sec*10
        contador+=cursor[dec_hour]+cursor[uni_hour]+cursor[dec_min]+cursor[uni_min]+cursor[dec_sec]+cursor[uni_sec]



    for segundo in range(1, segundos+1):
        digitos=[]
        digitos.append(segundo/36000)
        digitos.append((segundo-digitos[0]*36000)/3600)
        digitos.append((segundo-digitos[0]*36000-digitos[1]*3600)/600)
        digitos.append((segundo-digitos[0]*36000-digitos[1]*3600-digitos[2]*600)/60)
        digitos.append((segundo-digitos[0]*36000-digitos[1]*3600-digitos[2]*600-digitos[3]*60)/10)
        digitos.append(segundo-digitos[0]*36000-digitos[1]*3600-digitos[2]*600-digitos[3]*60-digitos[4]*10)

        for i, digito in enumerate(digitos):
            if segundo % multiplicador[i]==0:
                if i in [2, 4]:
                    contador2+=cursor_hexadecimal[digito]
                else:
                    contador2+=cursor_decimal[digito]
        
    print contador-contador2
