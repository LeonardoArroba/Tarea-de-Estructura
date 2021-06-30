#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
# si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
"""Ejercicio 6"""

class Empleado:
    
    def __init__(self):
        pass
    
    def sueldo():
        sueldo = float(input("sueldo del empleado"))
        if sueldo <=600:
            NuevoSueldo=sueldo+sueldo*0.10
            print()
        else:
            NuevoSueldo= sueldo
            print()
        print(NuevoSueldo,"$")
        
    sueldo()       
    
        
