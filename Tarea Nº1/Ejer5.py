#Dado como dato la calificación de un alumno en un examen, escriba “aprobado” 
#si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
"""Ejercicio 5"""

class Alumno:

    def __init__(self):
        pass
    
    def examen():
        calcu = float(input("Ingresar calificacion"))
        if calcu >=7:
           print("APROBADO")
           print("Felicidades, siga asi")
        else:
            print("REPROBADO")
            print("Vuelva a intentarlo")
        
    examen()    
