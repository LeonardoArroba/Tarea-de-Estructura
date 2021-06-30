#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
#El aspirante que obtenga calificaciones mayores que 80 en ambos examenes es aceptado; caso contrario es rechazado.
"""Ejercicio 10"""

class Escuela:
    
    def __init__(self):
        pass
    
    def variables(self):
        C1:float(input("Ingrese calificacion1:" ))
        C2:float(input("Ingrese calificacion2: "))
        if(C1 >= 80) and (C2 >=80):
            print("aceptado")
        else:
            print("rechazado")      

Escu1 = Escuela()
Escu1.variables()
    
