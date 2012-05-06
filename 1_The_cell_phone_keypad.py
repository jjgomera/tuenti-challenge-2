#!/usr/bin/python

#Challenge 1: The cell phone keypad

class keyboard(object):
    """Clase que define un teclado"""
    value=0
    position=(3, 1) #tuple with coordenates of finger, 0,0 at top left
    rotate=True     #Boolean to save the rotation in the character in a key
    cap=False       #Boolean to save the state of cap block
    keys={" ": (0, 0),
                "1": (0, 0),
                "A": (0, 1),
                "B": (0, 1),
                "C": (0, 1),
                "2": (0, 1),
                "D": (0, 2),
                "E": (0, 2),
                "F": (0, 2),
                "3": (0, 2),
                "G": (1, 0),
                "H": (1, 0),
                "I": (1, 0),
                "4": (1, 0),
                "J": (1, 1),
                "K": (1, 1),
                "L": (1, 1),
                "5": (1, 1),
                "M": (1, 2),
                "N": (1, 2),
                "O": (1, 2),
                "6": (1, 2),
                "P": (2, 0),
                "Q": (2, 0),
                "R": (2, 0),
                "S": (2, 0),
                "7": (2, 0),
                "T": (2, 1),
                "U": (2, 1),
                "V": (2, 1),
                "8": (2, 1),
                "W": (2, 2),
                "X": (2, 2),
                "Y": (2, 2),
                "Z": (2, 2),
                "9": (2, 2),
                "0": (3, 1)}
    
    orden=[[" 1", "ABC2", "DEF3"], 
                ["GHI4", "JKL5", "MNO6"], 
                ["PQRS7", "TUV8", "WXYZ9"]]
    
    def __init__(self, txt):
        "txt: el texto a escribir"
        for character in txt:
            indice=ord(character)
            character=character.upper()
            if (65<=indice<=90 and not self.cap) or (97<=indice<=122 and self.cap):
                self.go_to_key(3, 2)
                self.value+=100
                self.cap=not self.cap
                
            i, j=self.keys[character]
            self.go_to_key(i, j)
            
            self.press_button(character)
        
    
    def go_to_key(self, i, j):
        if i!=self.position[0] or j!=self.position[1]:
            if i!=self.position[0] and j!=self.position[1]:
                if i<self.position[0]:
                    newposi=self.position[0]-1
                else:
                    newposi=self.position[0]+1
                if j<self.position[1]:
                    newposj=self.position[1]-1
                else:
                    newposj=self.position[1]+1
                self.value+=350
                self.position=(newposi, newposj)
            elif i!=self.position[0]:
                if i<self.position[0]:
                    newposi=self.position[0]-1
                else:
                    newposi=self.position[0]+1
                self.value+=300
                self.position=(newposi, j)
            elif j!=self.position[1]:
                if j<self.position[1]:
                    newposj=self.position[1]-1
                else:
                    newposj=self.position[1]+1
                self.value+=200
                self.position=(i, newposj)
            self.rotate=False
            if i!=self.position[0] or j!=self.position[1]:
                self.go_to_key(i, j)
        else: self.rotate=True
            

    def press_button(self, character):
        if self.rotate:
            self.value+=500
        if character=="0":
            self.value+=100
        else:
            orden=self.orden[self.position[0]][self.position[1]].index(character)
            self.value+=(orden+1)*100

inputs=int(raw_input().split()[0])
for imput in range(inputs):
    txt=raw_input()
    teclado=keyboard(txt)
    print teclado.value


