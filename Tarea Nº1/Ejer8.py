#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
"""Ejercicio 8"""

class Numero:
    def __init__(self):
        pass
    def NumMayor(self):
        print("")
        num1 = int(input("Ingrese primer numero entero: "))
        num2 = int(input("Ingrese segudo numero entero: "))
        num3 = int(input("Ingrese tercer numero entero: "))
        print()
        if num1 > num2 and num1 > num3:
            Nm = num1
        else:
            if num2 > num3:
                Nm = num2
            else:
                Nm = num3
        print("El numero mayor es:", Nm)
        print()
        
ejercicio = Numero()
ejercicio.NumMayor()            
               