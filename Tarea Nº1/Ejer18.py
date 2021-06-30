#Sea un vector “Calificaciones” de 100 componentes: En forma de columna se representaría así
"""Ejercicio 18"""

class Vector:
    def __init__(self):
        pass

    def Calificaciones(self):
        calif = []
        for i in range(10):
            NuevoDato = int(input("diga el dato numero {}: ".format(i)))
            calif.append(NuevoDato)
        print("Las calificaciones son: {}".format(calif))   

resultado=Vector()
resultado.Calificaciones()
