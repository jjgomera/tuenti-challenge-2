#!/usr/bin/python
# -*- coding: utf-8 -*-

#Challenge 17:  The Solomonic pizza cut


#it is not always possible to make a straight-line cut into the pizza in such a way that the two slices have the same area and the same number of ingredients of each type.

#Straight-line cut and two slices, so we need split with a line pass for center


from math import cos, sin, atan, pi

class Pizza(object):
    """Clase que define una pizza como una circunferencia"""
    def __init__(self, centerx, centery, radius):
        self.Cx=centerx
        self.Cy=centery
        self.R=radius
        self.value=[True]
        self.circle=[0, pi]
        self.ingredientes={}
        
    def addPieze(self, id, center, vertices):
        if True in self.value:
            if self.center_in_polygon(center, vertices[0:2]):
                self.value=[False]
                self.circle=[0, pi]
            else:
                if not self.ingredientes.has_key(id):
                    self.ingredientes[id]=[]
                angulos=self.angle_Tangent(vertices)
                low=min(angulos)
                high=max(angulos)
                
                if high>3*pi/2 and low<pi/2: #la pieza cubre el angulo 0
                    low=0
                    high=min(angulos)
                    self.addBadZone(low, high)
                    
                    low=max(angulos)-pi
                    high=pi
                    self.addBadZone(low, high)
                    pieza={"center": center, 
                                "ang_low": max(angulos), 
                                "ang_high": min(angulos)+2*pi}
                    self.ingredientes[id].append(pieza)
                elif 3*pi/2>high>pi and pi/2<low<pi:    #la pieza cubre el angulo 180
                    low=0
                    high=max(angulos)-pi
                    self.addBadZone(low, high)
                        
                    low=min(angulos)
                    high=pi
                    self.addBadZone(low, high)
                    
                    pieza={"center": center, 
                                "ang_low": min(angulos), 
                                "ang_high": max(angulos)}
                    self.ingredientes[id].append(pieza)
                    
                else:
                    pieza={"center": center, 
                                "ang_low": low, 
                                "ang_high": high}
                    self.ingredientes[id].append(pieza)
                    
                    if high>pi and low>pi:  #la pieza está en la parte de abajo se transporta a arriba
                        high-=pi
                        low-=pi
                    self.addBadZone(low, high)
                    
                
    
    def addBadZone(self, low, high):
#        print low, high, 
        nuevos_puntos=[]
        if low not in self.circle:
            nuevos_puntos.append(low)
        if high not in self.circle:
            nuevos_puntos.append(high)
        
        new_circle=sorted(self.circle+nuevos_puntos)
        ind_low=new_circle.index(low)
        ind_high=new_circle.index(high)
        
#        print self.value, new_circle



#        for indice in range(ind_low+1, ind_high):
#            del new_circle[indice-1]
#        
#        for indice in range(ind_low+1, ind_high-1):
#            del self.value[indice-1]

        if low not in self.circle and high not in self.circle:
            nuevos_bool=[False, self.value[ind_low-1]]
            
            self.value=self.value[:ind_low]+nuevos_bool+self.value[ind_low:]
        
        elif low not in self.circle:
            self.value.insert(ind_low-1, False)
        elif high not in self.circle:
            self.value.insert(ind_high-1, False)
        
            
        self.circle=new_circle
        
#        new_circle=[self.circle[0]]
#        new_value=[self.value[0]]
#        for bool, angle in zip(self.value, self.circle):
#            if bool!=new_value[-1]:
#                new_circle.append(angle)
#                new_value.append(bool)
#        self.value=new_value
#        self.circle=new_circle


    def center_in_polygon(self, centro, puntos):
        """If center of pizza is inside the polygon the pizza is not divisible any more and the claculation speed up
        usaré la circunferencia circunscrita del poligono para evitar el errores y simplificar el algoritmo"""
        punto1, punto2=puntos
        medio=((punto1[0]+punto2[0])/2, (punto1[1]+punto2[1])/2)
        distancia=((medio[0]-self.Cx)**2+(medio[1]-self.Cy)**2)**0.5       
        radio=((medio[0]-centro[0])**2+(medio[1]-centro[1])**2)**0.5
        return distancia<=radio
        
    def angle_Tangent(self, polygon):
        """Return the max and min angle from polygon with pizza center"""
        left_tan = right_tan = polygon[0]
        verts = iter(polygon)
        v0_x, v0_y = polygon[-2]
        v1_x, v1_y = polygon[-1]
        prev_turn = (v1_x - v0_x)*(self.Cy - v0_y) - (self.Cx - v0_x)*(v1_y - v0_y)
        v0_x = v1_x
        v0_y = v1_y
        for v1_x, v1_y in polygon:
            next_turn = (v1_x - v0_x)*(self.Cy - v0_y) - (self.Cx - v0_x)*(v1_y - v0_y)
            if prev_turn <= 0.0 and next_turn > 0.0:
                if ((v0_x - self.Cx)*(right_tan[1] - self.Cy)
                    - (right_tan[0] - self.Cx)*(v0_y - self.Cy) >= 0.0):
                    right_tan = (v0_x, v0_y)
            elif prev_turn > 0.0 and next_turn <= 0.0:
                if ((v0_x - self.Cx)*(left_tan[1] - self.Cy)
                    - (left_tan[0] - self.Cx)*(v0_y - self.Cy) <= 0.0):
                    left_tan = (v0_x, v0_y)
            v0_x = v1_x
            v0_y = v1_y
            prev_turn = next_turn
        angulo_left=atan((left_tan[1]-self.Cy)/(left_tan[0]-self.Cx)) % (2*pi)
        angulo_right=atan((right_tan[1]-self.Cy)/(right_tan[0]-self.Cx)) % (2*pi)
        if right_tan[0]<0 and right_tan[1]<0:
            angulo_right=(angulo_right+pi)%(2*pi)
        if left_tan[0]<0 and left_tan[1]<0:
            angulo_left=(angulo_left+pi)%(2*pi)
        return angulo_left, angulo_right
        

    @property
    def isDivisible(self):
        """Función que calcula si la pizza es divisible por una diagonal"""
        if not True in self.value:
            return False
        else:
#            print self.circle, self.value
            for indice, bool in enumerate(self.value):
                parte1=[]
                parte2=[]
#                print bool, 
                if bool:
                    angulo=self.circle[indice]
                    for ingrediente in self.ingredientes:
                        parte1.append(0)
                        parte2.append(0)
                        for pieza in self.ingredientes[ingrediente]:
                            if pieza["ang_low"]>angulo+pi:
                                parte2[-1]+=1
                            else:
                                parte1[-1]+=1
                            print angulo, pieza, parte1, parte2
                    if parte1==parte2:
#                        print parte1, parte2
                        return True
                        break
                    else:
                        print parte1, parte2
            return False
        



def definePolygon(n_edges,  cx, cy, vx, vy):
    """return a list with the edge coordenates of polygon"""
    radius=((vx-cx)**2+(vy-cy)**2)**0.5
    if vx==cx:
        angle=pi/2
    else:
        angle=atan((vy-cy)/(vx-cx))
        if angle<0.:
            angle+=pi
    vertices=[]
    for i in range(n_edges):
        coseno=cos(angle)
        seno=sin (angle)
        vertices.append((coseno * radius + cx, seno * radius + cy))
        angle=(angle+2*pi/n_edges) % (2*pi)
    return vertices
    

        
inputs=int(raw_input())
inputs=1
for input in range(inputs):
    data=raw_input().split()
    centerx, centery, radio=(float(s) for s in data)
    pizza=Pizza(centerx, centery, radio)
    n_ingredients=int(raw_input())
    for ingredient in range(n_ingredients):
        data=raw_input().split()
        id=data[0]
        edges=int(data[1])
        piezas=int(data[2])
        for pieza in range(piezas):
            data=raw_input().split()
            cx, cy, vx, vy=(float(s) for s in data)
            vertices=definePolygon(edges, cx, cy, vx, vy) 
            pizza.addPieze(id, (cx, cy), vertices)
    
    divisible=pizza.isDivisible
    print "Case #%i: %s" %(input+1, str(divisible).upper())
