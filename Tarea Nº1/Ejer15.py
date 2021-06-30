#Determinar si un número entero proporcionado por el usuario es primo. Un número primo
#es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo
"""Ejercicio 15"""

class Bucle1:
    def __init__(self):
        pass
    
    def control_banderas(self):
        prim = True
        div = 2
        num = int(input('Ingrese numero: '))
        while (div < num) and (prim == True):
            res = num % div
            if res == 0:
                prim = False
            else:
                div += 1
        if prim == True:
            print('Numero {} es primo'.format(num))
        else:
            print('Numero {} no es primo'.format(num))
            
bucles = Bucle1()
bucles.control_banderas()    
       